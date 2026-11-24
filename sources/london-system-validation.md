# London System guide — validation and engine findings

Review date: **2026-11-24**.

[Guide](../guides/london-system.md) · [Source index](london-system.md) · [Provenance and game identifiers](london-system-games.json) · [Position manifest](london-system-positions.json) · [Machine-readable engine record](london-system-engine.json)

## Corpus integrity and scope

The 130 published games are the historical account's standard-chess, 300-second blitz games with White, beginning with the matched post-reset aziz4ab game and ending with the finale's fidemax game. The archive window is inclusive. Twenty-three earlier White games, 47 intervening 60-second bullet games, all Black games and all 2024 activity are excluded. The selection is based on account identity, exact game endpoints and time control, not merely a London ECO code or a search for Bf4.

The historical video name **systemplayer** now belongs to another account. The run's original account has player ID **188452309** and currently uses **systematic**. Recovery through the first opponent's archive was necessary to find it. The complete PGN preserves the API's original text, moves, clock comments, results and renamed player headers; individual game blocks were joined with a consistent blank-line separator. Per-game hashes and the full corpus hash are recorded in the provenance file. The retrieval script checks account identity and expected game count before writing.

The collection contains **120 wins, 8 losses and 2 draws**. These describe the selected archive, not opening performance against equal opposition. The last game's archived White rating is **2498**. Pre-game ratings shown in the videos can differ from the archive's postgame ratings.

Episode windows follow sampled boundary opponents and the ordered archive. Parts 5 and 14 use adjacent verified boundaries plus caption evidence because frame extraction was unavailable. The source index distinguishes those inferences. Interior games are not all individually frame-matched, and no exact game-start timestamps are invented.

## What was checked

- All 130 recovered scores parse legally, retain their game URLs and have matching canonical move hashes.
- All 22 diagram positions match their specified game and ply exactly, have valid FENs, and use White's orientation.
- Each study chapter preserves the recorded main-line prefix and a short recorded continuation. Editorial analysis branches are labelled and independently replayed for legality. Study results are `*`; actual results remain in the full corpus.
- All repository PGNs, including analysis variations, are checked by the London audit script.
- Local links, guide-map anchors, image references and complete initial-position prose lines are checked. Linked video passage times are bounded by the recovered video metadata; this does not establish a frame match.
- Generated SVGs retain Cburnett/python-chess notices. Contact sheets are used to inspect piece placement, orientation, arrows, coordinates and legibility.

Run the integrity check with `python3 scripts/check_london_system.py`. Regenerate boards and excerpts with `python3 scripts/render_london_system_diagrams.py`. The fetch script uses only Python's standard library; rendering and checking use the existing python-chess dependency.

The complete repository replay passed for **1,580 games/study chapters and 119,326 legal moves including variations**. The new slice passed **98 local link/anchor/image checks, 54 bounded video passage timestamps and 15 complete initial-position prose lines**. A fresh public-API retrieval reproduced the published 130-game file byte for byte (SHA-256 `ca61dda5bf1d4059439db5eb93423742379720985a8d0856d636c6d733f82184`). All 22 boards were rendered and visually reviewed, with caption corrections made where the displayed position included Black's next move.

## Engine method and limits

**Stockfish 18**, python-chess distribution **1.999** / chess module **1.11.2**. Two engine threads. The broad screen used 128 MiB hash; focused searches used 256 MiB and cleared the hash before each position. No external tablebase path was configured.

| Pass | Scope | Search limit |
| --- | --- | --- |
| White opening screen | First 15 White moves per selected game, or fewer for shorter games: **1,933 move instances, 1,472 distinct position/move pairs** | 50,000 nodes for best play and 50,000 nodes restricted to the actual move |
| Diagram review | All 22 displayed positions | 2,000,000 nodes, MultiPV 3 |
| Candidate comparisons | Bxh7+, Rxh5, the poisoned-pawn Nb5, c4 versus Ra1, and Bxd4 in the fianchetto loss | 5,000,000 nodes per restricted candidate |
| Deeper diagram review | Greek gift, rook sacrifice, poisoned-pawn decision, and central counterplay | 10,000,000 nodes, MultiPV 3; achieved depths **22–24** |
| Additional checks | Game 31 before and after Nb5, the defense to Bxh7+, and Black's replies after the gambit's c4 | 5,000,000 nodes except **10,000,000** after Nb5 |

