# London System guide — validation and engine findings

Second review completed: **2026-11-24**, against publication commit **76c5f11**.

[Guide](../guides/london-system.md) · [Source index](london-system.md) · [Game provenance](london-system-games.json) · [Position manifest](london-system-positions.json) · [Latest engine searches](london-system-second-review.json) · [Contextual tactical lines](london-system-tactical-lines.json)

## Outcome and corrections

All **22 diagram positions were correct**. The second review checked the actual SVG piece placements rather than relying only on the embedded FEN: **674 pieces**, White orientation, and all **22 exact move labels** agree with replayed source games. The rendered boards were visually inspected again.

The review found and corrected several explanations:

- The a-, e- and h-files in the cited examples are **half-open for White**, with a Black pawn still on the file. They are not fully open files.
- After game 114's **13.Bxd4 exd4**, Black has a protected d4-pawn, **not a passed pawn**: White's c2-pawn remains ahead on an adjacent file. A c3 challenge requires moving Nc3 first; Black's ...d3 makes the timing important.
- After the c-pawn has been exchanged, **...Bxf4 exf4 can isolate White's d4-pawn** by removing the e3-pawn's support. It does not automatically isolate the doubled f-pawns. The guide now includes a legal comparison from game 14 and acknowledges the doubled g-pawns after hxg3.
- Qd2 prepares queenside castling and can back Bh6; the former phrase about “connecting the bishops” was removed. Its diagram now shows the bishop route and queen support separately. The c3/Nd2 diagram explicitly identifies its arrows as support, rather than an instruction to move Ne4 into the d5-pawn.
- The early e4 example now includes Black's **...Qxd4** counterattack and the checked **Qc2** response. An attack on Bf5 does not force an immediate bishop retreat.
- The queen-chase line is presented as a **repetition resource, not a forced draw**. Black can deviate.
- The Greek-gift discussion includes both forward king escapes and the actual mating finish after ...Kh8. The rook-sacrifice discussion makes clear that the game's Bd3 still leaves White better at the tested limit.

The recorded game data is unchanged. The original API-text export is now preserved in [london-system-original-games.pgn](london-system-original-games.pgn), while the published game PGN adds video metadata. The original source SHA-256 remains `ca61dda5bf1d4059439db5eb93423742379720985a8d0856d636c6d733f82184`. All generated study chapters and affected SVG captions were regenerated from the corrected manifest.

## Latest engine method

