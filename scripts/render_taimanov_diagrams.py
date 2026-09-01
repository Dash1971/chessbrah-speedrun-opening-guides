#!/usr/bin/env python3
"""Render the Taimanov guide's reproducible SVG diagrams.

Requires python-chess. Every position is either built from a legal SAN sequence
or supplied as a validated FEN from the reviewed source artifact.
"""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "guides" / "assets" / "taimanov"

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
    return chess.svg.Arrow(
        chess.parse_square(uci[:2]),
        chess.parse_square(uci[2:]),
        color=color,
    )


DIAGRAMS = [
    {
        "name": "diagram-01-core-setup.svg",
        "title": "Core Taimanov setup after 8...Bb7",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Be3 a6 Be2 b5 O-O Bb7"),
        "arrows": [arrow("b5b4"), arrow("c6d4", BLUE)],
        "circles": [arrow("d7d7", YELLOW)],
    },
    {
        "name": "diagram-02-target-position.svg",
        "title": "Mature Taimanov target position",
        "board": chess.Board("2r2rk1/1bqpbppp/p1n1pn2/1p4B1/3NP3/P1N2B2/1PPQ1PPP/R3R1K1 b - - 0 1"),
        "arrows": [arrow("b5b4")],
        "circles": [arrow("d7d7", YELLOW)],
    },
    {
        "name": "diagram-03-qxc6-battery.svg",
        "title": "Queen recapture on c6 aligned with the b7-bishop",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Be3 a6 Be2 b5 O-O Bb7 Nxc6 Qxc6"),
        "arrows": [arrow("b7c6", BLUE), arrow("c6e4", RED)],
        "circles": [arrow("e4e4", RED)],
    },
    {
        "name": "diagram-04-bxc6-d5.svg",
        "title": "The c6-pawn is ready to recapture on d5",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Nxc6 bxc6 Bd3 d5 exd5"),
        "arrows": [arrow("c6d5", RED)],
        "circles": [arrow("c6c6", YELLOW), arrow("d5d5", RED), arrow("e6e6", YELLOW)],
    },
    {
        "name": "diagram-05-english-attack.svg",
        "title": "English Attack queenside pawn race",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Be3 a6 Qd2 Nf6 O-O-O Ng4 Nxc6 Nxe3 Qxe3 Qxc6 f3 b5 Kb1 b4"),
        "arrows": [arrow("b4c3", RED), arrow("a6a5"), arrow("a5a4"), arrow("a4a3")],
        "circles": [arrow("c3c3", RED)],
    },
    {
        "name": "diagram-06-ne5-pivot.svg",
        "title": "The Ne5-c4 pivot against Bd3 and Qd2",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 Qc7 Be3 a6 Qd2 Nf6 Bd3 Ne5"),
        "arrows": [arrow("e5d3", RED), arrow("e5c4"), arrow("c4d2", RED)],
        "circles": [arrow("e5e5", YELLOW), arrow("c4c4", YELLOW)],
    },
    {
        "name": "diagram-07-maroczy-tactic.svg",
        "title": "Maroczy tactic: Qxd4 wins the loose knight",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 c4 Nf6 Nc3 Bc5 Be3 Qb6 Na4 Bb4+ Bd2"),
        "arrows": [arrow("b6d4", RED), arrow("b4d2", BLUE)],
        "circles": [arrow("d4d4", RED)],
    },
    {
        "name": "diagram-08-bowdler-clamp.svg",
        "title": "Bowdler clamp with Ba4 still available",
        "board": position("e4 c5 Nf3 e6 Bc4 a6 Nc3 b5 Bb3 c4"),
        "arrows": [arrow("b3a4", YELLOW), arrow("b5b4")],
        "circles": [arrow("a4a4", YELLOW)],
    },
    {
        "name": "diagram-09-alapin-reset.svg",
        "title": "Alapin reset: the knight retreats to c7",
        "board": position("e4 c5 c3 Nf6 e5 Nd5 c4 Nc7"),
        "arrows": [arrow("d7d6"), arrow("c7e6"), arrow("b7b5")],
        "circles": [arrow("c7c7", YELLOW)],
    },
    {
        "name": "diagram-10-morra-declined.svg",
        "title": "Aman's declined Smith-Morra setup",
        "board": position("e4 c5 d4 cxd4 c3 d3 Bxd3 Nc6 Nf3 d6 O-O g6 Re1 Bg4"),
        "arrows": [arrow("g4f3", RED), arrow("f8g7", BLUE)],
        "circles": [arrow("f3f3", RED)],
    },
    {
        "name": "diagram-11-f4-adaptation.svg",
        "title": "Central counterplay against an f4 system",
        "board": position("e4 c5 f4 e6 Nf3 Nc6 Bb5 Qc7 Bxc6 Qxc6 d3 d5 e5 d4"),
        "arrows": [arrow("d4d3"), arrow("g8e7", BLUE), arrow("e7f5", BLUE)],
        "circles": [arrow("d4d4", YELLOW), arrow("e5e5", YELLOW)],
    },
    {
        "name": "diagram-12-nb3-counter.svg",
        "title": "Ne5 meets the Nb3 and kingside-pawn setup",
        "board": position("e4 c5 Nf3 e6 d4 cxd4 Nxd4 Nc6 Nc3 a6 Nb3 Nf6 Be3 b5 Qf3 Qc7 O-O-O d6 g4 Ne5"),
        "arrows": [arrow("e5g4", RED), arrow("b5b4"), arrow("e5c4")],
        "circles": [arrow("e5e5", YELLOW), arrow("c4c4", YELLOW)],
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
            orientation=chess.BLACK,
            coordinates=True,
            size=480,
            arrows=[*item["arrows"], *item["circles"]],
        )
        opening = svg.index(">") + 1
        embedded_notice = (
            f"<title>{escape(item['title'])}</title>"
            "<metadata>Board generated with python-chess. Chess-piece geometry "
            "is derived from the Cburnett set by Colin M. L. Burnett, GPL-2.0-or-later. "
            "See THIRD_PARTY_NOTICES.md in the repository.</metadata>"
        )
        svg = f"{svg[:opening]}{embedded_notice}{svg[opening:]}"
        path = OUTPUT / item["name"]
        path.write_text(svg, encoding="utf-8")
        path.chmod(0o644)
        print(f"{item['name']}\t{board.fen()}")


if __name__ == "__main__":
    main()
