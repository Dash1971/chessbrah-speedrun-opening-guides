#!/usr/bin/env python3
"""Audit the published London corpus, excerpt branches, boards and local links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs
import xml.etree.ElementTree as ET

import chess
import chess.pgn

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    games = []
    with path.open(encoding="utf-8-sig") as stream:
        while (game := chess.pgn.read_game(stream)) is not None:
            assert not game.errors, (path, game.errors)
            games.append(game)
    return games


def board_at(game, ply):
    board = game.board()
    for move in list(game.mainline_moves())[:ply]:
        board.push(move)
    return board


def svg_pieces(svg):
    """Read actual piece placements, independently of the SVG's FEN metadata."""
    pieces = {}
    for element in ET.fromstring(svg):
        if element.tag.rsplit("}", 1)[-1] != "use":
            continue
        reference = element.attrib.get("href", "")
        match = re.fullmatch(r"#(white|black)-(pawn|knight|bishop|rook|queen|king)", reference)
        if not match:
            continue
        offset = re.fullmatch(r"translate\((\d+), (\d+)\)", element.attrib["transform"])
        assert offset, element.attrib
        x, y = map(int, offset.groups())
        assert (x - 15) % 45 == (y - 15) % 45 == 0
        file, rank = (x - 15) // 45, 7 - (y - 15) // 45
        assert 0 <= file < 8 and 0 <= rank < 8
        square = chess.square(file, rank)
        assert square not in pieces
        piece_type = chess.PIECE_NAMES.index(match[2])
        pieces[square] = chess.Piece(piece_type, match[1] == "white")
    return pieces


