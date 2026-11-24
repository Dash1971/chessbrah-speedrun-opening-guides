#!/usr/bin/env python3
"""Render game-derived boards and annotated excerpts from one audited manifest."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.pgn
import chess.svg

ROOT = Path(__file__).resolve().parents[1]


def read_games(path):
    games = []
    with path.open(encoding="utf-8-sig") as stream:
        while (game := chess.pgn.read_game(stream)) is not None:
            if game.errors:
                raise ValueError((path, game.errors))
            games.append(game)
    return games


def main():
    games = read_games(ROOT / "pgn/london-system-games.pgn")
    items = json.loads((ROOT / "sources/london-system-positions.json").read_text())
    output = ROOT / "guides/assets/london-system"
    output.mkdir(parents=True, exist_ok=True)
    chapters = []
    for index, item in enumerate(items, 1):
        source = games[item["game"] - 1]
        game = chess.pgn.Game()
        game.headers.update({"Event": item["title"], "Site": "Study excerpt",
                             "Date": source.headers["Date"], "Round": str(index),
                             "White": source.headers["White"], "Black": source.headers["Black"],
                             "Result": "*", "SourceGame": str(item["game"]),
                             "SourceURL": source.headers["Link"], "StudyId": item["id"],
                             "Annotator": "Chessbrah speedrun opening guides"})
        for name in ["YouTubeEpisode", "YouTubeURL", "YouTubeEpisodeURL", "YouTubeTimestamp",
                     "YouTubeLinkType", "LinkPrecision"]:
            if name in source.headers:
                game.headers[name] = source.headers[name]
        game.comment = ("Editorial study excerpt from Aman Hambleton's London series. "
                        "The video handle was systemplayer; the recovered archive uses systematic. "
                        "Result * marks an excerpt, not a change to the actual game result. "
                        "Comments and analysis variations are editorial. " + source.headers["Link"] + " " + source.comment)
        node = game
        for ply, move in enumerate(list(source.mainline_moves())[:item["ply"]], 1):
            node = node.add_main_variation(move)
            node.comment = item["comments"].get(str(ply), "")
        board = node.board()
        assert board.is_valid() and board.fen() == item["fen"], item["id"]
        recorded = node
        for san in item.get("continuation", []):
            recorded = recorded.add_main_variation(recorded.board().parse_san(san))
        if recorded is not node:
            recorded.comment = "Recorded continuation. See the complete corpus for the rest of the game and its actual result."
        for line in item.get("analysis", []):
            branch = node
            for san in line["moves"]:
                move = branch.board().parse_san(san)
                branch = next((child for child in branch.variations if child.move == move), None) or branch.add_variation(move)
            branch.comment += " Editorial analysis: " + line["comment"]
        chapters.append(str(game))
        svg = chess.svg.board(board=board, orientation=chess.WHITE, size=480,
                              coordinates=True,
                              arrows=[chess.svg.Arrow.from_pgn(a) for a in item["arrows"]],
                              check=board.king(board.turn) if board.is_check() else None,
                              lastmove=board.peek() if board.move_stack else None)
        cut = svg.index(">") + 1
        notice = (f"<title>{escape(item['title'])}</title><desc>{escape(item['caption'])} "
                  f"Source game {item['game']}, ply {item['ply']}. {escape(board.fen())}</desc>"
                  "<metadata>Generated with python-chess. Cburnett-derived pieces by "
                  "Colin M. L. Burnett, GPL-2.0-or-later. See THIRD_PARTY_NOTICES.md.</metadata>")
        (output / item["diagram"]).write_text(svg[:cut] + notice + svg[cut:], encoding="utf-8")
    (ROOT / "pgn/london-system-repertoire.pgn").write_text("\n\n".join(chapters) + "\n", encoding="utf-8")
    print(f"Rendered {len(items)} boards and annotated excerpts.")


if __name__ == "__main__":
    main()
