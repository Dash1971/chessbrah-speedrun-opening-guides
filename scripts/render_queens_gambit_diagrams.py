#!/usr/bin/env python3
"""Render the Queen's Gambit guide's reproducible SVG diagrams."""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guides" / "assets" / "queens-gambit"

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
        "name": "diagram-01-core-position.svg",
        "title": "The Queen's Gambit decision point",
        "board": position("d4 d5 c4 e6 Nc3 Nf6"),
        "arrows": [arrow("c4d5", RED), arrow("c1f4", BLUE), arrow("c1g5", BLUE)],
        "circles": [arrow("d5d5", YELLOW), arrow("c4c4", YELLOW)],
    },
    {
        "name": "diagram-02-qgd-bf4.svg",
        "title": "QGD Exchange with Bf4 before Nf3",
        "board": position("d4 d5 c4 e6 Nc3 Be7 cxd5 exd5 Bf4 c6 e3 Bf5"),
        "arrows": [arrow("g2g4", RED), arrow("f1d3", BLUE), arrow("g1f3", BLUE)],
        "circles": [arrow("f4f4", YELLOW), arrow("f5f5", RED)],
    },
    {
        "name": "diagram-03-carlsbad-plans.svg",
        "title": "Carlsbad structure: choose a wing and make a plan",
        "board": position("d4 d5 c4 e6 Nc3 Nf6 cxd5 exd5 Bg5 Be7 e3 O-O Bd3 c6 Nge2 Nbd7 Qc2 Re8 O-O"),
        "arrows": [arrow("b2b4"), arrow("b4b5"), arrow("f2f3", BLUE), arrow("e3e4", BLUE)],
        "circles": [arrow("c6c6", RED), arrow("d5d5", RED)],
    },
    {
        "name": "diagram-04-tarrasch-iqp.svg",
        "title": "Against an early c5: isolate the d-pawn",
        "board": position("d4 e6 c4 d5 Nc3 c5 cxd5 exd5 Nf3 Nc6 g3 Nf6 Bg2 Be7 O-O O-O dxc5 Bxc5"),
        "arrows": [arrow("f1e1", BLUE), arrow("c1g5", BLUE), arrow("f3d4", RED)],
        "circles": [arrow("d5d5", RED)],
    },
    {
        "name": "diagram-05-qga-e4.svg",
        "title": "Queen's Gambit Accepted: occupy the center with e4",
        "board": position("d4 d5 c4 dxc4 e4 c5 d5 e6 Nc3 exd5 Nxd5 Nf6 Bxc4"),
        "arrows": [arrow("g1f3", BLUE), arrow("d1e2", BLUE), arrow("c1f4", BLUE)],
        "circles": [arrow("e4e4", YELLOW), arrow("d5d5", YELLOW)],
    },
    {
        "name": "diagram-06-qga-a4.svg",
        "title": "Queen's Gambit Accepted: a4 undermines the pawn chain",
        "board": position("d4 d5 c4 dxc4 e4 b5 a4 c6 axb5 cxb5 b3 Qc7 bxc4 bxc4 Nf3"),
        "arrows": [arrow("a4b5", RED), arrow("d1a4", BLUE), arrow("f1c4", BLUE)],
        "circles": [arrow("c4c4", RED)],
    },
    {
        "name": "diagram-07-slav-plan.svg",
        "title": "Slav: e3, Nf3 and h3 challenge the light-squared bishop",
        "board": position("d4 d5 c4 c6 Nc3 Nf6 e3 Bf5 Nf3 e6 Nh4 Bg6 Qb3 Qb6 Nxg6 hxg6"),
        "arrows": [arrow("h2h3"), arrow("g2g4"), arrow("f1d3", BLUE)],
        "circles": [arrow("g6g6", RED), arrow("b6b6", RED)],
    },
    {
        "name": "diagram-08-nimzo-qc2.svg",
        "title": "Nimzo-Indian: Qc2 keeps control of e4",
        "board": position("d4 Nf6 c4 e6 Nc3 Bb4 Qc2 O-O Nf3 d5 a3 Bxc3+ Qxc3"),
        "arrows": [arrow("e2e4"), arrow("b2b4"), arrow("c1b2", BLUE)],
        "circles": [arrow("c2c2", YELLOW), arrow("e4e4", YELLOW)],
    },
    {
        "name": "diagram-09-kings-indian.svg",
        "title": "King's Indian: the Bd3-Nge2 setup",
        "board": position("d4 Nf6 c4 g6 Nc3 Bg7 e4 d6 Bd3 O-O Nge2 e5 d5 Nbd7 O-O"),
        "arrows": [arrow("h2h3"), arrow("c1e3", BLUE), arrow("f2f4", RED)],
        "circles": [arrow("d5d5", YELLOW), arrow("e4e4", YELLOW)],
    },
    {
        "name": "diagram-10-benoni-space.svg",
        "title": "Modern Benoni: claim space, then finish development",
        "board": position("d4 Nf6 c4 e6 Nc3 c5 d5 exd5 cxd5 d6 e4 g6 h3 Bg7 Bd3 O-O Nf3"),
        "arrows": [arrow("e4e5", RED), arrow("f3d2", BLUE), arrow("d2c4", BLUE)],
        "circles": [arrow("d5d5", YELLOW), arrow("e4e4", YELLOW)],
    },
    {
        "name": "diagram-11-benko-accepted.svg",
        "title": "Benko Gambit: accept the pawns and blunt the long diagonal",
        "board": position("d4 Nf6 c4 c5 d5 b5 cxb5 a6 bxa6 Bxa6 Nc3 d6 e4 Bxf1 Kxf1 g6 Nge2 Bg7 g3 O-O"),
        "arrows": [arrow("f1g2", BLUE), arrow("g2h3", BLUE), arrow("a1b1", RED)],
        "circles": [arrow("a6a6", YELLOW), arrow("b2b2", RED)],
    },
    {
        "name": "diagram-12-dutch-fianchetto.svg",
        "title": "Dutch: fianchetto against Black's weakened dark squares",
        "board": position("d4 f5 c4 e6 g3 Nf6 Bg2 d5 Nf3 c6 O-O Bd6 b3 O-O"),
        "arrows": [arrow("c1a3", BLUE), arrow("b1c3", BLUE), arrow("f3e5", RED)],
        "circles": [arrow("e6e6", RED), arrow("g2g2", YELLOW)],
    },
    {
        "name": "diagram-13-englund.svg",
        "title": "Englund Gambit: accept, develop with tempo, watch c7",
        "board": position("d4 e5 dxe5 Nc6 Bf4 Qe7 Nc3 Nxe5 Nd5 Qd6 Nf3"),
        "arrows": [arrow("f3e5", RED), arrow("d5c7", RED), arrow("e5d6", RED)],
        "circles": [arrow("c7c7", RED), arrow("d5d5", YELLOW)],
    },
    {
        "name": "diagram-14-albin.svg",
        "title": "Albin Countergambit: a3 asks the advanced pawn a question",
        "board": position("d4 d5 c4 e5 dxe5 d4 a3 Nc6 e3 Bf5 Nf3"),
        "arrows": [arrow("e3d4", RED), arrow("b2b4", BLUE), arrow("f1d3", BLUE)],
        "circles": [arrow("d4d4", RED), arrow("a3a3", YELLOW)],
    },
    {
        "name": "diagram-15-center-takeover.svg",
        "title": "If a piece recaptures on d5, build the pawn center",
        "board": position("d4 d5 c4 Nf6 cxd5 Nxd5 e4 Nf6 Nc3 Nc6 Nf3 e6 Bd3"),
        "arrows": [arrow("e4e5"), arrow("d4d5"), arrow("f1b5", BLUE)],
        "circles": [arrow("d4d4", YELLOW), arrow("e4e4", YELLOW)],
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
