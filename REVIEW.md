# Review of the contributed Taimanov draft

## What was retained

- The 12-chapter structure and its coverage of the main system, recaptures on c6, English Attack, quiet development, doubled c-pawn structures, Maroczy, Bowdler, Alapin, Smith-Morra, early c4, f4, and Nb3/b3 systems.
- The central teaching ideas: learn piece destinations, keep the d-pawn flexible, develop against the castled king, preserve the dark-squared bishop where it matters, and use `...Ne5-c4` with a concrete target.
- The practical tone and emphasis on decisions rather than a database-sized move tree.

## Review of the complete Claude artifact

The supplied PDF was only a clipped viewport, but the complete public artifact was subsequently recovered from Claude's versioned frame endpoint. It contains six teaching sections plus its sources-and-method section, 82 searchable teaching cards, seven recapture-tree branches, four diagrams, and a claim that 356 points were extracted from 152 games.

The artifact's target diagram is correct. Its FEN places the queen on c7, bishop on b7, and rook on c8 exactly as the caption states. An earlier version of this review incorrectly described the board as mismatched; that criticism has been withdrawn.

### What the artifact added

- A clearer hierarchy: move order, recaptures, White's sidelines, middlegame plans, structures and endgames, and practical play.
- Valuable move-order refinements: delay castling, wait for the b1-knight before `...b5`, prefer `...b6` when only the fianchetto is required, and use `...d6` as a reaction to `f4-e5`.
- Strong explanations of the long-diagonal battery, the need to advance Black's central pawns, open-file technique, two weaknesses, bishop-colour pawn placement, and practising the structure from both sides.
- A useful explanation of why apparently contradictory c6 recaptures belong to different board states.

### What still needed correction

1. **Timestamp precision:** many artifact links point to the start of the relevant game rather than the exact teaching moment. For example, “prefer the simpler continuation” links to 38:20 but occurs at 48:15; the open-file queen recapture links to 26:10 but occurs at 36:35; and “two weaknesses” links to 31:50 but occurs at 57:04. Timestamps adopted by this repository were re-indexed against the captions.
2. **Mechanical development:** the artifact calls `...Nf6`, `...Be7`, and castling “mechanical.” The corrected guide keeps Aman's setup but requires a fresh check of `e5`, `Nd5`, and c6 tactics before each move.
3. **Bowdler bishop:** the diagram caption and lookup say `...c4` traps a bishop on b3, but `Ba4` remains legal. The guide describes a severe restriction rather than a literal trap.
4. **Absolute language:** claims such as “you cannot be mated on f7,” “White has no plan,” and Sicilian endgames being inherently better were retained only as practical tendencies with the necessary qualifications.
5. **Recapture tree:** the tree is pedagogically useful but too rigid as a repertoire law. The guide keeps its board-state questions and practical defaults while requiring a tactical check in the actual position.
6. **Licensing boundary:** the artifact embeds GPLv2+ Cburnett piece artwork. The repository now uses an AGPLv3-or-later project license so compatible Lichess, Chessground, and Cburnett components can be used with their original notices preserved. The artifact's presentation code was reviewed but not copied wholesale.

## Corrections made

1. **Model-system continuation:** the supplied line continued mechanically with `...Rc8`, `...Nf6`, and castling while allowing `e5/Nd5` tactics. The chapter now ends at the stable skeleton and explicitly says the remaining move order is tactical.
2. **c6 recapture rule:** converted an over-specific decision tree into a practical hierarchy with an explicit instruction to compare queen, b-pawn, bishop, and exceptional d-pawn recaptures in the actual position.
3. **Maroczy tactic:** after `8...Bb4+ 9.Bd2`, the draft retreated with `9...Qc7` despite stating that the d4-knight was hanging. This is corrected to `9...Qxd4`.
4. **Alapin centre:** after `...d6`, the draft rebuilt with `...e6` while the e5-pawn could be removed. This is corrected to `...dxe5`.
5. **Nb3/b3 move order:** immediate `...Rb8` was too slow against `g4`; it is replaced with the central response `...Ne5`.
6. **Bowdler wording:** `...c4` restricts the bishop but does not literally trap it; `Ba4` remains legal.
7. **Evaluation language:** “near-decisive” became “clear practical advantage,” and other absolute claims were softened where the position still required work.
8. **Flexible bishop:** corrected the reconstructed guide's reference from the c8-bishop to the f8-bishop. Keeping the d-pawn home preserves the f8-bishop's diagonal through e7 and d6, matching Aman's explanation.
9. **Visual instruction:** the initial reconstructed guide had no boards, while the Stonewall and French guides each had seven. The Taimanov guide now has 13 Black-oriented SVG diagrams covering the system, both c6 recapture structures, English Attack, the `e5`/`...b4` counter-threat, `...Ne5-c4`, Maroczy tactic, Bowdler restriction, Alapin, declined Morra, f4, and Nb3 systems. Claude's four diagrams informed the selection, but inaccurate captions and under-specified positions were not copied.