**Stockfish 18**, python-chess distribution **1.999** / chess module **1.11.2**. Two threads, **512 MiB hash**, cleared before each search. **MultiPV 1** concentrates each search on its strongest line; see the [Stockfish analysis settings](https://official-stockfish.github.io/docs/stockfish-wiki/Stockfish-FAQ.html#optimal-settings).

Every search was started with the **complete source-game move history**, rather than an isolated FEN. This preserves castling rights, move counters and repetition history. Candidate moves were tested with separate restricted searches. No external tablebases were configured.

| Pass | Scope | Per-search node cap |
| --- | --- | --- |
| Diagram recheck | All 22 displayed positions | 10,000,000 nodes |
| Focused tactical review | 18 searches covering candidate comparisons, king escapes, mating and defensive resources | 30,000,000–100,000,000 nodes |

Total: **40 searches and 1,400,047,794 searched nodes**. Node limits are caps: the forced-mate search after ...Kh8 finished after 23,103 nodes; the other searches reached their requested budgets. The [raw record](london-system-second-review.json) includes source positions, candidate restrictions, full returned PVs, depths, actual node counts, engine identity and binary hash. [The review script](../scripts/review_london_tactics.py) can reproduce or resume the searches. Multiple threads can change exact scores and move order on another run.

Positive scores below favor **White**; divide centipawns by 100 for the displayed engine scale. These are normalized evaluations, not a count of material or a human win probability. A mating score is recorded separately. Search depth is selective, not proof that every line has been exhausted to that ply. In particular, the high reported depth on the already-forced mate must not be read as an exhaustive 245-ply proof.

This is a focused verification of the guide's positions and tactical advice. It is **not a full-game engine annotation of every move in all 130 games**, an exhaustive repertoire, or a mathematical proof of every strategic statement. Short returned PVs are preserved without inventing missing moves.

## Tactical findings

### Game 31: the symmetric Nb5 jump remains a serious mistake

After:

`1.d4 d5 2.Bf4 Bf5 3.c4 e6 4.Nc3 Nf6 5.e3 c5 6.Qb3 Qb6 7.cxd5 exd5`

| Search | Limit | White evaluation |
| --- | --- | --- |
| Before 8.Nb5: best line begins **8.Qxb6** | 50M | **+0.86** |
| After **8.Nb5?**: best defense begins **8...c4!** | 50M | **−3.81** |
| Restrict Black to the game's **8...Na6** | 50M | **−1.32** |

The checked illustration **8...c4 9.Nd6+ Qxd6 10.Bxd6 cxb3 11.Bxf8 Rxf8 12.axb3** leaves Black an extra knight for one pawn. The integrity checker verifies the complete material balance. The game result does not establish that Nb5 was sound; even ...Na6 left Black good play with accurate subsequent moves.

### Game 39: the Greek gift gives away White's advantage

| Search | Limit | White evaluation |
| --- | --- | --- |
| Before the sacrifice: best line begins **9.Qe2** | 100M | **+1.03** |
| Restrict White to **9.Bxh7+** | 100M | **−0.01** |
| After 9.Bxh7+ Kxh7 10.Ng5+: unrestricted defense selects **10...Kh6** | 100M | **+0.05** |
| Restrict that defense to **10...Kg6** | 100M | **0.00** |
| Restrict that defense to the game's **10...Kh8** | 50M | **Mate in 2 for White** |

One balanced illustrative branch is **10...Kg6 11.Qc2+ f5 12.O-O-O Qd6 13.Ndf3**. It is a sample line, not a forced sequence. Both forward king escapes require attention.

After the game move **10...Kh8**, the finish is **11.Qh5+ Kg8 12.Qh7#**. The integrity checker independently verifies that Kg8 is Black's only legal reply to Qh5+ and that Qh7 is checkmate.

### Game 66: Rxh5 is supported, and Bd3 is not an immediate losing error

After **17...Nh5**, the 100M-node restricted search supports **18.Rxh5**, evaluating the position at **+2.59** for White. An illustrative attacking continuation is **18...gxh5 19.Bxh7+ Kg7 20.Qxh5 Nxe5 21.fxe5 Rh8 22.Rf1**.

At the position after **19...Kg7**, separate 50M-node searches give **+2.52** for **20.Qxh5** and **+1.38** for the game's **20.Bd3**. The latter still favors White. The eventual loss on time does not refute the sacrifice, and these searches do not claim a forced mate.

### Games 112 and 123: distinguish a queen blunder from the serious defense

Both games share:

`1.d4 Nf6 2.Bf4 c5 3.e3 Qb6 4.Nc3 Qxb2 5.Nb5 Nd5 6.Rb1 Qxa2 7.Ra1 Qb2 8.Rb1`

After game 112's **8...Qc3+?**, the 30M-node search selects **9.Nxc3**, returning **+3.97**. The legal recorded continuation includes **9...Nxc3 10.Qc1 Nxb1 11.Qxb1**. This punishes a queen blunder; it does not refute the original pawn grab.

After game 123's **8...Qa2**:

| Candidate or reply | Limit | White evaluation |
| --- | --- | --- |
| **9.Ra1** | 100M | **+0.54** |
| **9.c4** | 100M | **−0.41** |
| After c4, unrestricted Black search selects **9...Qa5+** | 50M | **−0.60** |
| After c4, restrict Black to the game's **9...Nxf4** | 50M | **0.00** |

The scores support the preference for Ra1 and identify ...Qa5+ as a strong answer to c4, but they do not establish a forced loss after c4 or a forced win after ...Nxf4.

With full history, **9.Ra1 Qb2 10.Rb1 Qa2** produces the third occurrence of the position first reached after **6...Qxa2**. The integrity checker verifies that repetition. Black can choose another line; White is not guaranteed a draw by playing Ra1.

### Game 114: the bishop exchange remains playable

After **12...Nd4**, separate 50M-node searches give **+0.04** for **13.Bd5** and **−0.04** for **13.Bxd4**. Both are approximately balanced at the tested limit. Bd5 is a playable alternative, not a uniquely required move.

The pawn after **13.Bxd4 exd4** is protected and advanced, but not passed. White still has c2, and Nc3 currently blocks c3. The later checkmate must not be attributed to this exchange as though it loses immediately.

### Game 2: e4 allows a counterattack on d4

At the displayed position after **5.e4**, the 10M-node recheck selects **5...Qxd4**, with **+1.10** for White. Its returned line continues **6.Qc2 Bd7 7.Nb5**. The guide now includes this counterattack and identifies e4 as an active pawn investment rather than an automatic material-winning attack on Bf5.

## Integrity checks and reproduction

[The integrity checker](../scripts/check_london_system.py) now verifies:

- All **130 recovered games**, their preserved results, time controls, game links and canonical move hashes.
- All **22 FEN/source-game matches**, all **674 SVG piece placements**, orientation, exact caption move labels, and agreement between guide captions and the manifest.
- All **22 study excerpts**, their recorded main-line prefixes and every analysis variation.
- **20 contextual tactical lines**, including lines that start midgame; material balance in the Nb5 illustration; the threefold repetition; the forced mating finish; half-open files; the non-passed d4-pawn; and the isolated-d4 comparison.
- All **15 complete initial-position prose lines**, both for legality and for matching an actual source-game prefix.
- All **40 new engine records**, their source positions, restricted candidates and returned PV moves.
- Every repository PGN and variation, plus local links, guide anchors, image paths and bounded video timestamps.

The published `pgn/` collections contain 1,580 game/study entries. Including the separately preserved 130-game source copy, the complete repository replay passes for **1,710 entries and 128,445 legal moves including variations**; this count includes duplicate source material, not 1,710 unique games. All 22 boards were rendered and visually inspected again. Original headers, game scores, clocks and results are preserved; the enriched PGN adds video headers and opening comments.

```sh
python3 scripts/enrich_london_video_links.py
python3 scripts/render_london_system_diagrams.py
python3 scripts/check_london_system.py
python3 scripts/review_london_tactics.py --output sources/london-system-second-review.json
```

The engine script resumes already-completed jobs after checking their source hash, position, candidate and node limit. Use a fresh output path to recompute them. It requires a local Stockfish executable and accepts `--engine /path/to/stockfish`. The diagrams and critical sections can be run separately with `--section`.

The [initial publication engine record](london-system-engine.json) is retained for traceability. Its smaller searches are superseded by the second review where the same claim was checked. The original opening screen covered the first 15 White moves of each selected game: **1,933 move instances and 1,472 distinct position/move pairs**, at 50,000 nodes for unrestricted and played-move searches. That screen was a diagnostic, not a full-game verdict.

## PGN video-link follow-up — 2026-11-24

The original release omitted the repo’s established YouTube metadata convention. The follow-up checked a sampled video point for each of the 130 games, including historical opponent-handle changes, and added the links in headers and opening comments. All 22 study excerpts inherit the corresponding reference. The [video-link manifest](london-system-video-links.json) defines the `game-point` precision label and makes no exact game-start claim. Teaching references remain distinct.

The checker now compares the enriched games with the unchanged original source, including every original header and every move comment/clock annotation, and checks all 152 embedded URLs, episode assignments, timestamp values and runtime bounds. The preserved original source hash remains the engine-review input hash, so metadata enrichment does not invalidate or require repeating the tactical searches.
