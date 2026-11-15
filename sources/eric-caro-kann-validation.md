# Eric's Caro-Kann guide: validation and engine findings

Review date: **2026-11-15**.

[Guide](../guides/eric-caro-kann.md) · [Sources](eric-caro-kann.md) · [Full machine-readable engine record](eric-caro-kann-engine.json) · [Position manifest](eric-caro-kann-positions.json)

## What was checked

- The 148-game published corpus has the same SHA-256 as the supplied PGN: `8a54549471ce5bfd55cbd9db4b04fe922be8237769df6c44fbc4340732d02778`.
- All **1,428 games/study chapters across the repository's 11 PGNs** parsed without errors. All **109,673 moves**, including variations, were legal from their parent positions; all visited boards passed `board.is_valid()`.
- The 22 new study chapters preserve their specified source-game prefixes. Editorial branches are labelled separately, and study results are `*` because these are excerpts.
- All 22 diagram FENs match their specified source game and ply. All SVGs were rendered and visually inspected in contact sheets for orientation, piece placement, arrows, coordinates, and legibility. They use the existing python-chess/Cburnett convention and retain component notices.
- All new guide/source links, local paths, guide-map anchors, diagram references, and linked YouTube timestamps were checked against the available playlist metadata. The time bounds check does not prove a frame match.
- The new release slice was checked for accidental credentials, personal filesystem paths, raw caption archives, and private working notes. The original public chess handles remain part of the supplied game metadata.

## Engine method and limits

Engine: **Stockfish 18**, using python-chess distribution **1.999** / chess module **1.11.2**. Two threads; 128 MiB hash for the broad screen and 256 MiB for deeper checks. No external tablebase path was configured.

| Pass | Scope | Search limit |
| --- | --- | --- |
| Opening screen | First 15 Black moves of each of the 148 games, or all Black moves when the game is shorter; 2,204 move instances, 1,787 distinct position/move pairs | 100,000 nodes for an unrestricted search, then 100,000 nodes restricted to the played move |
| Targeted comparisons | 14 critical starting positions, including alternative candidate moves | 2,000,000 nodes per search; initial MultiPV 3, followed by separate single-candidate searches |
| Diagram audit | All 22 displayed positions | 1,000,000 nodes each, clearing hash before each position |
| Deeper critical checks | The Exchange pin, Two Knights escape, Greek-gift defense, and Nd7 sacrifice | 10,000,000 nodes each, clearing hash before each position; achieved depths 22–26 |

Scores in the position/comparison records use **White's perspective**: positive means White is favored. The broad screen's `best_cp` and `played_cp` instead use **Black's perspective**, as explicitly recorded in the JSON metadata. Divide centipawns by 100 for the displayed pawn-unit scale; this is an engine evaluation scale, not a material count. Mate scores in the broad machine record use a ±100000 sentinel and must not be read as ordinary pawn evaluations.

The small opening screen is a diagnostic, not a verdict on theoretical soundness. Comparisons can move with search depth, thread scheduling, hash state, and engine version. The deeper checks investigate the instructional claims; the guide avoids precise numerical promises and forced-win claims where the search does not justify them. Some engine principal variations are short because the engine returned only a short PV; no missing continuation has been invented.

**This is not a full-game engine annotation of every middlegame/endgame, an exhaustive opening book, or a mathematical proof of every strategic statement.** In particular, a won game does not certify its opening, and a loss does not refute a sound opening choice.

## Findings that changed the instruction

### 1. The Two Knights “trap” has a tactical escape

Source: game 23, after `1.e4 c6 2.Nf3 d5 3.Nc3 Bg4 4.exd5 cxd5 5.h3 Bh5 6.Bb5+ Nc6 7.Ne5 Bxd1 8.Nxc6`.

