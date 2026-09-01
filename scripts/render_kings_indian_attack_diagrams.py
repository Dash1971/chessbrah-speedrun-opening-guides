#!/usr/bin/env python3
"""Render the King's Indian Attack guide's reproducible SVG diagrams."""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guides" / "assets" / "kings-indian-attack"

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
        "name": "diagram-01-core-shell.svg",
        "title": "The King's Indian Attack core shell",
        "board": position("e4 e5 Nf3 Nc6 d3 Nf6 g3 d6 Bg2 Be7 O-O O-O Nbd2"),
        "arrows": [arrow("h2h3"), arrow("g1h2", BLUE), arrow("f2f4", RED), arrow("c2c3", BLUE)],
        "circles": [arrow("g2g2", YELLOW), arrow("d2d2", YELLOW)],
    },
    {
        "name": "diagram-02-complete-setup.svg",
        "title": "Complete the shell before launching the attack",
        "board": position("e4 e5 Nf3 Nc6 d3 Nf6 g3 Be7 Bg2 O-O O-O d6 Nbd2 Bg4 h3 Bh5 c3"),
        "arrows": [arrow("d1e1", BLUE), arrow("f3h4"), arrow("f2f4", RED), arrow("g1h2", BLUE)],
        "circles": [arrow("c3c3", YELLOW), arrow("h3h3", YELLOW)],
    },
    {
        "name": "diagram-03-anti-queen-trade.svg",
        "title": "Nbd2 keeps queens on after Black challenges the centre",
        "board": position("e4 e5 Nf3 Nc6 d3 d5 Nbd2 dxe4 dxe4"),
        "arrows": [arrow("d2f3", BLUE), arrow("f1g2", BLUE), arrow("e1g1", BLUE)],
        "circles": [arrow("d1d1", YELLOW), arrow("e4e4", YELLOW)],
    },
    {
        "name": "diagram-04-c3-control.svg",
        "title": "C3 controls d4 before the queen leaves d1",
        "board": position("e4 e5 Nf3 Nc6 d3 Bc5 g3 Nf6 Bg2 d5 Nbd2 dxe4 dxe4 O-O O-O Bg4 h3 Bh5 c3"),
        "arrows": [arrow("c3d4", RED), arrow("d1e1", BLUE), arrow("f3h4")],
        "circles": [arrow("d4d4", RED), arrow("c3c3", YELLOW)],
    },
    {
        "name": "diagram-05-qe1-pin-break.svg",
        "title": "Qe1 unpins the knight and supports the attack",
        "board": position("e4 e5 Nf3 Nc6 d3 Bc5 g3 Nf6 Bg2 d5 Nbd2 dxe4 dxe4 O-O O-O Bg4 h3 Bh5 c3 Qd6 Qe1"),
        "arrows": [arrow("f3h4"), arrow("f2f4", RED), arrow("g3g4", RED), arrow("e1f2", BLUE)],
        "circles": [arrow("e1e1", YELLOW), arrow("h5h5", RED)],
    },
    {
        "name": "diagram-06-ng5-light-bishop.svg",
        "title": "The Ng5 motif against Be6 and Qd7",
        "board": position("e4 e5 Nf3 Nc6 d3 d5 Nbd2 dxe4 dxe4 Nf6 g3 Bb4 c3 Ba5 Bg2 Be6 h3 Qd7"),
        "arrows": [arrow("f3g5", RED), arrow("g5e6", RED), arrow("g1h2", BLUE)],
        "circles": [arrow("e6e6", RED), arrow("h3h3", YELLOW)],
    },
    {
        "name": "diagram-07-nh4-f4.svg",
        "title": "Nh4 clears the f-pawn's road",
        "board": position("e4 e5 Nf3 Nc6 d3 h6 g3 Nf6 Bg2 Bc5 O-O d6 h3 O-O Nbd2 Be6 Kh2 Qd7 Nh4 Nh7 f4"),
        "arrows": [arrow("f4f5", RED), arrow("h4f5"), arrow("d1e1", BLUE)],
        "circles": [arrow("h4h4", YELLOW), arrow("f4f4", YELLOW)],
    },
    {
        "name": "diagram-08-gxf4-recapture.svg",
        "title": "Gxf4 keeps the attacking pawn chain",
        "board": position("e4 e5 Nf3 Nc6 d3 h6 g3 Nf6 Bg2 Bc5 O-O d6 h3 O-O Nbd2 Be6 Kh2 Qd7 Nh4 Nh7 f4 exf4 gxf4"),
        "arrows": [arrow("f4f5", RED), arrow("e4e5", RED), arrow("d1g4", BLUE)],
        "circles": [arrow("f4f4", YELLOW), arrow("h4h4", YELLOW)],
    },
    {
        "name": "diagram-09-sicilian-pawn-storm.svg",
        "title": "The f- and g-pawns advance against a castled king",
        "board": position("e4 c5 Nf3 d6 d3 Bg4 Nbd2 Nf6 h3 Bh5 g3 Bg6 Bg2 h6 O-O e6 Nh4 Bh7 f4 Be7 Kh2 O-O f5 Nc6 Ndf3 Qc8 g4"),
        "arrows": [arrow("g4g5", RED), arrow("f5f6", RED), arrow("f3h4"), arrow("d1e1", BLUE)],
        "circles": [arrow("f5f5", YELLOW), arrow("g4g4", YELLOW)],
    },
    {
        "name": "diagram-10-opposite-castling.svg",
        "title": "When Black castles long, switch to b4-b5 and Qa4",
        "board": position("e4 e5 Nf3 d6 d3 Bg4 Nbd2 Nc6 h3 Bh5 g3 Nf6 Bg2 g5 c3 h6 O-O Qe7 b4 O-O-O b5 Nb8 Qa4"),
        "arrows": [arrow("b5b6", RED), arrow("a4a7", RED), arrow("a2a4"), arrow("f3h4", BLUE)],
        "circles": [arrow("c8c8", RED), arrow("a4a4", YELLOW)],
    },
    {
        "name": "diagram-11-caro-kann.svg",
        "title": "Against the Caro-Kann: d3 and Nbd2 first",
        "board": position("e4 c6 d3 d5 Nd2 Nf6 Ngf3 Bg4 h3 Bxf3 Qxf3 e6 g3 Be7 Bg2 Nbd7 O-O O-O Qe2"),
        "arrows": [arrow("e4e5", RED), arrow("f2f4", RED), arrow("g1h2", BLUE)],
        "circles": [arrow("d2d2", YELLOW), arrow("e2e2", YELLOW)],
    },
    {
        "name": "diagram-12-french-advance.svg",
        "title": "Against the French: close with e5, then reroute",
        "board": position("e4 e6 d3 d5 Nd2 g6 g3 Bg7 Bg2 Ne7 Ngf3 O-O O-O c5 e5 d4 Re1 Nbc6 h4"),
        "arrows": [arrow("h4h5", RED), arrow("d2f1", BLUE), arrow("f1h2", BLUE), arrow("h2g4", BLUE)],
        "circles": [arrow("e5e5", YELLOW), arrow("d4d4", RED)],
    },
    {
        "name": "diagram-13-sicilian-shell.svg",
        "title": "The KIA shell against the Sicilian",
        "board": position("e4 c5 Nf3 d6 d3 Nf6 g3 e6 Bg2 Be7 O-O O-O Nbd2 a6 h3 Bd7 Kh2 Nc6 c3 Qc7 Nh4"),
        "arrows": [arrow("f2f4", RED), arrow("h4f5"), arrow("f1e1", BLUE), arrow("g3g4", RED)],
        "circles": [arrow("c3c3", YELLOW), arrow("h4h4", YELLOW)],
    },
    {
        "name": "diagram-14-scandinavian-exception.svg",
        "title": "The Scandinavian interrupts the pure KIA move order",
        "board": position("e4 d5 Nc3 e6 d3 Nf6 Qe2 dxe4 Nxe4 Be7 g3 Nxe4 dxe4 O-O Bg2 Nc6 c3"),
        "arrows": [arrow("g1f3", BLUE), arrow("e1g1", BLUE), arrow("f2f4", RED)],
        "circles": [arrow("e2e2", YELLOW), arrow("e4e4", YELLOW)],
    },
    {
        "name": "diagram-15-hippo.svg",
        "title": "Against a Hippo: finish development, then f4",
        "board": position("e4 b6 d3 Bb7 Nd2 g6 g3 Bg7 Bg2 d6 Ngf3 e6 O-O a6 h3 h6 Kh2 Nd7 Nh4 Ne7 f4"),
        "arrows": [arrow("f4f5", RED), arrow("h4f5"), arrow("c2c3", BLUE), arrow("d1e2", BLUE)],
        "circles": [arrow("f4f4", YELLOW), arrow("g2g2", YELLOW)],
    },
    {
        "name": "diagram-16-mirrored-kid.svg",
        "title": "In a mirrored King's Indian, watch the overloaded g-pawn",
        "board": position("e4 d6 Nf3 Nf6 d3 g6 g3 Bg7 Bg2 O-O O-O e5 h3 Nh5 Nh4 f5 exf5 Bxf5"),
        "arrows": [arrow("h4f5", RED), arrow("g2b7", BLUE), arrow("g3g4", RED)],
        "circles": [arrow("f5f5", RED), arrow("g6g6", YELLOW)],
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
