#!/usr/bin/env python3
"""Render the Orangutan guide's reproducible SVG diagrams."""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guides" / "assets" / "orangutan"

GREEN = "#15781bcc"
YELLOW = "#e6a700cc"
BLUE = "#003088cc"
RED = "#cc3333cc"


def position(san_moves: str) -> chess.Board:
    board = chess.Board()
    for san in san_moves.split():
        board.push_san(san)
    if not board.is_valid():
        raise ValueError(f"Invalid position after: {san_moves}")
    return board


def arrow(uci: str, color: str = GREEN) -> chess.svg.Arrow:
    return chess.svg.Arrow(chess.parse_square(uci[:2]), chess.parse_square(uci[2:]), color=color)


DIAGRAMS = [
    {
        "name": "diagram-01-core-idea.svg",
        "title": "The Orangutan's core bargain after 2.Bb2",
        "board": position("b4 e5 Bb2"),
        "arrows": [arrow("b2e5", RED), arrow("b4b5"), arrow("c2c4", BLUE)],
        "circles": [arrow("e5e5", RED), arrow("b4b4", YELLOW)],
    },
    {
        "name": "diagram-02-nc6-b5.svg",
        "title": "Meet Nc6 with b5",
        "board": position("b4 e5 Bb2 Nc6 b5"),
        "arrows": [arrow("c6d4", RED), arrow("c6b4", RED), arrow("b2e5", BLUE)],
        "circles": [arrow("c6c6", RED), arrow("b5b5", YELLOW)],
    },
    {
        "name": "diagram-03-nb4-trap.svg",
        "title": "The Nb4 motif: a3 attacks, but check every retreat",
        "board": position("b4 d5 Bb2 Nc6 b5 Nb4 a3"),
        "arrows": [arrow("a3b4", RED), arrow("b4d5", BLUE), arrow("b4d3", BLUE), arrow("b4c6", BLUE), arrow("b4a6", BLUE)],
        "circles": [arrow("b4b4", RED)],
    },
    {
        "name": "diagram-04-nd4-e3.svg",
        "title": "E3 meets the knight on d4",
        "board": position("b4 e5 Bb2 Nc6 b5 Nd4 e3"),
        "arrows": [arrow("e3d4", RED), arrow("b2e5", BLUE)],
        "circles": [arrow("d4d4", RED), arrow("e5e5", RED)],
    },
    {
        "name": "diagram-05-bxb4-center-pawn.svg",
        "title": "Black takes b4; White takes e5",
        "board": position("b4 e5 Bb2 Bxb4 Bxe5 Nf6 Nf3 O-O e3"),
        "arrows": [arrow("f1e2", BLUE), arrow("c2c4"), arrow("e5b2", BLUE)],
        "circles": [arrow("e5e5", YELLOW)],
    },
    {
        "name": "diagram-06-nf6-center.svg",
        "title": "Nf6 leaves the e5-pawn to the bishop",
        "board": position("b4 e5 Bb2 Nf6 Bxe5 Bxb4 Nf3 d6 Bb2"),
        "arrows": [arrow("e2e3"), arrow("c2c4"), arrow("f1e2", BLUE)],
        "circles": [arrow("b2b2", YELLOW), arrow("e5e5", BLUE)],
    },
    {
        "name": "diagram-07-qf6-tempo.svg",
        "title": "Qf6: develop with tempo before taking e5",
        "board": position("b4 e5 Bb2 Qf6 Nf3 Bxb4 Bxe5 Qg6"),
        "arrows": [arrow("e5c7", RED), arrow("e5g7", RED), arrow("b1c3", BLUE)],
        "circles": [arrow("g6g6", RED)],
    },
    {
        "name": "diagram-08-d6-shell.svg",
        "title": "The standard e3-c4 development shell",
        "board": position("b4 e5 Bb2 d6 e3 Nf6 c4 Be7 Nc3 O-O Nf3"),
        "arrows": [arrow("f1e2", BLUE), arrow("d2d4"), arrow("e1g1", BLUE)],
        "circles": [arrow("c4c4", YELLOW), arrow("e3e3", YELLOW)],
    },
    {
        "name": "diagram-09-f6-dark-squares.svg",
        "title": "F6 defends e5 but weakens Black's dark squares",
        "board": position("b4 e5 Bb2 f6 b5 d5 e3 Be6 Nf3 Bd6 d4 e4 Nfd2"),
        "arrows": [arrow("c2c4"), arrow("f1e2", BLUE), arrow("d2f1", BLUE)],
        "circles": [arrow("e6e6", RED), arrow("g6g6", RED)],
    },
    {
        "name": "diagram-10-d5-main.svg",
        "title": "Against d5: restrain, then challenge with c4",
        "board": position("b4 d5 Bb2 Nf6 e3 e6 b5 c5 Nf3 Bd7 c4"),
        "arrows": [arrow("c4d5", RED), arrow("b1c3", BLUE), arrow("f1e2", BLUE)],
        "circles": [arrow("b5b5", YELLOW), arrow("d5d5", RED)],
    },
    {
        "name": "diagram-11-c6-d5.svg",
        "title": "Against c6 and d5: build before opening the centre",
        "board": position("b4 c6 Bb2 d5 e3 Nf6 Nf3 Bf5 c4 e6 b5"),
        "arrows": [arrow("b5c6", RED), arrow("b1c3", BLUE), arrow("f1e2", BLUE)],
        "circles": [arrow("c6c6", RED), arrow("d5d5", RED)],
    },
    {
        "name": "diagram-12-immediate-c5.svg",
        "title": "Immediate c5: take the pawn and claim the centre",
        "board": position("b4 c5 bxc5 e6 d4 Nc6 Nf3 Nf6 Bf4"),
        "arrows": [arrow("e2e3"), arrow("c5b6", BLUE), arrow("c5c6", BLUE)],
        "circles": [arrow("c5c5", YELLOW), arrow("d4d4", YELLOW)],
    },
    {
        "name": "diagram-13-g6-setup.svg",
        "title": "Against a kingside fianchetto: occupy c4 and d4",
        "board": position("b4 Nf6 Bb2 g6 e3 Bg7 Nf3 O-O c4 d6 Be2 e5 d3"),
        "arrows": [arrow("b1c3", BLUE), arrow("d3d4"), arrow("e1g1", BLUE)],
        "circles": [arrow("c4c4", YELLOW), arrow("b2b2", YELLOW)],
    },
    {
        "name": "diagram-14-b6-mirror.svg",
        "title": "Against b6 and Bb7: use the extra queenside space",
        "board": position("b4 b6 Bb2 Bb7 e3 a5 b5 Nf6 Nf3 g6 c4 Bg7 Nc3 O-O Be2"),
        "arrows": [arrow("e1g1", BLUE), arrow("d2d4"), arrow("a2a4")],
        "circles": [arrow("b5b5", YELLOW), arrow("c4c4", YELLOW)],
    },
    {
        "name": "diagram-15-a5-space.svg",
        "title": "Meet a5 with b5 and stabilise with a4",
        "board": position("b4 a5 b5 c5 c4 b6 Bb2 Bb7 Nf3 e6 e3 Nf6 Nc3 d5 cxd5 Nxd5 a4"),
        "arrows": [arrow("a4a5"), arrow("b2g7", BLUE), arrow("c3d5", RED)],
        "circles": [arrow("b5b5", YELLOW), arrow("a4a4", YELLOW)],
    },
    {
        "name": "diagram-16-rb1-pressure.svg",
        "title": "Mature Orangutan: centre secured, rook to the b-file",
        "board": position("b4 Nf6 Bb2 a5 b5 c6 e3 cxb5 Bxb5 e6 Nf3 Be7 O-O b6 c4 O-O Nc3 Bb7 Rb1"),
        "arrows": [arrow("b1b3"), arrow("d2d4"), arrow("f1e1", BLUE)],
        "circles": [arrow("b6b6", RED), arrow("b5b5", YELLOW)],
    },
]


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for item in DIAGRAMS:
        board = item["board"]
        if not board.is_valid():
            raise ValueError(f"Invalid board for {item['name']}: {board.fen()}")
        svg = chess.svg.board(
            board=board,
            orientation=chess.WHITE,
            coordinates=True,
            size=480,
            arrows=[*item["arrows"], *item["circles"]],
        )
        opening = svg.index(">") + 1
        notice = (
            f"<title>{escape(item['title'])}</title>"
            "<metadata>Board generated with python-chess. Chess-piece geometry "
            "is derived from the Cburnett set by Colin M. L. Burnett, GPL-2.0-or-later. "
            "See THIRD_PARTY_NOTICES.md in the repository.</metadata>"
        )
        svg = f"{svg[:opening]}{notice}{svg[opening:]}"
        path = OUTPUT / item["name"]
        path.write_text(svg, encoding="utf-8")
        path.chmod(0o644)
        print(f"{item['name']}\t{board.fen()}")


if __name__ == "__main__":
    main()