- The recorded `8…bxc6?` permits `9.Bxc6+ Qd7 10.Bxd7+ Kxd7 11.Kxd1`, leaving Black a pawn down.
- **`8…Qb6!`** is the resource. The 10-million-node search reached depth 24 and evaluated the position at **−2.42** after best play, favoring Black.
- One illustrative continuation is `9.Ne5+ Kd8 10.Nxf7+ Kc8 11.Kxd1 d4`. The remaining white choices are not all forced.
- Therefore neither `6…Nc6` nor accepting the queen offer should be branded a losing move in this exact position. Eric's post-game analysis identifies the same queen move. The guide preserves that correction rather than quoting only his initial reaction.

### 2. A successful Greek gift was unsound

Source: game 20, after `14…Bxh2+ 15.Kxh2 Ng4+`.

- The game continues `16.Kg1` and Black wins by attack.
- **`16.Kh3!`** is the critical defense. The 10-million-node search reached depth 26 and returned **+1.57**, favoring White.
- A checked line is `16…Qd6 17.g3 Qg6 18.Rxe8+ Rxe8 19.Qg5`. It is a defensive example, not an assertion that every alternative is forced.
- The earlier candidate comparison prefers keeping the bishop with moves such as `14…Qc7` or `14…Ne4` to the played sacrifice. The guide treats the sacrifice as a warning and calculation exercise.

### 3. Eric spots the Exchange pin, but his reply can be improved

Source: game 20, after `1.e4 c6 2.d4 d5 3.exd5 cxd5 4.Nc3 Nc6 5.Bb5 Bf5 6.Nf3 e6 7.Qe2`.

- The candidate `7…Bd6` allows `8.Nxd5`; `…exd5` is illegal because it uncovers check on Ke8 from Qe2.
- Eric correctly sees that problem and plays `7…Nf6`.
- The targeted search also finds `…Nf6` less precise than alternatives including **`7…Ne7`**. The latter scored about **−0.34** in its 2-million-node candidate search, whereas a fresh 10-million-node search after `7…Nf6` reached depth 24 and returned **+0.81**, with `8.Ne5`.
- These are searches at different resulting positions and limits, so the difference is not presented as an exact error metric. The practical lesson is to solve the pins, with `…Ne7` supplied as a checked editorial improvement.

### 4. The Nd7 loss does not validate White's sacrifice

Source: game 117, after `1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Nf3 Ngf6 6.Neg5 e6 7.Bd3 Bd6 8.Nxf7`.

- The 10-million-node search reached depth 22 and returned **−2.11** with **`8…Kxf7`**, favoring Black.
- Black must still defend accurately after `9.Ng5+ Kg8`. `…Nf8` is one resource in the `10.O-O` branch shown in the study; the deeper search also examines `10.Qe2 Qe7`.
- The game was lost later. It is not presented as a refutation of `7…Bd6` or the entire `…Nd7` system.

### 5. Bishop development is conditional

- In game 55's position after `4.h4`, the targeted search supports **`4…h6`** as playable; routine `4…e6` allows a much stronger white initiative after g4. The retreat-square explanation is preserved.
- In game 99's Slav position, **`4…e6`** is a checked alternative to `4…Bg4`; the latter invites the subsequent Qb3 pressure. The guide warns about the concrete b7/d5 problem without claiming that every early Slav bishop development loses.
- In game 58, **`5…Qxh4`** really does win the loose knight. The later rook fork depends on White's `6.g3`; it is not described as forced against all sixth moves.

## Reproduce the checks

Install the repository's Python requirement and make Stockfish available on your PATH. The engine is not bundled or redistributed.

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/render_eric_caro_kann_diagrams.py
python3 scripts/check_eric_caro_kann.py
python3 scripts/check_eric_caro_kann.py --engine-suite critical --output /tmp/caro-critical.json
```

Other suites are `positions` (22 diagrams plus four deeper checks), `comparisons` (the 14 candidate comparisons), and `screen` (all 2,204 opening move instances, reusing identical position/move pairs). Use `--stockfish /path/to/stockfish` if it is not on PATH. New searches write only to the requested output; they do not silently replace the published record. Multi-threaded results need not be bit-for-bit identical.

The renderer also regenerates the separate study PGN, so edits to the study's comments or examples should be made in the position manifest or renderer and then regenerated. The unchanged complete-game corpus is never rewritten by either script.
