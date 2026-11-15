#!/usr/bin/env python3
"""Validate chess artifacts; optionally repeat the recorded Stockfish searches.

Requires scripts/requirements.txt. Stockfish is an external executable, not bundled.
Run from any directory. --engine-suite does not overwrite the published report.
"""
import argparse
import hashlib
import json
from pathlib import Path

import chess
import chess.engine
from render_eric_caro_kann_diagrams import ROOT, POSITIONS, read_games

SOURCE_SHA = "8a54549471ce5bfd55cbd9db4b04fe922be8237769df6c44fbc4340732d02778"


def validate():
    corpus = ROOT / "pgn/eric-caro-kann-games.pgn"
    assert hashlib.sha256(corpus.read_bytes()).hexdigest() == SOURCE_SHA
    total, moves = 0, 0
    counts = {}
    for path in sorted((ROOT / "pgn").glob("*.pgn")):
        games = read_games(path)
        counts[path.name] = len(games)
        total += len(games)
        for game in games:
            stack = [game]
            while stack:
                node = stack.pop()
                board = node.board()
                assert board.is_valid(), (path, board.fen())
                for child in node.variations:
                    assert child.move in board.legal_moves, (path, child.move)
                    moves += 1
                    stack.append(child)
    games = read_games(corpus)
    assert len(games) == 148
    items = json.loads(POSITIONS.read_text())
    assert len(items) == 22
    study = read_games(ROOT / "pgn/eric-caro-kann-repertoire.pgn")
    assert len(study) == 22
    for item, chapter in zip(items, study):
        source = games[item["game"] - 1]
        source_moves = list(source.mainline_moves())[:item["ply"]]
        assert list(chapter.mainline_moves())[:item["ply"]] == source_moves
        board = source.board()
        for move in source_moves:
            board.push(move)
        assert board.fen() == item["fen"]
        assert chapter.headers["SourceGame"] == str(item["game"])
        assert chapter.headers["StudyId"] == item["id"]
        svg = ROOT / "guides/assets/eric-caro-kann" / item["diagram"]
        assert svg.exists() and "Cburnett" in svg.read_text()
        for arrow in item["arrows"]:
            chess.svg.Arrow.from_pgn(arrow)
    report = json.loads((ROOT / "sources/eric-caro-kann-engine.json").read_text())
    for entry in report["positions"]:
        board = games[entry["game"] - 1].board()
        for move in list(games[entry["game"] - 1].mainline_moves())[:entry["ply"]]:
            board.push(move)
        assert board.fen() == entry["fen"]
        pv = [chess.Move.from_uci(m) for m in entry["pv_uci"]]
        assert board.variation_san(pv) == entry["pv"]
    for entry in report["screening"]:
        game = games[entry["game"] - 1]
        board = game.board()
        for move in list(game.mainline_moves())[:entry["ply"] - 1]:
            board.push(move)
        assert board.fen() == entry["fen"] and board.turn == chess.BLACK
        assert board.san(list(game.mainline_moves())[entry["ply"] - 1]) == entry["san"]
    return {"games_and_chapters": total, "moves_including_variations": moves,
            "pgn_counts": counts, "source_sha256": SOURCE_SHA, "diagrams": len(items)}


def describe(board, info):
    return {"depth": info.get("depth"), "nodes": info.get("nodes"),
            "white_cp": info["score"].white().score(mate_score=100000),
            "mate_white": info["score"].white().mate(),
            "pv_uci": [m.uci() for m in info.get("pv", [])],
            "pv": board.variation_san(info.get("pv", []))}


def engine_checks(args):
    recorded = json.loads((ROOT / "sources/eric-caro-kann-engine.json").read_text())
    engine = chess.engine.SimpleEngine.popen_uci(args.stockfish)
    engine.configure({"Threads": 2, "Hash": 256})
    results = []
    try:
        if args.engine_suite in {"critical", "positions"}:
            specs = recorded["positions"]
            if args.engine_suite == "critical":
                specs = [s for s in specs if s["nodes_limit"] == 10000000]
            for spec in specs:
                board = chess.Board(spec["fen"])
                engine.configure({"Clear Hash": None})
                info = engine.analyse(board, chess.engine.Limit(nodes=spec["nodes_limit"]))
                results.append({"id": spec["id"], "fen": board.fen(), **describe(board, info)})
                print(spec["id"], results[-1]["white_cp"], flush=True)
        elif args.engine_suite == "comparisons":
            for spec in recorded["comparisons"]:
                board = chess.Board(spec["fen"])
                infos = engine.analyse(board, chess.engine.Limit(nodes=2000000), multipv=3)
                results.append({"id": spec["id"], "fen": board.fen(),
                                "multipv": [describe(board, info) for info in infos]})
                for option in spec["options"]:
                    if not option.get("restricted"):
                        continue
                    info = engine.analyse(board, chess.engine.Limit(nodes=2000000),
                                          root_moves=[board.parse_san(option["move"])])
                    results.append({"id": spec["id"], "move": option["move"],
                                    "fen": board.fen(), **describe(board, info)})
                print(spec["id"], flush=True)
        elif args.engine_suite == "screen":
            engine.configure({"Hash": 128})
            cache = {}
            for spec in recorded["screening"]:
                key = (spec["fen"], spec["san"])
                if key not in cache:
                    board = chess.Board(spec["fen"])
                    best = engine.analyse(board, chess.engine.Limit(nodes=100000))
                    played = engine.analyse(board, chess.engine.Limit(nodes=100000),
                                            root_moves=[board.parse_san(spec["san"])])
                    cache[key] = {"best": describe(board, best), "played": describe(board, played)}
                results.append({"game": spec["game"], "ply": spec["ply"], **cache[key]})
        return {"engine": engine.id, "suite": args.engine_suite, "results": results}
    finally:
        engine.quit()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine-suite", choices=["critical", "positions", "comparisons", "screen"])
    parser.add_argument("--stockfish", default="stockfish")
    parser.add_argument("--output", type=Path, help="Save new results without changing the published audit")
    args = parser.parse_args()
    result = {"validation": validate()}
    print(json.dumps(result["validation"], indent=2))
    if args.engine_suite:
        result["analysis"] = engine_checks(args)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
