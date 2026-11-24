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
                prose_lines += 1
    print(json.dumps(dict(corpus_games=len(corpus), diagrams=len(manifest), excerpts=len(excerpts),
          repository_games_and_chapters=game_count, legal_moves_including_variations=move_count,
          local_links=local_links, bounded_video_timestamps=video_times,
          complete_initial_position_prose_lines=prose_lines), indent=2))


if __name__ == "__main__":
    main()
