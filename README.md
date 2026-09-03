# Chessbrah Speedrun Opening Guides

Practical chess-opening guides distilled from Chessbrah speedruns, supported by annotated PGNs, diagrams, source links, and game-study references.

The aim is not to replace the videos. It is to preserve the teaching framework: recurring structures, decisions, plans, exceptions, and practical move-order rules that players can carry into their own games.

## Guides

- [Building Chess Habits V2, as Aman Hambleton Teaches It](guides/building-habits-v2.md)
- [Building Chess Habits V1, as Aman Hambleton Teaches It](guides/building-habits-v1.md)
- [The Stonewall Attack, as Aman Hambleton Plays It](guides/stonewall-attack.md)
- [The Stonewall Defense, as Aman Hambleton Plays It](guides/stonewall-defense.md)
- [The French Defense, as Aman Hambleton Plays It](guides/french-speedrun.md)
- [The Stonewall Playbook](guides/stonewall.md)
- [The French Defense Playbook](guides/french-defense.md)
- [The Taimanov, as Aman Hambleton Plays It](guides/taimanov-sicilian.md)
- [The Queen's Gambit, as Aman Hambleton Plays It](guides/queens-gambit.md)
- [The Orangutan, as Aman Hambleton Plays It](guides/orangutan.md)
- [The King's Indian Attack, as Aman Hambleton Plays It](guides/kings-indian-attack.md)

## Study material

- [Building Habits V2 — all 527 games](pgn/building-habits-v2-games.pgn)
- [Building Habits V2 complete source index](sources/building-habits-v2.md)
- [Building Habits V1 — all 394 games](pgn/building-habits-v1-games.pgn)
- [Building Habits V1 complete source index](sources/building-habits-v1.md)
- [Annotated Stonewall Attack games](pgn/stonewall-attack-annotated-games.pgn)
- [Stonewall Attack speedrun source index](sources/stonewall-attack-speedrun.md)
- [Annotated Stonewall Defense games](pgn/stonewall-defense-annotated-games.pgn)
- [Stonewall Defense speedrun source index](sources/stonewall-defense-speedrun.md)
- [Annotated French Defense games](pgn/french-defense-annotated-games.pgn)
- [French Defense speedrun source index](sources/french-defense-speedrun.md)
- [Annotated Taimanov repertoire PGN](pgn/taimanov-sicilian-repertoire.pgn)
- [Taimanov speedrun source index](sources/taimanov-speedrun.md)
- [Annotated Queen's Gambit repertoire PGN](pgn/queens-gambit-repertoire.pgn)
- [Queen's Gambit speedrun source index](sources/queens-gambit-speedrun.md)
- [Annotated Orangutan repertoire PGN](pgn/orangutan-repertoire.pgn)
- [Orangutan speedrun source index](sources/orangutan-speedrun.md)
- [Annotated King's Indian Attack repertoire PGN](pgn/kings-indian-attack-repertoire.pgn)
- [King's Indian Attack speedrun source index](sources/kings-indian-attack-speedrun.md)
- [Review notes for the contributed Taimanov draft](REVIEW.md)

Building Habits V2 adds 15 instructional boards across its four levels; V1 adds 14. The transcript-led Stonewall Attack, Stonewall Defense, and French guides add 41 diagrams: 13 White-oriented Stonewall Attack boards, 13 Black-oriented Stonewall Defense boards, and 15 Black-oriented French boards. The Taimanov guide includes 13 annotated boards; the Queen's Gambit adds 15; the Orangutan and King's Indian Attack add 16 each. The SVGs are built from validated FENs or legal SAN sequences by the reproducible rendering scripts.

To regenerate them:

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/render_taimanov_diagrams.py
python3 scripts/render_queens_gambit_diagrams.py
python3 scripts/render_orangutan_diagrams.py
python3 scripts/render_kings_indian_attack_diagrams.py
python3 scripts/render_stonewall_french_speedrun_diagrams.py
python3 scripts/render_building_habits_v1_diagrams.py
python3 scripts/render_building_habits_v2_diagrams.py
```

## Method

1. Start with the original speedrun videos and their game material.
2. Identify repeated structures and decisions rather than memorizing isolated move trees.
3. Preserve Aman's practical explanations and exceptions.
4. Validate PGN legality and use engine analysis as a tactical guardrail.
5. Link back to the original source wherever possible.

Engine checks are not used to rewrite the repertoire into a computer opening book. They catch illegal moves, missed tactics, and claims that are stronger than the position supports.

## Credits and rights

The teaching source is Aman Hambleton and Chessbrah. The guides are study aids built from the speedruns and linked game material; the videos remain the authoritative source.

The chess presentation defaults to Lichess conventions: a board-first interface, the Cburnett piece style, restrained controls, responsive layouts, accessible coordinates, and familiar move-navigation behaviour. Lichess is a credited design and open-source reference; this independent project is not affiliated with or endorsed by Lichess. See [DESIGN.md](DESIGN.md).

Repository-authored work is released under the GNU Affero General Public License v3.0 or later. Individual third-party components retain their own compatible licenses and attribution requirements. The Chessbrah-derived teaching material is included subject to the source-material permissions described in [RIGHTS.md](RIGHTS.md). See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for Lichess, Chessground, and chess-piece credits.
