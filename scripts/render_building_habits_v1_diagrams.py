#!/usr/bin/env python3
"""Render diagrams for the Building Habits V1 guide."""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guides" / "assets" / "building-habits-v1"

GREEN = "#15781bcc"
YELLOW = "#e6a700cc"
BLUE = "#003088cc"
RED = "#cc3333cc"


def position(source: str) -> chess.Board:
    if source.startswith("fen:"):
        board = chess.Board(source.removeprefix("fen:"))
    else:
        board = chess.Board()
        for san in source.split():
            board.push_san(san)
    if not board.is_valid():
        raise ValueError(f"Invalid position: {source}")
    return board


def arrow(uci: str, color: str = GREEN) -> chess.svg.Arrow:
    return chess.svg.Arrow(
        chess.parse_square(uci[:2]), chess.parse_square(uci[2:]), color=color
    )


DIAGRAMS = [
    (
        "diagram-01-central-setup.svg",
        "Level 1: develop toward the centre and castle",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 Bc4 Bc5 d3 d6 Be3 Be6 Qd2 Qd7 O-O O-O",
        chess.WHITE,
        [arrow("a1d1", BLUE), arrow("f1e1", BLUE), arrow("h2h3")],
        [arrow("d4d4", YELLOW), arrow("e4e4", YELLOW), arrow("d5d5", YELLOW), arrow("e5e5", YELLOW)],
    ),
    (
        "diagram-02-kick-the-bishops.svg",
        "Use the rook pawns to question bishops on b4 and g4",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 d3 Bb4 Bd2 d6 h3 Bg4 a3",
        chess.WHITE,
        [arrow("a3b4", RED), arrow("h3g4", RED)],
        [arrow("b4b4", YELLOW), arrow("g4g4", YELLOW)],
    ),
    (
        "diagram-03-castle-connect-luft.svg",
        "Castle, connect the rooks, then make an escape square",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 Bc4 Bc5 d3 d6 Be3 Be6 Qd2 Qd7 O-O O-O h3 h6",
        chess.WHITE,
        [arrow("a1d1", BLUE), arrow("f1e1", BLUE)],
        [arrow("h3h3", YELLOW)],
    ),
    (
        "diagram-04-active-king.svg",
        "In the endgame, activate the king and push the passed pawn",
        "fen:8/5pk1/6p1/3P4/8/4K3/5PPP/8 w - - 0 1",
        chess.WHITE,
        [arrow("e3d4"), arrow("e3f4", BLUE), arrow("d5d6")],
        [arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-05-full-centre.svg",
        "Level 2: take more space when the centre is available",
        "e4 e5 Nf3 Nc6 Bc4 Nf6 d4",
        chess.WHITE,
        [arrow("d4e5", RED), arrow("e4d5", RED), arrow("b1c3", BLUE)],
        [arrow("d4d4", YELLOW), arrow("e4e4", YELLOW)],
    ),
    (
        "diagram-06-keep-the-pin.svg",
        "Keep the pin instead of trading automatically",
        "d4 d5 Nc3 Nf6 Bg5",
        chess.WHITE,
        [arrow("g5f6", RED), arrow("g5h4", BLUE)],
        [arrow("f6f6", YELLOW), arrow("d8d8", RED)],
    ),
    (
        "diagram-07-capture-away.svg",
        "The Ruy Lopez exception: dxc6 opens Black's pieces",
        "e4 e5 Nf3 Nc6 Bb5 a6 Bxc6 dxc6",
        chess.BLACK,
        [arrow("c8f5", BLUE), arrow("d8d3", BLUE)],
        [arrow("c6c6", YELLOW)],
    ),
    (
        "diagram-08-rook-behind-pawn.svg",
        "Put the rook behind a passed pawn",
        "fen:8/5pk1/6p1/3P4/8/4K3/5PPP/3R4 w - - 0 1",
        chess.WHITE,
        [arrow("d1d4", BLUE), arrow("d5d6"), arrow("e3d4")],
        [arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-09-open-file.svg",
        "Level 3: choose an open file instead of moving a rook by habit",
        "d4 d5 c4 e6 Nc3 Nf6 Nf3 Be7 Bf4 O-O e3 b6 Bd3 Bb7 O-O dxc4 Bxc4",
        chess.WHITE,
        [arrow("a1c1"), arrow("c1c7", RED)],
        [arrow("c1c1", YELLOW), arrow("c7c7", RED)],
    ),
    (
        "diagram-10-central-tension.svg",
        "Do not resolve central tension automatically",
        "d4 d5 c4 e6 Nc3 Nf6",
        chess.WHITE,
        [arrow("c4d5", RED), arrow("e2e4"), arrow("g1f3", BLUE)],
        [arrow("c4c4", YELLOW), arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-11-alapin.svg",
        "Against the Sicilian, Aman builds c3 and d4",
        "e4 c5 Nf3 d6 c3 Nf6 d4",
        chess.WHITE,
        [arrow("d4c5", RED), arrow("b1d2", BLUE), arrow("f1d3", BLUE)],
        [arrow("c3c3", YELLOW), arrow("d4d4", YELLOW)],
    ),
    (
        "diagram-12-d5-outpost.svg",
        "Level 4: build the whole plan around a permanent square",
        "e4 e5 Nf3 d6 d4 exd4 Nxd4 c5 Ne2 Nc6 Nbc3 Bd7 Nf4 Nf6 Bc4 Qe7 O-O O-O-O Re1 Ne5 Bb5 a6 Bxd7+ Qxd7 Nfd5",
        chess.WHITE,
        [arrow("d5c7", RED), arrow("d5e7", RED), arrow("d5f6", RED)],
        [arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-13-lucena.svg",
        "Level 4 endgames: know the Lucena bridge",
        "fen:1K6/1P1k4/8/8/8/8/r7/4R3 w - - 0 1",
        chess.WHITE,
        [arrow("e1e4"), arrow("b8c7", BLUE), arrow("b7b8", RED)],
        [arrow("b7b7", YELLOW)],
    ),
    (
        "diagram-14-nimzo-imbalance.svg",
        "The Nimzo creates a bishop-knight and pawn-structure imbalance",
        "d4 Nf6 c4 e6 Nc3 Bb4 e3 O-O Bd3 d5 Nf3 c5 O-O Nc6 a3 Bxc3 bxc3",
        chess.BLACK,
        [arrow("c6a5", BLUE), arrow("c5c4"), arrow("e6e5", BLUE)],
        [arrow("c2c2", YELLOW), arrow("c3c3", YELLOW)],
    ),
]


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for name, title, source, orientation, arrows, circles in DIAGRAMS:
        board = position(source)
        svg = chess.svg.board(
            board=board,
            orientation=orientation,
            coordinates=True,
            size=480,
            arrows=[*arrows, *circles],
        )
        opening = svg.index(">") + 1
        notice = (
            f"<title>{escape(title)}</title>"
            "<metadata>Board generated with python-chess. Chess-piece geometry "
            "is derived from the Cburnett set by Colin M. L. Burnett, "
            "GPL-2.0-or-later. See THIRD_PARTY_NOTICES.md.</metadata>"
        )
        svg = f"{svg[:opening]}{notice}{svg[opening:]}"
        destination = OUTPUT / name
        destination.write_text(svg, encoding="utf-8")
        destination.chmod(0o644)
        print(f"{name}\t{board.fen()}")


if __name__ == "__main__":
    main()
