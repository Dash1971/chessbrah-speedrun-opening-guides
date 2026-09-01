# Chessbrah Speedrun Opening Guides

Practical chess-opening guides distilled from Chessbrah speedruns, supported by annotated PGNs, diagrams, source links, and game-study references.

The aim is not to replace the videos. It is to preserve the teaching framework: recurring structures, decisions, plans, exceptions, and practical move-order rules that players can carry into their own games.

## Guides

- [The Stonewall Playbook](guides/stonewall.md)
- [The French Defense Playbook](guides/french-defense.md)
- [The Taimanov, as Aman Hambleton Plays It](guides/taimanov-sicilian.md)
- [The Queen's Gambit, as Aman Hambleton Plays It](guides/queens-gambit.md)
- [The Orangutan, as Aman Hambleton Plays It](guides/orangutan.md)
- [The King's Indian Attack, as Aman Hambleton Plays It](guides/kings-indian-attack.md)

## Study material

- [Annotated Taimanov repertoire PGN](pgn/taimanov-sicilian-repertoire.pgn)
- [Taimanov speedrun source index](sources/taimanov-speedrun.md)
- [Annotated Queen's Gambit repertoire PGN](pgn/queens-gambit-repertoire.pgn)
- [Queen's Gambit speedrun source index](sources/queens-gambit-speedrun.md)
- [Annotated Orangutan repertoire PGN](pgn/orangutan-repertoire.pgn)
- [Orangutan speedrun source index](sources/orangutan-speedrun.md)
- [Annotated King's Indian Attack repertoire PGN](pgn/kings-indian-attack-repertoire.pgn)
- [King's Indian Attack speedrun source index](sources/kings-indian-attack-speedrun.md)
- [Review notes for the contributed Taimanov draft](REVIEW.md)

The Taimanov guide includes 13 annotated board diagrams, all oriented from Black's side. The Queen's Gambit adds 15 White-oriented boards; the Orangutan and King's Indian Attack add 16 each, covering their major structures and deviations. The SVGs are built from validated FENs or legal SAN sequences by the reproducible rendering scripts.

To regenerate them:

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/render_taimanov_diagrams.py
python3 scripts/render_queens_gambit_diagrams.py
python3 scripts/render_orangutan_diagrams.py
python3 scripts/render_kings_indian_attack_diagrams.py
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
