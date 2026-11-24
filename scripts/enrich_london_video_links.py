#!/usr/bin/env python3
"""Add reviewed YouTube metadata while preserving the original game data."""
import hashlib
import json
from pathlib import Path

import chess.pgn

ROOT = Path(__file__).resolve().parents[1]


def read_games(path):
    games = []
    with path.open(encoding="utf-8-sig") as stream:
        while (game := chess.pgn.read_game(stream)) is not None:
            assert not game.errors, (path, game.errors)
            games.append(game)
    return games


def timestamp(second):
    hour, remainder = divmod(second, 3600)
    minute, second = divmod(remainder, 60)
    return f"{hour}:{minute:02d}:{second:02d}" if hour else f"{minute}:{second:02d}"


def main():
    source = ROOT / "sources/london-system-original-games.pgn"
    links = json.loads((ROOT / "sources/london-system-video-links.json").read_text())
    provenance_path = ROOT / "sources/london-system-games.json"
    provenance = json.loads(provenance_path.read_text())
    games = read_games(source)
    entries = links["games"]
    assert len(games) == len(entries) == 130
    for number, (game, entry, info) in enumerate(zip(games, entries, provenance["games"]), 1):
        assert entry["game"] == info["game"] == number
        assert game.headers["Link"] == entry["chesscom_url"] == info["url"]
        game.headers.update({"YouTubeEpisode": str(entry["episode"]),
                             "YouTubeURL": entry["url"],
                             "YouTubeEpisodeURL": entry["episode_url"],
                             "YouTubeLinkType": entry["link_type"],
                             "LinkPrecision": entry["precision"]})
        description = f"Aman Hambleton's London System, Part {entry['episode']}. "
        if entry.get("second") is not None:
            stamp = timestamp(entry["second"])
            game.headers["YouTubeTimestamp"] = stamp
            description += (f"Verified game/review point at {stamp}; this is not an exact game-start marker. ")
        else:
            description += "Episode context only; no verified timestamp is asserted. "
        game.comment = " ".join(filter(None, [game.comment, description + entry["url"]]))
        # Do not change any original headers, move comments, clock values or results.
    output = "\n\n".join(game.accept(chess.pgn.StringExporter(
        headers=True, variations=True, comments=True, columns=None)) for game in games) + "\n"
    destination = ROOT / "pgn/london-system-games.pgn"
    destination.write_text(output, encoding="utf-8")
    provenance["original_source_pgn"] = "sources/london-system-original-games.pgn"
    provenance["source_corpus_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    provenance["corpus_sha256"] = hashlib.sha256(destination.read_bytes()).hexdigest()
    provenance["video_links"] = "sources/london-system-video-links.json"
    provenance["metadata_enrichment"] = "YouTube headers and opening comments only; original headers, moves, clocks and results retained."
    provenance_path.write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    print(f"Enriched {len(games)} games; original source retained separately.")


if __name__ == "__main__":
    main()
