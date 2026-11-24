#!/usr/bin/env python3
"""Repeat the London review with full game history and single-PV searches.

Results are resumable. Use --section diagrams or --section critical to run
the two independent parts separately. A source hash prevents stale reuse.
"""
import argparse
import hashlib
import json
import shutil
from pathlib import Path

import chess
import chess.engine
import chess.pgn

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", default=shutil.which("stockfish"))
    parser.add_argument("--section", choices=["all", "diagrams", "critical"], default="all")
    parser.add_argument("--only", action="append", help="Run only these job IDs; repeat for multiple IDs.")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = ROOT / "sources/london-system-original-games.pgn"
    games = []
    with source.open() as stream:
        while (game := chess.pgn.read_game(stream)) is not None:
            assert not game.errors
            games.append(game)
    positions = json.loads((ROOT / "sources/london-system-positions.json").read_text())
    jobs = []
    if args.section in ["all", "diagrams"]:
        jobs += [(x["id"], x["game"], x["ply"], 10_000_000, None) for x in positions]
    if args.section in ["all", "critical"]:
        jobs += [
            ("g31-before-nb5", 31, 14, 50_000_000, None),
            ("g31-after-nb5", 31, 15, 50_000_000, None),
            ("g31-na6", 31, 15, 50_000_000, "Na6"),
            ("g39-before-sacrifice", 39, 16, 100_000_000, None),
            ("g39-bxh7", 39, 16, 100_000_000, "Bxh7+"),
            ("g39-king-escape", 39, 19, 100_000_000, None),
            ("g39-kg6", 39, 19, 100_000_000, "Kg6"),
            ("g39-kh8", 39, 19, 50_000_000, "Kh8"),
            ("g66-rxh5", 66, 34, 100_000_000, "Rxh5"),
            ("g66-qxh5", 66, 38, 50_000_000, "Qxh5"),
            ("g66-bd3", 66, 38, 50_000_000, "Bd3"),
            ("g123-ra1", 123, 16, 100_000_000, "Ra1"),
            ("g123-c4", 123, 16, 100_000_000, "c4"),
            ("g123-answer-c4", 123, 17, 50_000_000, None),
            ("g123-nxf4", 123, 17, 50_000_000, "Nxf4"),
            ("g112-punish-qc3", 112, 16, 30_000_000, None),
            ("g114-bd5", 114, 24, 50_000_000, "Bd5"),
            ("g114-bxd4", 114, 24, 50_000_000, "Bxd4"),
        ]
    if args.only:
        jobs = [job for job in jobs if job[0] in args.only]
        if {job[0] for job in jobs} != set(args.only):
            parser.error("Unknown job ID or job outside the selected section")
    if not args.engine:
        parser.error("Stockfish was not found; supply --engine /path/to/stockfish")
    engine = chess.engine.SimpleEngine.popen_uci(args.engine)
    engine.configure({"Threads": 2, "Hash": 512})
    signature = dict(source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                     engine=engine.id, threads=2, hash_mb=512, multipv=1,
                     game_history="Complete source prefix from the initial position; repetition history retained.")
    record = dict(**signature, results=[])
    if args.output.exists():
        record = json.loads(args.output.read_text())
        assert all(record[k] == v for k, v in signature.items()), "Stale review output"
    completed = {x["id"]: x for x in record["results"]}
    try:
        for identifier, game_number, ply, nodes, candidate in jobs:
            board = games[game_number - 1].board()
            for move in list(games[game_number - 1].mainline_moves())[:ply]:
                board.push(move)
            if identifier in completed:
                previous = completed[identifier]
                expected = dict(game=game_number, ply=ply, fen=board.fen(),
                                node_limit=nodes, root_san=candidate)
                assert all(previous[k] == v for k, v in expected.items()), "Stale review job: " + identifier
                continue
            engine.configure({"Clear Hash": None})
            kwargs = {"multipv": 1}
            if candidate:
                kwargs["root_moves"] = [board.parse_san(candidate)]
            info = engine.analyse(board, chess.engine.Limit(nodes=nodes), **kwargs)[0]
            replay = board.copy()
            pv = []
            for move in info.get("pv", []):
                pv.append(replay.san(move))
                replay.push(move)
            score = info["score"].white()
            result = dict(id=identifier, game=game_number, ply=ply, fen=board.fen(),
                          root_san=candidate, node_limit=nodes, nodes=info["nodes"],
                          depth=info["depth"], seldepth=info.get("seldepth"),
                          white_cp=score.score(), mate=score.mate(), pv=pv,
                          can_claim_threefold=board.can_claim_threefold_repetition())
            record["results"].append(result)
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(record, indent=2) + "\n")
            print(identifier, result["white_cp"], result["mate"], result["depth"], " ".join(pv[:12]), flush=True)
    finally:
        engine.quit()


if __name__ == "__main__":
    main()
