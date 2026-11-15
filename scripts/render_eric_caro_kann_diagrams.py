#!/usr/bin/env python3
"""Render actual game positions; build the companion study from the same manifest."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.pgn
import chess.svg

ROOT = Path(__file__).resolve().parents[1]
POSITIONS = ROOT / "sources/eric-caro-kann-positions.json"


def read_games(path):
    games = []
    with path.open(encoding="utf-8-sig") as stream:
        while (game := chess.pgn.read_game(stream)) is not None:
            if game.errors:
                raise ValueError((path, game.errors))
            games.append(game)
    return games


def add_line(parent, sans, comment):
    node = parent
    for san in sans.split():
        node = node.add_variation(node.board().parse_san(san))
    node.comment = comment
    return node


def main():
    games = read_games(ROOT / "pgn/eric-caro-kann-games.pgn")
    items = json.loads(POSITIONS.read_text())
    output = ROOT / "guides/assets/eric-caro-kann"
    output.mkdir(parents=True, exist_ok=True)
    chapters = []
    for index, item in enumerate(items, 1):
        source = games[item["game"] - 1]
        game = chess.pgn.Game()
        game.headers.update({"Event": item["title"], "Site": "Study excerpt",
                             "Date": source.headers["Date"], "Round": str(index),
                             "White": source.headers["White"], "Black": source.headers["Black"],
                             "Result": "*", "SourceGame": str(item["game"]),
                             "StudyId": item["id"], "Annotator": "Chessbrah speedrun opening guides"})
        game.comment = (f"Editorial study excerpt from source game {item['game']}. "
                        "Result * means this chapter ends before the game; it does not change the source result. "
                        "Annotations and analysis variations are editorial, not verbatim speech. " + source.comment)
        node = game
        for ply, move in enumerate(list(source.mainline_moves())[:item["ply"]], 1):
            node = node.add_main_variation(move)
            node.comment = item["comments"].get(str(ply), "")
        board = node.board()
        assert board.is_valid() and board.fen() == item["fen"], item["id"]
        # All extra moves are explicitly labelled analysis; the original corpus is unchanged.
        if item["id"] == "pin-warning":
            add_line(node, "Ne7", "Engine-checked editorial alternative: develops while keeping d5 protected and preparing to unpin Nc6.")
            add_line(node, "Bd6 Nxd5", "Analysis warning: the e6-pawn is pinned to Ke8 by Qe2; ...exd5 is illegal.")
            add_line(node, "Nf6 Ne5", "Played continuation: Ne5 increases the pressure on the pinned c6-knight. The deeper engine check favors White; see the report for the comparison with ...Ne7.")
        elif item["id"] == "two-knights-trap":
            add_line(node, "Qb6 Ne5+ Kd8 Nxf7+ Kc8 Kxd1 d4", "Engine-checked escape, also discussed by Eric after the game. A sample defense, not a claim that every White move is forced.")
            add_line(node, "bxc6 Bxc6+ Qd7 Bxd7+ Kxd7 Kxd1", "This is the played continuation. Black emerges a pawn down; the original game nevertheless ended 0-1.")
        elif item["id"] == "karpov-sacrifice":
            add_line(node, "Nxf7 Kxf7 Ng5+ Kg8 O-O Nf8", "Editorial defense to the sacrifice. Stockfish favors Black here; Eric lost later. Do not infer opening soundness from the final result.")
        elif item["id"] == "slav-warning":
            add_line(node, "e6 Qxb7", "Played continuation: White wins b7. The earlier bishop sortie needed a concrete answer to Qb3.")
            early = game
            for _ in range(7):
                early = early.variation(0)
            add_line(early, "e6", "Engine-checked alternative to the played 4...Bg4; keeping Bc8 at home protects b7 for now.")
        elif item["id"] == "greek-gift":
            add_line(node, "Kh3 Qd6 g3 Qg6 Rxe8+ Rxe8 Qg5", "Engine-checked illustrative defense. White has the better position; ...Bxh2+ was not a forced winning sacrifice.")
            add_line(node, "Kg1 Qh4 Kf1 Nh2+ Kg1 Ng4 f3 Qh2+ Kf1 Qh1#", "The game continuation, ending in mate. White's cooperation does not validate the initial sacrifice.")
        elif item["id"] == "knight-h4":
            add_line(node, "Qxh4 g3 Qe4+ Be2 Qxh1+", "Played continuation: the queen wins the knight, then forks king and rook. White could defend more stubbornly than 6.g3.")
        chapters.append(str(game))
        arrows = [chess.svg.Arrow.from_pgn(a) for a in item["arrows"]]
        fill = {chess.parse_square(s): "#e6a70066" for s in item["highlights"]}
        svg = chess.svg.board(board=board, orientation=chess.BLACK, size=480,
                              coordinates=True, arrows=arrows, fill=fill,
                              check=board.king(board.turn) if board.is_check() else None,
                              lastmove=board.peek() if board.move_stack else None)
        cut = svg.index(">") + 1
        notice = (f"<title>{escape(item['title'])}</title><desc>{escape(item['caption'])} "
                  f"Source game {item['game']}, ply {item['ply']}. {escape(board.fen())}</desc>"
                  "<metadata>Generated with python-chess. Cburnett-derived chess pieces by "
                  "Colin M. L. Burnett, GPL-2.0-or-later. See THIRD_PARTY_NOTICES.md.</metadata>")
        (output / item["diagram"]).write_text(svg[:cut] + notice + svg[cut:], encoding="utf-8")
    (ROOT / "pgn/eric-caro-kann-repertoire.pgn").write_text("\n\n".join(chapters) + "\n", encoding="utf-8")
    print(f"Rendered {len(items)} diagrams and {len(chapters)} annotated study chapters.")


if __name__ == "__main__":
    main()
