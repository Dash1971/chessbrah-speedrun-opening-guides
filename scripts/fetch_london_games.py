#!/usr/bin/env python3
"""Recover the historical London blitz run from Chess.com's public archive.

Python standard library only. Serial requests; no login or private endpoints.
The historical video handle systemplayer was renamed systematic. A new,
unrelated account now uses systemplayer; identity is checked before export. The default destination is the unchanged
source file; run enrich_london_video_links.py to regenerate the linked PGN.
"""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
ACCOUNT = "systematic"
PLAYER_ID = 188452309
FIRST = "https://www.chess.com/game/live/50356815043"
LAST = "https://www.chess.com/game/live/54591542165"


def get(url):
    request = Request(url, headers={"User-Agent":
        "ChessbrahOpeningGuideResearch/1.0 (github.com/Dash1971/chessbrah-speedrun-opening-guides)"})
    with urlopen(request, timeout=45) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "sources/london-system-original-games.pgn")
    args = parser.parse_args()
    profile = get(f"https://api.chess.com/pub/player/{ACCOUNT}")
    if profile.get("player_id") != PLAYER_ID:
        raise RuntimeError("Historical account identity changed; locate player_id 188452309 before fetching.")
    games = []
    for month in ("06", "07", "08"):
        archive = get(f"https://api.chess.com/pub/player/{ACCOUNT}/games/2022/{month}")
        games.extend(archive["games"])
    white = sorted((g for g in games if g["white"]["username"].lower() == ACCOUNT
                    and g.get("rules") == "chess" and g.get("time_class") == "blitz"
                    and g.get("time_control") == "300"), key=lambda g: g["end_time"])
    urls = [g["url"] for g in white]
    selected = white[urls.index(FIRST):urls.index(LAST) + 1]
    if len(selected) != 130 or len({g["url"] for g in selected}) != 130:
        raise RuntimeError("Archive coverage changed; review the selection before replacing the corpus.")
    text = "\n\n".join(g["pgn"].strip() for g in selected) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    print(f"Exported {len(selected)} games; SHA-256 {hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