def main():
    corpus_path = ROOT / "pgn/london-system-games.pgn"
    corpus = read(corpus_path)
    manifest = json.loads((ROOT / "sources/london-system-positions.json").read_text())
    provenance = json.loads((ROOT / "sources/london-system-games.json").read_text())
    excerpts = read(ROOT / "pgn/london-system-repertoire.pgn")
    assert hashlib.sha256(corpus_path.read_bytes()).hexdigest() == provenance["corpus_sha256"]
    assert len(corpus) == 130 and len(manifest) == len(excerpts) == 22
    for game, info in zip(corpus, provenance["games"]):
        assert game.headers["Link"] == info["url"]
        assert game.headers["TimeControl"] == "300"
        assert game.headers["White"].lower() == "systematic"
        assert game.headers["Result"] == info["result"]
        board = game.board()
        sans = []
        for move in game.mainline_moves():
            sans.append(board.san(move))
            board.push(move)
        assert hashlib.sha256(" ".join(sans).encode()).hexdigest() == info["moves_sha256"]
    guide = (ROOT / "guides/london-system.md").read_text()
    piece_placements = 0
    for item, excerpt in zip(manifest, excerpts):
        source = corpus[item["game"] - 1]
        source_moves = list(source.mainline_moves())
        board = source.board()
        for move in source_moves[:item["ply"]]:
            board.push(move)
        assert board.fen() == item["fen"] and board.is_valid(), item["id"]
        assert excerpt.headers["StudyId"] == item["id"]
        assert excerpt.headers["SourceGame"] == str(item["game"])
        assert excerpt.headers["Result"] == "*"
        excerpt_moves = list(excerpt.mainline_moves())
        assert excerpt_moves == source_moves[:len(excerpt_moves)], item["id"]
        svg_path = ROOT / "guides/assets/london-system" / item["diagram"]
        svg = svg_path.read_text()
        ET.fromstring(svg)
        assert item["fen"] in svg and "GPL-2.0-or-later" in svg
        assert svg_pieces(svg) == board.piece_map(), item["id"]
        piece_placements += len(board.piece_map())
        label = re.match(r"After (\d+)(\.\.\.|\.)([A-Za-z0-9=+#-]+)[?!]*:", item["caption"])
        assert label, item["id"]
        number, dots, san = label.groups()
        expected_ply = 2 * (int(number) - 1) + (2 if dots == "..." else 1)
        assert expected_ply == item["ply"], item["id"]
        parent = board.copy()
        last_move = parent.pop()
        assert parent.san(last_move) == san, item["id"]
        assert item["caption"] in guide, item["id"]
        assert f'assets/london-system/{item["diagram"]}' in guide
    tactical_lines = json.loads((ROOT / "sources/london-system-tactical-lines.json").read_text())
    endings = {}
    for line in tactical_lines:
        board = board_at(corpus[line["game"] - 1], line["source_ply"])
        for san in line["moves"]:
            board.push_san(san)
            assert board.is_valid(), line["id"]
        endings[line["id"]] = board
    # Check material, repetition and pawn-structure statements, not only legal SAN.
    board = endings["nb5-c4"]
    assert len(board.pieces(chess.KNIGHT, chess.BLACK)) == len(board.pieces(chess.KNIGHT, chess.WHITE)) + 1
    assert len(board.pieces(chess.PAWN, chess.WHITE)) == len(board.pieces(chess.PAWN, chess.BLACK)) + 1
    for piece_type in [chess.BISHOP, chess.ROOK, chess.QUEEN]:
        assert len(board.pieces(piece_type, chess.WHITE)) == len(board.pieces(piece_type, chess.BLACK))
    assert endings["queen-chase-repetition"].is_repetition(3)
    board = board_at(corpus[38], 20)
    board.push_san("Qh5+")
    assert len(list(board.legal_moves)) == 1
    assert endings["greek-gift-mate"].is_checkmate()
    board = endings["isolated-d4"]
    assert board.piece_at(chess.D4) == chess.Piece(chess.PAWN, chess.WHITE)
    assert not (board.pieces_mask(chess.PAWN, chess.WHITE) & (chess.BB_FILE_C | chess.BB_FILE_E))
    board = endings["protected-not-passed"]
    assert board.piece_at(chess.D4) == chess.Piece(chess.PAWN, chess.BLACK)
    assert board.piece_at(chess.C2) == chess.Piece(chess.PAWN, chess.WHITE)
    assert board.piece_at(chess.C3) == chess.Piece(chess.KNIGHT, chess.WHITE)
    assert chess.C3 not in [m.to_square for m in board.legal_moves if m.from_square == chess.C2]
    for board, file in [(endings["recapture-d4"], 4), (endings["queens-exchanged"], 0),
                        (board_at(corpus[13], 15), 7)]:
        mask = chess.BB_FILES[file]
        assert not (board.pieces_mask(chess.PAWN, chess.WHITE) & mask)
        assert board.pieces_mask(chess.PAWN, chess.BLACK) & mask
    review = json.loads((ROOT / "sources/london-system-second-review.json").read_text())
    assert review["source_sha256"] == provenance["corpus_sha256"]
    assert len(review["results"]) == len({x["id"] for x in review["results"]}) == 40
    engine_pv_moves = 0
    for result in review["results"]:
        board = board_at(corpus[result["game"] - 1], result["ply"])
        assert board.fen() == result["fen"], result["id"]
        assert result["nodes"] >= result["node_limit"] or result["mate"] is not None
        if result["root_san"]:
            assert board.parse_san(result["pv"][0]) == board.parse_san(result["root_san"])
        for san in result["pv"]:
            board.push_san(san)
            assert board.is_valid(), result["id"]
            engine_pv_moves += 1
    game_count = move_count = 0
    for path in sorted((ROOT / "pgn").glob("*.pgn")):
        for game in read(path):
            game_count += 1
            stack = [game]
            while stack:
                node = stack.pop()
                board = node.board()
                assert board.is_valid(), (path, game.headers)
                for child in node.variations:
                    assert child.move in board.legal_moves, (path, child.move)
                    move_count += 1
                    stack.append(child)
    files = [ROOT / p for p in ["README.md", "guides/london-system.md",
             "sources/london-system.md", "sources/london-system-validation.md"]]
    local_links = video_times = prose_lines = 0
    for path in files:
        text = path.read_text()
        for link in re.findall(r'\]\(([^\s)]+)\)', text) + re.findall(r'src="([^"]+)"', text):
            if link.startswith("https:"):
                query = parse_qs(urlparse(link).query)
                if "v" in query and "t" in query:
                    duration = next((v["duration"] for v in provenance["videos"] if v["id"] == query["v"][0]), None)
                    if duration is not None:
                        assert 0 <= int(query["t"][0].rstrip("s")) < duration, link
                        video_times += 1
                continue
            rel, _, anchor = link.partition("#")
            target = (path.parent / unquote(rel)).resolve() if rel else path
            assert target.exists(), (path, link)
            if anchor and target.suffix == ".md":
                headings = re.findall(r"^#{1,6} (.+)$", target.read_text(), re.M)
                anchors = {re.sub(r"[^\w\- ]", "", h.lower().replace("`", "")).replace(" ", "-") for h in headings}
                assert unquote(anchor) in anchors, (path, link)
            local_links += 1
        if path.name == "london-system.md":
            for literal in re.findall(r"`([^`]+)`", text):
                if not literal.startswith("1."):
                    continue
                board = chess.Board()
                line = re.sub(r"\d+\.(?:\.\.|…)?", " ", literal)
                for token in line.split():
                    board.push_san(token.rstrip("?!"))
                quoted_moves = board.move_stack
                assert any(list(game.mainline_moves())[:len(quoted_moves)] == quoted_moves for game in corpus), literal
                prose_lines += 1
    print(json.dumps(dict(corpus_games=len(corpus), diagrams=len(manifest), excerpts=len(excerpts),
          repository_games_and_chapters=game_count, legal_moves_including_variations=move_count,
          local_links=local_links, bounded_video_timestamps=video_times,
          complete_initial_position_prose_lines=prose_lines,
          svg_piece_placements=piece_placements, exact_caption_move_labels=len(manifest),
          contextual_tactical_lines=len(tactical_lines), reviewed_engine_searches=len(review["results"]),
          legal_engine_pv_moves=engine_pv_moves), indent=2))


if __name__ == "__main__":
    main()
