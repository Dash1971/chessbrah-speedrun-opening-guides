#!/usr/bin/env python3
"""Render diagrams for the Building Habits V2 guide."""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guides" / "assets" / "building-habits-v2"

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
        "diagram-01-level-one-routine.svg",
        "Level 1: centre, development, castle, rooks",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 Bc4 Bc5 d3 d6 Be3 Be6 Qd2 Qd7 O-O O-O",
        chess.WHITE,
        [arrow("a1d1", BLUE), arrow("f1e1", BLUE), arrow("h2h3")],
        [arrow("d4d4", YELLOW), arrow("e4e4", YELLOW), arrow("d5d5", YELLOW), arrow("e5e5", YELLOW)],
    ),
    (
        "diagram-02-snorkel.svg",
        "The snorkel gives the castled king an escape square",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 Bc4 Bc5 d3 d6 O-O O-O h3 h6",
        chess.WHITE,
        [arrow("g1h2", BLUE)],
        [arrow("h3h3", YELLOW)],
    ),
    (
        "diagram-03-red-dot.svg",
        "Red dot: step off an enemy queen's line",
        "fen:6k1/8/1q6/8/8/8/5P2/6K1 w - - 0 1",
        chess.WHITE,
        [arrow("b6g1", RED), arrow("g1h2", BLUE)],
        [arrow("g1g1", RED), arrow("h2h2", YELLOW)],
    ),
    (
        "diagram-04-rpm.svg",
        "After the useful moves, RPMs gain safe space",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 Bc4 Bc5 d3 d6 Be3 Be6 Qd2 Qd7 O-O O-O h3 h6 Rad1 Rad8 Rfe1 Rfe8",
        chess.WHITE,
        [arrow("a2a3"), arrow("b2b3"), arrow("c2c3")],
        [arrow("a2a2", YELLOW), arrow("b2b2", YELLOW), arrow("c2c2", YELLOW)],
    ),
    (
        "diagram-05-active-king.svg",
        "In the endgame, the king becomes a fighting piece",
        "fen:8/5pk1/6p1/3P4/8/4K3/5PPP/8 w - - 0 1",
        chess.WHITE,
        [arrow("e3d4"), arrow("e3f4", BLUE), arrow("d5d6")],
        [arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-06-full-centre.svg",
        "Level 2: take more central space when it is safe",
        "e4 e5 Nf3 Nc6 Bc4 Nf6 d4",
        chess.WHITE,
        [arrow("d4e5", RED), arrow("e4d5", RED), arrow("b1c3", BLUE)],
        [arrow("d4d4", YELLOW), arrow("e4e4", YELLOW)],
    ),
    (
        "diagram-07-keep-the-pin.svg",
        "Keep a useful pin instead of trading automatically",
        "d4 d5 Nc3 Nf6 Bg5 h6 Bh4",
        chess.WHITE,
        [arrow("h4f6", RED), arrow("h4g3", BLUE)],
        [arrow("f6f6", YELLOW), arrow("d8d8", RED)],
    ),
    (
        "diagram-08-basic-fork.svg",
        "Level 2 tactics: one knight attacks two valuable pieces",
        "fen:r3k2r/ppp2ppp/2n5/4N3/8/8/PPP2PPP/R3K2R w KQkq - 0 1",
        chess.WHITE,
        [arrow("e5c6", RED), arrow("e5f7", RED)],
        [arrow("e5e5", YELLOW)],
    ),
    (
        "diagram-09-mating-box.svg",
        "Learn the mating box around a castled king",
        "fen:5rk1/5ppp/8/7Q/2B5/8/8/6K1 w - - 0 1",
        chess.WHITE,
        [arrow("h5f7", RED), arrow("c4f7", RED)],
        [arrow("f7f7", YELLOW)],
    ),
    (
        "diagram-10-alapin.svg",
        "Level 3 Sicilian habit: c3, d4, and d5 against Nc6",
        "e4 c5 Nf3 Nc6 c3 Nf6 d4 cxd4 cxd4 d6 d5",
        chess.WHITE,
        [arrow("d5c6", RED), arrow("b1c3", BLUE), arrow("f1d3", BLUE)],
        [arrow("c3c3", YELLOW), arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-11-central-rpm.svg",
        "At Level 3, improve the centre before a flank RPM",
        "e4 e5 Nf3 Nc6 Nc3 Nf6 Bc4 Bc5 O-O O-O",
        chess.WHITE,
        [arrow("d2d4"), arrow("a2a3", BLUE)],
        [arrow("d4d4", YELLOW)],
    ),
    (
        "diagram-12-weak-pawn.svg",
        "Occupy the square in front of a weak pawn",
        "fen:6k1/5ppp/4p3/4N3/8/8/5PPP/6K1 w - - 0 1",
        chess.WHITE,
        [arrow("e5c6", BLUE), arrow("e5f7", RED)],
        [arrow("e6e6", RED), arrow("e5e5", YELLOW)],
    ),
    (
        "diagram-13-colour-complex.svg",
        "Pawns on the bishop's colour can form a defensive chain",
        "fen:6k1/8/8/8/4P3/3P1P1P/2B5/4K3 w - - 0 1",
        chess.WHITE,
        [arrow("c2b3", BLUE), arrow("c2a4", BLUE), arrow("c2d1", BLUE)],
        [arrow("d3d3", YELLOW), arrow("e4e4", YELLOW), arrow("f3f3", YELLOW), arrow("h3h3", YELLOW)],
    ),
    (
        "diagram-14-rook-behind-pawn.svg",
        "Put the rook behind the passed pawn",
        "fen:8/5pk1/6p1/3P4/8/4K3/5PPP/3R4 w - - 0 1",
        chess.WHITE,
        [arrow("d1d4", BLUE), arrow("d5d6"), arrow("e3d4")],
        [arrow("d5d5", YELLOW)],
    ),
    (
        "diagram-15-seventh-rank.svg",
        "An active rook can invade the seventh rank",
        "fen:6k1/5ppp/8/8/8/8/5RPP/6K1 w - - 0 1",
        chess.WHITE,
        [arrow("f2f7", RED), arrow("f7g7", RED)],
        [arrow("f7f7", YELLOW)],
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
