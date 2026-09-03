#!/usr/bin/env python3
"""Render diagrams for the transcript-led Stonewall and French guides."""

from pathlib import Path
from xml.sax.saxutils import escape

import chess
import chess.svg


ROOT = Path(__file__).resolve().parents[1]

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
        chess.parse_square(uci[:2]), chess.parse_square(uci[2:]), color=color
    )


SETS = {
    "stonewall-attack": {
        "orientation": chess.WHITE,
        "diagrams": [
            ("diagram-01-core-setup.svg", "The Stonewall Attack shell", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2", [arrow("f3e5"), arrow("d2f3", BLUE)], [arrow("d4d4", YELLOW), arrow("e3e3", YELLOW), arrow("f4f4", YELLOW), arrow("c3c3", YELLOW)]),
            ("diagram-02-nc6-f4.svg", "Nc6 threatens e5, so play f4", "d4 Nc6 f4", [arrow("c6e5", RED), arrow("f4e5", BLUE)], [arrow("f4f4", YELLOW)]),
            ("diagram-03-bishop-first.svg", "Solve the bishop before completing the shell", "d4 e6 e3 d5 Bd3 Nf6 f4", [arrow("d3h7", RED), arrow("g1f3", BLUE), arrow("b1d2", BLUE)], [arrow("d3d3", YELLOW)]),
            ("diagram-04-stop-ne4.svg", "Nd2 keeps Black out of e4", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 Nd2 Nc6 c3 Bd6 Ngf3 O-O O-O", [arrow("d2e4", BLUE), arrow("f2f3", BLUE), arrow("f6e4", RED)], [arrow("e4e4", RED)]),
            ("diagram-05-ne5.svg", "The fan favourite: Ne5", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Ne5", [arrow("e5d7", RED), arrow("e5f7", RED), arrow("d3h7", RED)], [arrow("e5e5", YELLOW)]),
            ("diagram-06-f-pawn-recapture.svg", "After Bxe5, take with the f-pawn", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Ne5 Bxe5 fxe5", [arrow("f1f7", RED), arrow("e5e6"), arrow("d3h7", RED)], [arrow("e5e5", YELLOW), arrow("f1f1", BLUE)]),
            ("diagram-07-qf3.svg", "Qf3 attacks and guards e4", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Ne5 Nd7 Qf3", [arrow("f3h3", BLUE), arrow("f3g4", BLUE), arrow("f3e4", BLUE), arrow("d3h7", RED)], [arrow("f3f3", YELLOW), arrow("e4e4", BLUE)]),
            ("diagram-08-g4-g5.svg", "Use g4-g5 to drive away a defender", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Ne5 Nd7 Qf3 f5 g4", [arrow("g4g5"), arrow("g4f5", RED), arrow("f3h3", BLUE)], [arrow("g4g4", YELLOW)]),
            ("diagram-09-qe1-h4.svg", "The queen route Qe1-h4", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Qe1", [arrow("e1h4"), arrow("h4h7", RED), arrow("f3e5", BLUE)], [arrow("e1e1", YELLOW)]),
            ("diagram-10-rook-lift.svg", "The rook lift Rf3-h3", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Ne5 Bxe5 fxe5 Nd7 Qe1 b6 Rf3", [arrow("f3h3"), arrow("h3h7", RED), arrow("e1h4", BLUE)], [arrow("f3f3", YELLOW)]),
            ("diagram-11-bad-bishop-route.svg", "The c1-bishop route: d2-e1-h4", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Bd2 Qc7 Be1 b6 Bh4", [arrow("h4f6", RED), arrow("h4g5", BLUE)], [arrow("h4h4", YELLOW)]),
            ("diagram-12-e4-break.svg", "If Black stops Ne5, play e4", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O O-O Nbd2 Qc7 Qe2 b6 e4", [arrow("e4e5"), arrow("e4d5", RED), arrow("d3h7", RED)], [arrow("e4e4", YELLOW)]),
            ("diagram-13-opposite-castling.svg", "Against queenside castling, open lines there", "d4 d5 e3 Nf6 Bd3 e6 f4 c5 c3 Nc6 Nf3 Bd6 O-O Qc7 Nbd2 Bd7 Ne5 O-O-O", [arrow("b2b4"), arrow("a2a4"), arrow("d1a4", BLUE)], [arrow("c8c8", RED)]),
        ],
    },
    "stonewall-defense": {
        "orientation": chess.BLACK,
        "diagrams": [
            ("diagram-01-core-setup.svg", "The Stonewall Defense shell", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O", [arrow("f6e4"), arrow("d8c7", BLUE), arrow("b8d7", BLUE)], [arrow("f5f5", YELLOW), arrow("e6e6", YELLOW), arrow("d5d5", YELLOW), arrow("c6c6", YELLOW)]),
            ("diagram-02-stop-e4.svg", "Priority number one: stop e4", "d4 d5 Nc3 f5", [arrow("c3e4", RED), arrow("f5e4", BLUE)], [arrow("e4e4", RED)]),
            ("diagram-03-ne4.svg", "The Stonewall knight belongs on e4", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Qc7 b3 Ne4", [arrow("e4c3", RED), arrow("e4d2", RED), arrow("e4g3", RED), arrow("e4f2", RED)], [arrow("e4e4", YELLOW)]),
            ("diagram-04-f-pawn-recapture.svg", "After Bxe4, take with the f-pawn", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Qc7 b3 Ne4 Bxe4 fxe4", [arrow("f8f2", RED), arrow("c8h3", BLUE), arrow("e4e3")], [arrow("e4e4", YELLOW), arrow("f8f8", BLUE)]),
            ("diagram-05-attack-shell.svg", "Qc7, Ne4 and the kingside battery", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Qc7 b3 Ne4 Bb2 Nd7", [arrow("d7f6", BLUE), arrow("c7h2", RED), arrow("d6h2", RED)], [arrow("e4e4", YELLOW)]),
            ("diagram-06-bad-bishop-route.svg", "Bring the c8-bishop through d7-e8-h5", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Qc7 b3 Bd7 Bb2 Be8 Rac1 Bh5", [arrow("h5f3", RED), arrow("h5g4", BLUE)], [arrow("h5h5", YELLOW)]),
            ("diagram-07-nd7-stops-ne5.svg", "Nd7 takes e5 away from White", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Nbd7", [arrow("d7e5", BLUE), arrow("f3e5", RED), arrow("f6e4")], [arrow("e5e5", RED)]),
            ("diagram-08-e5-break.svg", "Use e5 when White has not controlled it", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Nbd7 b3 e5", [arrow("e5e4"), arrow("e5d4", RED)], [arrow("e5e5", YELLOW)]),
            ("diagram-09-c5-break.svg", "Use c5 to challenge d4", "d4 d5 Nf3 f5 e3 Nf6 Bd3 e6 O-O Bd6 c4 c6 Nc3 O-O Qc2 Nbd7 b3 Qe7 Bb2 c5", [arrow("c5d4", RED), arrow("c5c4")], [arrow("d4d4", RED)]),
            ("diagram-10-meet-bf4.svg", "Against Bf4, challenge the bishop", "d4 d5 Nf3 f5 Bf4 Nf6 e3 e6 Bd3 Bd6", [arrow("d6f4", RED), arrow("f6e4")], [arrow("f4f4", RED)]),
            ("diagram-11-meet-bg5.svg", "Against Bg5, break the pin before Ne4", "d4 d5 Nf3 f5 Bg5 Nf6 Nbd2 e6 e3 Be7", [arrow("e8g8", BLUE), arrow("f6e4")], [arrow("g5g5", RED), arrow("e7e7", YELLOW)]),
            ("diagram-12-exchange-french-route.svg", "Against e4, the Exchange French may allow a Stonewall", "e4 e6 d4 d5 exd5 exd5 Bd3 f5 Nf3 Nf6 O-O Bd6 c4 c6", [arrow("f6e4"), arrow("b8d7", BLUE)], [arrow("f5f5", YELLOW), arrow("d5d5", YELLOW), arrow("c6c6", YELLOW)]),
            ("diagram-13-switch-to-french.svg", "If White advances e5, stop forcing the Stonewall", "e4 e6 d4 d5 e5 c5", [arrow("c5d4", RED), arrow("b8c6", BLUE), arrow("d8b6", BLUE)], [arrow("e5e5", RED)]),
        ],
    },
    "french-speedrun": {
        "orientation": chess.BLACK,
        "diagrams": [
            ("diagram-01-start.svg", "The French starts by challenging e4", "e4 e6 d4 d5", [arrow("c7c5"), arrow("f7f6", BLUE)], [arrow("e4e4", RED), arrow("d4d4", RED)]),
            ("diagram-02-advance.svg", "Advance: attack the pawn chain", "e4 e6 d4 d5 e5 c5 c3 Nc6 Nf3 Qb6", [arrow("c5d4", RED), arrow("b6d4", RED), arrow("b6b2", RED)], [arrow("d4d4", YELLOW)]),
            ("diagram-03-no-c3.svg", "If White has not played c3, take on d4", "e4 e6 d4 d5 e5 c5 Nf3 cxd4 Nxd4", [arrow("b8c6"), arrow("d8b6", BLUE)], [arrow("d4d4", RED)]),
            ("diagram-04-qb6-pressure.svg", "Qb6 makes White defend d4 and b2", "e4 e6 d4 d5 e5 c5 c3 Qb6 Nf3 Nc6 Bd3", [arrow("b6d4", RED), arrow("b6b2", RED), arrow("c6d4", RED)], [arrow("d4d4", YELLOW), arrow("b2b2", YELLOW)]),
            ("diagram-05-trade-bad-bishop.svg", "Trade the light-squared bishop with Bd7-b5", "e4 e6 d4 d5 e5 c5 c3 Qb6 Nf3 Bd7 Bd3 Bb5", [arrow("b5d3", RED), arrow("c5d4", BLUE)], [arrow("b5b5", YELLOW), arrow("d3d3", RED)]),
            ("diagram-06-f6-break.svg", "The second break is f6", "e4 e6 d4 d5 e5 c5 c3 Nc6 Nf3 Qb6 Bd3 Bd7 O-O cxd4 cxd4 Nge7 Nc3 Nf5", [arrow("f7f6"), arrow("f5d4", RED)], [arrow("e5e5", RED), arrow("d4d4", RED)]),
            ("diagram-07-exchange-active.svg", "Exchange: play actively, not symmetrically", "e4 e6 d4 d5 exd5 exd5 Nf3 Bd6 Bg5 f6 Be3 Ne7", [arrow("b8c6"), arrow("c8f5", BLUE), arrow("d8d7", BLUE)], [arrow("f6f6", YELLOW)]),
            ("diagram-08-exchange-long-castle.svg", "Aman's aggressive Exchange setup", "e4 e6 d4 d5 exd5 exd5 Nf3 Bd6 Bg5 f6 Be3 Ne7 Nc3 Nbc6 Qd2 Bf5 O-O-O Qd7", [arrow("e8c8", BLUE), arrow("h7h5"), arrow("g7g5")], [arrow("c8c8", YELLOW)]),
            ("diagram-09-exchange-safe.svg", "The quiet Exchange setup", "e4 e6 d4 d5 exd5 exd5 Nf3 Nf6 Bd3 Bd6 O-O O-O c3 c6", [arrow("f8e8"), arrow("b8d7", BLUE), arrow("c8g4", BLUE)], [arrow("e8e8", YELLOW)]),
            ("diagram-10-qe2-check.svg", "Against Qe2+, castle and use the e-file", "e4 e6 d4 d5 exd5 exd5 Nf3 Nf6 Qe2+ Be7 Be3 O-O", [arrow("f8e8")], [arrow("e2e2", RED), arrow("g8g8", YELLOW)]),
            ("diagram-11-winawer.svg", "Aman's Winawer: trade bishops, then use f5 and c4", "e4 e6 d4 d5 Nc3 Bb4 e5 Ne7 Nf3 b6 a3 Bxc3+ bxc3 Ba6 Bxa6 Nxa6 O-O Nb8", [arrow("b8c6"), arrow("c6a5", BLUE), arrow("a5c4"), arrow("e7f5"), arrow("h7h5", BLUE)], [arrow("c4c4", YELLOW), arrow("f5f5", YELLOW)]),
            ("diagram-12-tarrasch.svg", "Tarrasch: c5 and the Qxd5 recapture", "e4 e6 d4 d5 Nd2 c5 exd5 Qxd5 dxc5 Bxc5 Ngf3 Nf6 Bc4 Qh5", [arrow("b8c6"), arrow("c8d7", BLUE), arrow("e8g8", BLUE)], [arrow("h5h5", YELLOW), arrow("c4c4", RED)]),
            ("diagram-13-c4-outpost.svg", "The c4 square can become a knight outpost", "e4 e6 d4 d5 exd5 exd5 Nf3 Nc6 Bd3 Bd6 O-O Nge7 c3 O-O Qc2 h6 Nbd2 Na5", [arrow("a5c4"), arrow("c8f5", BLUE)], [arrow("c4c4", YELLOW), arrow("a5a5", BLUE)]),
            ("diagram-14-kia.svg", "Against the King's Indian Attack, stop e5 and take space", "e4 e6 d3 d5 Nd2 c5 Ngf3 Bd6 g3 Nc6 Bg2 Nge7 O-O O-O Re1 Qc7 c3 d4 c4 e5", [arrow("h7h6", BLUE), arrow("g7g5"), arrow("f7f6"), arrow("a7a6", BLUE), arrow("b7b5")], [arrow("e5e5", YELLOW), arrow("f4f4", RED)]),
            ("diagram-15-sidelines.svg", "Against second-move sidelines, play d5", "e4 e6 f4 d5", [arrow("d5e4", RED), arrow("g8f6", BLUE), arrow("c7c5")], [arrow("e4e4", RED)]),
            ("diagram-16-winawer-ne2.svg", "Against Winawer 4.Ne2, challenge the centre with f6", "e4 e6 d4 d5 Nc3 Bb4 Ne2 Nc6 e5 f6 exf6 Qxf6 Be3 Nge7 a3 Ba5 Qd2 O-O", [arrow("e7f5"), arrow("f6f2", RED), arrow("c6d4", RED)], [arrow("d4d4", YELLOW), arrow("f2f2", RED)]),
        ],
    },
}


def main() -> None:
    for directory, group in SETS.items():
        output = ROOT / "guides" / "assets" / directory
        output.mkdir(parents=True, exist_ok=True)
        for name, title, moves, arrows, circles in group["diagrams"]:
            board = position(moves)
            svg = chess.svg.board(
                board=board,
                orientation=group["orientation"],
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
            destination = output / name
            destination.write_text(svg, encoding="utf-8")
            destination.chmod(0o644)
            print(f"{directory}/{name}\t{board.fen()}")


if __name__ == "__main__":
    main()