Scores use **White's perspective**: positive favors White. Centipawns divided by 100 give the pawn-unit evaluation scale, not a material count. Deep records store mate separately; the broad screen uses a ±100000 mate sentinel that must not be interpreted as ordinary centipawns. Short PVs are preserved when the engine returns them; no continuation has been fabricated to make a line appear complete.

The small opening screen is a diagnostic, not an opening-theory verdict. Node-limited searches, multiple threads and hash state can change scores and move rankings. The deeper checks support the concrete qualifications below. This is **not a full-game audit of every middlegame or ending**, an exhaustive repertoire against every legal defense, or a proof that the teacher's every move is best.

## Findings that changed the guide

### 1. A symmetric queen-pressure win contains a serious opening error

Game 31, after:

`1.d4 d5 2.Bf4 Bf5 3.c4 e6 4.Nc3 Nf6 5.e3 c5 6.Qb3 Qb6 7.cxd5 exd5`

The game move **8.Nb5?** is not a general-purpose refutation of ...Qb6. Before the move, a 5-million-node search prefers **8.Qxb6**, returning **+0.86** at depth 21. After Nb5, the 10-million-node search finds **8...c4!** and returns **−3.78** at depth 23.

One illustrative line is `9.Nd6+ Qxd6 10.Bxd6 cxb3 11.Bxf8 Rxf8 12.axb3`. Black emerges a piece up for a pawn. The knight's tempting fork does not save the white queen from the c-pawn.

Even the game's **8...Na6** is evaluated in Black's favor (**−1.30** in that same MultiPV search with best subsequent play). White eventually won; the result does not certify Nb5. The guide explicitly attaches this warning to the general queenside-pressure lesson.

### 2. The Greek-gift example is not a forced win

Game 39, after **8...O-O**. The actual game continues **9.Bxh7+ Kxh7 10.Ng5+ Kh8** and ends 1-0.

The unrestricted 10-million-node search before the sacrifice prefers **9.Qe2**, giving **+1.03** at depth 23. A 5-million-node restricted Bxh7+ search gives only **+0.26**. A separate 5-million-node search after Bxh7+ identifies **9...Kxh7 10.Ng5+ Kg6!**, with an approximately balanced **+0.05** evaluation at depth 22. An illustrative continuation is **11.Qc2+ f5 12.Ndf3**.

The forward king escape is the important defensive resource. The guide does not teach Bxh7+ here as forced mate or even as the best way to preserve White's opening advantage.

### 3. A sacrifice from a lost game is supported

Game 66, after **17...Nh5**. The game's attack continues **18.Rxh5 gxh5 19.Bxh7+ Kg7 20.Bd3**, and White eventually loses on time.

The 10-million-node search chooses **18.Rxh5** and returns **+2.04** at depth 22. Its illustrative continuation includes **20.Qxh5**, then **20...Nxe5 21.fxe5 Rh8 22.Rf1**. The restricted 5-million-node check also supports Rxh5 (**+2.23**). These results favor White but do not establish a forced mate. The guide separates the sound attacking commitment from the game's subsequent decisions and clock outcome.

### 4. The poisoned-pawn win and loss must be read together

Games 112 and 123 share:

`1.d4 Nf6 2.Bf4 c5 3.e3 Qb6 4.Nc3 Qxb2 5.Nb5 Nd5 6.Rb1 Qxa2 7.Ra1 Qb2 8.Rb1`

In game 112, **8...Qc3+?** loses the queen. In game 123, **8...Qa2** poses a more serious practical problem. At that latter position, the deeper search favors **9.Ra1**, giving **+0.39** at depth 24. Restricted 5-million-node comparisons give **+0.23** for Ra1 and **−0.84** for the immediate **9.c4**.

After c4, a separate search finds **9...Qa5+** with **−0.79** at depth 22. The game's **9...Nxf4** permits a return to a queen-chase line with Ra1 and is evaluated at approximately equality in that additional search. White's eventual loss therefore should not be explained as c4 forcing a loss or Nxf4 winning by force.

The guide presents a concrete gambit and its repetition resource, not a universal punishment of ...Qxb2.

### 5. A structural concession is not an immediate blunder

Game 114, after **12...Nd4**. The unrestricted 10-million-node search prefers **13.Bd5**, with **+0.10** at depth 24. Restricting White to the game's **13.Bxd4** gives **−0.12** at depth 24 in a 5-million-node search. Both are approximately balanced positions at the tested limits.

The resulting passed d-pawn is strategically important, but the later checkmate does not establish that the bishop exchange loses immediately. The guide uses this game to teach respect for central counterplay and labels Bd5 as editorial analysis.