## Full transcript editorial audit

The guide, source index, and annotated PGN were subsequently checked again against all 20 episode transcripts. That pass made the teaching order closer to the series:

- The guide now asks the reader to identify the first branch before playing the setup: normal `d4`, `c3`, `c4`, `Bc4`, or a Closed Sicilian.
- The repeated `e5` rule is explicit: before `...Nf6`, the knight needs a useful square; `...d6` provides d7, while a return to g8 usually signals a bad move order.
- The English Attack section distinguishes Aman's proactive `...h5` before `g4` from the separate `...h6` idea after `g4`.
- The c6 recapture section uses Aman's simple defaults, then lists the concrete exceptions rather than presenting a rigid decision tree.
- Short phrases from the series—"where the pieces go," "pawns first," "perfect pivot square," and "stick to the setup"—replace more generic explanatory language.
- Unsupported or overly broad practical advice was removed, and the prose and PGN comments were rewritten in simpler language.
- The source index is grouped by decision and includes the newly surfaced teaching moments.

## Validation

- All 12 chapters parse with `python-chess` and contain no illegal moves.
- Every Black move was checked with Stockfish 18 as a tactical guardrail.
- After correction, no retained Black move scored more than one pawn worse than the engine's first choice at the review search limit.
- Several practical repertoire choices remain outside the engine's first choice. They were retained when they reflected the speedrun's teaching and stayed playable.
- All 13 guide diagrams are generated from legal SAN sequences or the validated target-position FEN. Their provenance is recorded in the source index, and the rendering script rejects invalid boards.

Engine analysis is deliberately subordinate to the source material. Its role here is to catch tactical contradictions, not to replace Aman's repertoire with computer moves.

## Full French transcript editorial audit

The transcript-led French guide was first published when only episodes 1 and 2 had been recovered. Its later sections relied on the supplied PGN annotations and game timestamps. After all eight playlist transcripts became available, the guide and source index were checked again against the complete caption set.

That pass corrected the guide in several important ways:

- The Winawer chapter now teaches Aman's actual speedrun system: `...Ne7` rather than immediate `...c5`, followed by `...b6`, `...Ba6`, the `...Na6-b8-c6-a5-c4` reroute, a second knight on f5, and `...h5` against `g4`.
- The missing `4.Ne2` exception is explicit: avoid automatic `...Bxc3+` when another knight can replace the c3-knight, avoid trying to hold the tempting e4-pawn, and challenge the centre with `...f6`.
- The Exchange chapter now clearly separates Aman's basic short-castle setup from the more double-edged `...Bd6`, `...Nge7`, `...Nc6`, `...f6`, `...Qd7`, and long-castle setup.
- The Tarrasch chapter now includes Aman's `...Qxd5` recapture and its move-order reason: the b1-knight has already gone to d2 and cannot chase the queen with `Nc3`.
- The King's Indian Attack chapter now follows Aman's displayed setup with `...Bd6`, `...Nc6`, `...Nge7`, control of e5, `...d4-e5` against `c3`, and queenside play after the kingside is fixed.
- A source-index error was removed: episode 6 at 63:10 belongs to the King's Indian Attack model game, not a Tarrasch game. The higher-rated Tarrasch reference is at 1:11:34.
- Generic prose was replaced where possible by Aman's short recurring language: "stick to what we know," "one step backwards, two steps forwards," and "knight c4, knight f5—those are my squares."

The 61-game supplied PGN remains unchanged. The guide uses it to connect concepts to complete games, while the recovered captions remain the authority for Aman's explanations.
