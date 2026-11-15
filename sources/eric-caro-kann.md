# Eric Hansen's Caro-Kann / …c6 speedrun: sources

[Guide](../guides/eric-caro-kann.md) · [Complete supplied corpus](../pgn/eric-caro-kann-games.pgn) · [Annotated study](../pgn/eric-caro-kann-repertoire.pgn) · [Validation](eric-caro-kann-validation.md)

## Evidence and attribution

The teacher is **Eric Hansen**, with Chessbrah. This series is not Aman Hambleton's repertoire. Original videos remain the authority for spoken explanations. The written guide and study annotations are editorial paraphrases and position-based analysis, not quotations or an official Chessbrah publication.

The 148-game user-supplied PGN is preserved byte-for-byte, including comments, clock annotations, game order, names, results, and source-link precision. No analysis is inserted into that file. The separate 22-chapter PGN is a study: it stops source games early, uses `Result "*"`, and labels editorial continuations and corrections. Its `SourceGame` tag refers to the one-based game number in the complete corpus.

- Account: `PoojaFan69`, Black in all 148 games.
- Dates: 2023-05-09 through 2023-07-25; all games have `TimeControl "180"` (three-minute games).
- Recorded Black ratings: 436–2621. These are PGN values, not a claim that every rating was shown in a video.
- Results: 141 Black wins, seven White wins. This describes a grandmaster's speedrun sample, not the opening's expected score at equal strength.
- Source checksum (SHA-256): `8a54549471ce5bfd55cbd9db4b04fe922be8237769df6c44fbc4340732d02778`.
- 138 games have supplied approximate video start links. Game 127 has only a playlist link and a disputed off-camera note. Games 140–148 are labelled by the supplier as beyond the series endpoint and have only playlist links.
- The supplied ECO headers divide into 89 B-code, 43 D-code, and 16 A-code games. These are header counts, not an independent classification of all transpositions.

## Playlist and caption inventory

[Original playlist](https://www.youtube.com/playlist?list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX), enumerated on 2026-11-15 with yt-dlp 2026.10.26. Preserve the observed order: the 2000–2200 video appears after 2300–2400 in the playlist. The supplied PGN is in its own game order and is not rearranged to match that playlist anomaly.

English auto-caption tracks were recovered directly with youtube-transcript-api 1.2.5 for **12/12 videos**, with **11,344 segments** and approximately **11.41 hours of caption span**. Each track has a beginning and ending consistent with the listed runtime (caption end may slightly exceed rounded video duration). This is a retrieval and timestamp-span check, not proof of verbatim caption accuracy or a full audiovisual audit. The guide review read the opening windows and relevant teaching/recap passages across all 12 tracks, then expanded the tactical exceptions in context. It does not claim an exhaustive review of every sentence or every endgame. Raw tracks and working excerpts are retained locally and are not republished.

| Playlist position | Video / rating title | Runtime | Caption segments | First–last caption end (seconds) | Games with supplied timed links |
| --- | --- | --- | --- | --- | --- |
| 1 | [400-600](https://www.youtube.com/watch?v=rCZrddCQWY8) | 43:04 | 698 | 0.12–2585.66 | 8 |
| 2 | [600-800](https://www.youtube.com/watch?v=YDUfNGkU3GA) | 60:23 | 1099 | 1.44–3623.96 | 12 |
| 3 | [800-1000](https://www.youtube.com/watch?v=tyFiLrOpKYg) | 58:18 | 1109 | 1.44–3499.10 | 11 |
| 4 | [1000-1200](https://www.youtube.com/watch?v=-Gp7ZDRtDKo) | 66:29 | 1186 | 1.44–3990.56 | 13 |
| 5 | [1200-1400](https://www.youtube.com/watch?v=HI0Q1obUbXA) | 65:46 | 1158 | 1.44–3947.06 | 15 |
| 6 | [1400-1600](https://www.youtube.com/watch?v=0B8A_9sGGbM) | 61:23 | 1049 | 1.44–3683.20 | 14 |
| 7 | [1600-1800](https://www.youtube.com/watch?v=VEl-6jrdpDA) | 67:07 | 1047 | 7.93–4028.60 | 13 |
| 8 | [1800-2000](https://www.youtube.com/watch?v=qRgmW6SW_b0) | 58:16 | 965 | 1.44–3496.88 | 12 |
| 9 | [2200-2300](https://www.youtube.com/watch?v=Y0LtCzfbdwA) | 34:45 | 578 | 1.44–2084.66 | 6 |
| 10 | [2300-2400](https://www.youtube.com/watch?v=FmT5SkOnEHE) | 55:22 | 696 | 1.44–3322.00 | 10 |
| 11 | [2000-2200](https://www.youtube.com/watch?v=mKmkrye5lUs) | 55:22 | 930 | 1.44–3323.36 | 12 |
| 12 | [2400-2600](https://www.youtube.com/watch?v=wNuYG9_1uf4) | 58:18 | 829 | 7.93–3499.60 | 12 |

## Provenance correction: game 127

The source comment says Hollywood_Chess–PoojaFan69 was played off camera between the last two rating bands. The opening of the 2400–2600 video instead resumes a game after a glitch and mentions **Hollywood Chess at about 1:04**, describing a Slav position. This strongly suggests that the game is **partially shown**, not wholly off camera. The supplied comment remains unchanged so the original evidence is preserved. No exact start timestamp or independent frame match is asserted. [Caption passage](https://www.youtube.com/watch?v=wNuYG9_1uf4&t=11s).

## Teaching passages used

These are caption-grounded teaching links. The game index below uses the separately supplied approximate game starts. A teaching time is not necessarily a game start.

| Decision | Passage | Position / games |
| --- | --- | --- |
| Caro-Kann versus Slav identity | [Introduction, 0:07](https://www.youtube.com/watch?v=rCZrddCQWY8&t=7s) | Whole repertoire |
| Two Advance approaches | [400–600, 1:16](https://www.youtube.com/watch?v=rCZrddCQWY8&t=76s) | Game 1 |
| Do not premove d5 against Qh5 | [400–600, 11:02](https://www.youtube.com/watch?v=rCZrddCQWY8&t=662s) | Game 3 |
| Bishop before e6 / knight development | [400–600, 21:40](https://www.youtube.com/watch?v=rCZrddCQWY8&t=1300s) | Game 5 |
| Simple Two Knights exchange | [400–600, 33:20](https://www.youtube.com/watch?v=rCZrddCQWY8&t=2000s) | Game 7 |
| Early Nf3 allows Bg4 | [600–800, 11:50](https://www.youtube.com/watch?v=YDUfNGkU3GA&t=710s) | Game 12 |
| Exchange pins and development | [600–800, 56:20](https://www.youtube.com/watch?v=YDUfNGkU3GA&t=3380s) | Game 20; engine refines the reply |
| Greek-gift attack as played | [600–800, 57:53](https://www.youtube.com/watch?v=YDUfNGkU3GA&t=3473s) | Game 20; Kh3 is an engine correction |
| Ne5 trap and Qb6 resource | [800–1000, 13:42](https://www.youtube.com/watch?v=tyFiLrOpKYg&t=822s) | Game 23 post-game analysis |
| Knight f5 versus bishop h5 | [800–1000, 36:10](https://www.youtube.com/watch?v=tyFiLrOpKYg&t=2170s) | Game 28 |
| Rook file and Na5-c4 | [800–1000, 42:20](https://www.youtube.com/watch?v=tyFiLrOpKYg&t=2540s) | Game 29 |
| Fantasy e6 and Nh6 | [1000–1200, 6:20](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&t=380s) | Game 33 |
| Ne7, Nd7, dxc4, Nb6-d5 | [1000–1200, 46:00](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&t=2760s) | Game 41 |
| Stonewall with an outside bishop | [1000–1200, 55:50](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&t=3350s) | Game 43 |
| h4 and h6 retreat square | [1200–1400, 49:40](https://www.youtube.com/watch?v=HI0Q1obUbXA&t=2980s) | Game 55 |
| Nh4, Qxh4, Qe4+ | [1200–1400, 1:02:20](https://www.youtube.com/watch?v=HI0Q1obUbXA&t=3740s) | Game 58 |
| Bishop safety against g4/h4 | [1400–1600, 13:10](https://www.youtube.com/watch?v=0B8A_9sGGbM&t=790s) | Game 64; a later loss |
| Exchange fianchetto and g-file | [1600–1800, 5:00](https://www.youtube.com/watch?v=VEl-6jrdpDA&t=300s) | Game 75 |
| Accelerated Panov recapture | [1600–1800, 1:00:50](https://www.youtube.com/watch?v=VEl-6jrdpDA&t=3650s) | Game 86 |
| Keep tension until exchange helps | [1800–2000, 8:10](https://www.youtube.com/watch?v=qRgmW6SW_b0&t=490s) | Game 89 |
| Qc7 and the Exchange fianchetto | [1800–2000, 12:30](https://www.youtube.com/watch?v=qRgmW6SW_b0&t=750s) | Game 90 |
| Nf6 and gxf6 | [1800–2000, 48:50](https://www.youtube.com/watch?v=qRgmW6SW_b0&t=2930s) | Game 97 |
| Premature Slav bishop development | [2000–2200, 0:20](https://www.youtube.com/watch?v=mKmkrye5lUs&t=20s) | Game 99 |
| Quiet d3 centre | [2000–2200, 15:10](https://www.youtube.com/watch?v=mKmkrye5lUs&t=910s) | Game 102 |
| Classical development | [2000–2200, 20:50](https://www.youtube.com/watch?v=mKmkrye5lUs&t=1250s) | Game 104 |
| Target d4 after development | [2200–2300, 9:30](https://www.youtube.com/watch?v=Y0LtCzfbdwA&t=570s) | Game 113 |
| Nd7 sacrifice and later loss | [2300–2400, 0:20](https://www.youtube.com/watch?v=FmT5SkOnEHE&t=20s) | Game 117 |
| Exchanges against a space advantage | [2300–2400, 18:20](https://www.youtube.com/watch?v=FmT5SkOnEHE&t=1100s) | Game 120 |
| Delayed bishop development | [2400–2600, 4:30](https://www.youtube.com/watch?v=wNuYG9_1uf4&t=270s) | Game 128 |
| Prompt Panov recovery after an experiment | [2400–2600, 42:20](https://www.youtube.com/watch?v=wNuYG9_1uf4&t=2540s) | Game 136 |

## Diagram and study provenance

All 22 diagrams replay an exact mainline prefix of the supplied corpus. [The machine-readable position manifest](eric-caro-kann-positions.json) records source game, ply, FEN, arrows, captions, and study comments. [The renderer](../scripts/render_eric_caro_kann_diagrams.py) asserts that replayed FENs match the manifest, then produces both the SVGs and study PGN. Alternative moves in that PGN are labelled editorial analysis or played continuations. No synthetic position is presented as a video frame.

## Complete supplied-game index

The source opening names are copied from `Event` and may be coarse; move sequences, not the labels, control the guide. All players listed here are White; Black is `PoojaFan69`. Black ratings and results are retained as supplied. Links marked “about” have not been independently checked against video frames.

| Game | White | Black Elo | Result | Supplied opening label | Video provenance |
| --- | --- | --- | --- | --- | --- |
| <a id="game-001"></a>1 | SneaksXO | 436 | 0-1 | Caro-Kann Defense: Advance Botvinnik Carls Defense 4.dxc5 e6 | [about 1:00](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=60s) |
| <a id="game-002"></a>2 | KavisNotTaken | 455 | 0-1 | Caro-Kann Defense | [about 7:00](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=420s) |
| <a id="game-003"></a>3 | VVD_Clix | 484 | 0-1 | Caro-Kann Defense | [about 11:00](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=660s) |
| <a id="game-004"></a>4 | Knight_to-H3 | 498 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.c3 Bf5 | [about 16:30](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=990s) |
| <a id="game-005"></a>5 | isupportok | 523 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 3.d3 | [about 21:40](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1300s) |
| <a id="game-006"></a>6 | Antonyyj | 546 | 0-1 | Caro-Kann Defense | [about 28:10](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1690s) |
| <a id="game-007"></a>7 | crackermain | 570 | 0-1 | Caro-Kann Defense: Two Knights Mindeno Exchange Line 5.Qxf3 e6 | [about 33:30](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2010s) |
| <a id="game-008"></a>8 | lillisio | 593 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 3.d3 | [about 36:50](https://www.youtube.com/watch?v=rCZrddCQWY8&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2210s) |
| <a id="game-009"></a>9 | johntunny | 618 | 0-1 | Caro-Kann Defense...3.d3: dxe4 4.dxe4 Qxd1 5.Kxd1 | [about 0:20](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-010"></a>10 | M8Gaming | 638 | 0-1 | Caro-Kann Defense: 2.f4 d5 | [about 5:10](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=310s) |
| <a id="game-011"></a>11 | lmaothisfun | 655 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 | [about 9:00](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=540s) |
| <a id="game-012"></a>12 | hahGOTEEM | 670 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 | [about 11:50](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=710s) |
| <a id="game-013"></a>13 | JlmmyVaImer | 687 | 0-1 | Polish Opening: Outflank Variation 2.Bb2 | [about 17:00](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1020s) |
| <a id="game-014"></a>14 | serki_77 | 697 | 0-1 | Caro-Kann Defense | [about 22:20](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1340s) |
| <a id="game-015"></a>15 | hinileb | 724 | 0-1 | Queens Pawn Opening: Chigorin Variation 2...c6 | [about 28:30](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1710s) |
| <a id="game-016"></a>16 | sid1270 | 749 | 0-1 | Caro-Kann Defense: Advance Short Variation with 4 Nf3...e6 | [about 34:50](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2090s) |
| <a id="game-017"></a>17 | QueenMaeve0020 | 763 | 0-1 | Caro-Kann Defense: Two Knights Mindeno Retreat Line 5.exd5 cxd5 6.g4 Bg6 | [about 41:00](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2460s) |
| <a id="game-018"></a>18 | Azamatik_zxc1000-7 | 779 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 | [about 46:20](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2780s) |
| <a id="game-019"></a>19 | arad192 | 786 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 | [about 49:50](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2990s) |
| <a id="game-020"></a>20 | arsen265 | 801 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 | [about 56:00](https://www.youtube.com/watch?v=YDUfNGkU3GA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3360s) |
| <a id="game-021"></a>21 | josex2 | 837 | 0-1 | Caro-Kann Defense | [about 0:20](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-022"></a>22 | br0g123 | 844 | 0-1 | Caro-Kann Defense | [about 4:30](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=270s) |
| <a id="game-023"></a>23 | NamChickenn | 851 | 0-1 | Caro-Kann Defense: Two Knights Mindeno Retreat Line 5.exd5 cxd5 6.Bb5 Nc6 | [about 10:00](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=600s) |
| <a id="game-024"></a>24 | MoneaManuelBrendon | 878 | 0-1 | Nimzowitsch-Larsen Attack: Classical Variation 2.Bb2 c6 | [about 16:10](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=970s) |
| <a id="game-025"></a>25 | VladislavTotev | 891 | 0-1 | Caro-Kann Defense: Advance Botvinnik Carls Defense | [about 19:50](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1190s) |
| <a id="game-026"></a>26 | Wamsetha | 900 | 0-1 | Nimzowitsch-Larsen Attack: Classical Variation 2.Bb2 c6 | [about 26:10](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1570s) |
| <a id="game-027"></a>27 | Kayaba2496 | 932 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 | [about 31:20](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1880s) |
| <a id="game-028"></a>28 | mentallychallenged4 | 948 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 | [about 36:10](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2170s) |
| <a id="game-029"></a>29 | Sarrouf | 962 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 | [about 41:40](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2500s) |
| <a id="game-030"></a>30 | jhowton94 | 987 | 0-1 | Queens Pawn Opening: Accelerated London System 2...c6 3.e3 Bf5 | [about 47:40](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2860s) |
| <a id="game-031"></a>31 | proverma | 994 | 0-1 | Caro-Kann Defense: Advance Variation 3...Bf5 | [about 52:30](https://www.youtube.com/watch?v=tyFiLrOpKYg&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3150s) |
| <a id="game-032"></a>32 | Koooooooooodie | 1018 | 0-1 | English Opening: Caro-Kann Defensive System 2.g3 d5 | [about 0:20](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-033"></a>33 | LilPawnNamesJoe | 1034 | 0-1 | Caro-Kann Defense: Fantasy Variation 3...e6 | [about 6:20](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=380s) |
| <a id="game-034"></a>34 | Factfullness | 1041 | 0-1 | Caro-Kann Defense | [about 9:50](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=590s) |
| <a id="game-035"></a>35 | Peruser | 1050 | 0-1 | Nimzowitsch-Larsen Attack: Classical Variation 2.Bb2 c6 | [about 15:40](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=940s) |
| <a id="game-036"></a>36 | murkush20 | 1073 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.c3 Bf5 | [about 20:50](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1250s) |
| <a id="game-037"></a>37 | eescamilla07 | 1080 | 0-1 | Slav Defense: Exchange Variation 3...cxd5 | [about 26:10](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1570s) |
| <a id="game-038"></a>38 | yungvirgin3 | 1088 | 0-1 | Caro-Kann Defense: Two Knights Mindeno Variation 4.Be2 e6 | [about 30:00](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1800s) |
| <a id="game-039"></a>39 | LegendaryyPred | 1131 | 0-1 | Slav Defense: 3.e3 Nf6 4.Nc3 | [about 33:50](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2030s) |
| <a id="game-040"></a>40 | elliottgr | 1139 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 | [about 40:20](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2420s) |
| <a id="game-041"></a>41 | SNchilly | 1147 | 0-1 | Caro-Kann Defense: Advance Variation...4.c4 e6 5.Nc3 Ne7 | [about 46:00](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2760s) |
| <a id="game-042"></a>42 | andreplcoelho | 1170 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 4.Nf3 Nc6 | [about 51:00](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3060s) |
| <a id="game-043"></a>43 | MasterJ007 | 1178 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.e3 Bg4 | [about 55:50](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3350s) |
| <a id="game-044"></a>44 | kmies | 1193 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.e3 Bg4 | [about 60:30](https://www.youtube.com/watch?v=-Gp7ZDRtDKo&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3630s) |
| <a id="game-045"></a>45 | neurofor50 | 1225 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.e3 Bg4 | [about 0:10](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=10s) |
| <a id="game-046"></a>46 | DVDV28 | 1235 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.Bf4 Bf5 4.e3 | [about 4:10](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=250s) |
| <a id="game-047"></a>47 | Hanif777 | 1242 | 0-1 | Caro-Kann Defense | [about 8:40](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=520s) |
| <a id="game-048"></a>48 | merogon | 1265 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 | [about 11:50](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=710s) |
| <a id="game-049"></a>49 | cdhagen | 1279 | 0-1 | Kings-Indian Attack...3.Bg2: Bf5 4.O O e6 | [about 17:10](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1030s) |
| <a id="game-050"></a>50 | jwatts0723 | 1287 | 0-1 | Queens Pawn Opening: Accelerated London System 2...c6 3.e3 Bf5 | [about 21:00](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1260s) |
| <a id="game-051"></a>51 | fedevali | 1316 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 | [about 26:20](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1580s) |
| <a id="game-052"></a>52 | yobo12 | 1324 | 0-1 | Caro-Kann Defense | [about 32:30](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1950s) |
| <a id="game-053"></a>53 | Arzach86 | 1340 | 0-1 | Queens Gambit: Declined Exchange Positional Line...6.Nf3 Bf5 7.e3 Nbd7 | [about 39:30](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2370s) |
| <a id="game-054"></a>54 | killer_wails | 1356 | 0-1 | Caro-Kann Defense: Two Knights Mindeno Variation 4.Be2 e6 | [about 44:50](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2690s) |
| <a id="game-055"></a>55 | Tom_Hack | 1364 | 0-1 | Caro-Kann Defense: Advance Tal Variation 4...h6 | [about 49:40](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2980s) |
| <a id="game-056"></a>56 | Ollie1027 | 1372 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 4.Nf3 Nc6 5.c3 | [about 53:20](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3200s) |
| <a id="game-057"></a>57 | yerke2020 | 1382 | 0-1 | Caro-Kann Defense: Advance Botvinnik Carls Defense 4.c4 cxd4 | [about 58:40](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3520s) |
| <a id="game-058"></a>58 | MagnusJansohn | 1390 | 0-1 | Caro-Kann Defense: Advance Short Variation with 4 Nf3...e6 | [about 62:20](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3740s) |
| <a id="game-059"></a>59 | Tavareshu3 | 1407 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 | [about 63:50](https://www.youtube.com/watch?v=HI0Q1obUbXA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3830s) |
| <a id="game-060"></a>60 | latuya007 | 1429 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 3.d3 | [about 0:30](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=30s) |
| <a id="game-061"></a>61 | MyStewBetter | 1436 | 0-1 | Caro-Kann Defense: 2.f4 d5 | [about 6:30](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=390s) |
| <a id="game-062"></a>62 | diegosilvago3 | 1443 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 | [about 9:20](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=560s) |
| <a id="game-063"></a>63 | CryanBarey | 1458 | 0-1 | Caro-Kann Defense: Advance Variation 3...Bf5 | [about 10:30](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=630s) |
| <a id="game-064"></a>64 | Jetsurgeon | 1474 | 1-0 | Caro-Kann Defense: Advance Bayonet Attack 4...Be4 | [about 13:10](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=790s) |
| <a id="game-065"></a>65 | TheVoodooMaster | 1482 | 0-1 | Richter-Veresov Attack: Richter Variation 4...c6 | [about 19:40](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1180s) |
| <a id="game-066"></a>66 | skott2400 | 1504 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 | [about 23:20](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1400s) |
| <a id="game-067"></a>67 | ooar | 1510 | 0-1 | Queens Pawn Opening: Accelerated London System 2...Nf6 3.e3 c6 | [about 27:30](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1650s) |
| <a id="game-068"></a>68 | Neinkein | 1524 | 0-1 | Slav Defense: 3.Nc3 dxc4 4.a4 | [about 32:10](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1930s) |
| <a id="game-069"></a>69 | akarnik | 1541 | 0-1 | Queens Pawn Opening: 1...c6 | [about 37:50](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2270s) |
| <a id="game-070"></a>70 | Roberto2234 | 1558 | 0-1 | Slav Defense: Modern Line...4.g3 dxc4 5.Bg2 b5 | [about 41:50](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2510s) |
| <a id="game-071"></a>71 | kayroscar | 1565 | 0-1 | Caro-Kann Defense: Exchange Variation...4.Bd3 Nc6 5.Nf3 Bg4 | [about 46:50](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2810s) |
| <a id="game-072"></a>72 | SepeGimbo | 1584 | 0-1 | English Opening: Caro-Kann Defensive System 2.Nc3 d5 | [about 51:30](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3090s) |
| <a id="game-073"></a>73 | KimJongSesentaNueve | 1607 | 0-1 | Slav Defense: Slav Gambit Alekhine Attack 4...b5 | [about 56:40](https://www.youtube.com/watch?v=0B8A_9sGGbM&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3400s) |
| <a id="game-074"></a>74 | khaicunghia | 1625 | 0-1 | Undefined | [about 0:20](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-075"></a>75 | novalife | 1633 | 0-1 | Caro-Kann Defense: Exchange Variation...7.Nf3 Bg7 8.O O-O-O | [about 5:00](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=300s) |
| <a id="game-076"></a>76 | txusnibal82 | 1647 | 0-1 | Caro-Kann Defense: 2.f4 d5 3.e5 | [about 10:40](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=640s) |
| <a id="game-077"></a>77 | MGZVU1 | 1654 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 4.Nf3 Nc6 | [about 16:40](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1000s) |
| <a id="game-078"></a>78 | KaricHasan | 1668 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.g3 Bf5 4.Bg2 | [about 21:00](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1260s) |
| <a id="game-079"></a>79 | DenisMNE | 1699 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 | [about 26:20](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1580s) |
| <a id="game-080"></a>80 | peterlangers | 1706 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.e3 Bg4 | [about 29:20](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1760s) |
| <a id="game-081"></a>81 | Julian_Ibarra | 1729 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.e3 Bf5 4.Bd3 | [about 34:50](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2090s) |
| <a id="game-082"></a>82 | jordan_echecs | 1737 | 0-1 | Caro-Kann Defense: Accelerated Panov Attack...4.cxd5 Qxd5 5.Nc3 Qd8 | [about 40:30](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2430s) |
| <a id="game-083"></a>83 | routin3 | 1743 | 0-1 | Queens Pawn Opening: Zukertort Variation...3.Bf4 Bf5 4.e3 e6 | [about 44:50](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2690s) |
| <a id="game-084"></a>84 | A_River_There_Chief | 1775 | 0-1 | Caro-Kann Defense: Advance Short Variation with 4 Nf3...e6 | [about 50:30](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3030s) |
| <a id="game-085"></a>85 | kostkajedrez | 1783 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 4.Nf3 Nc6 | [about 55:20](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3320s) |
| <a id="game-086"></a>86 | startalready | 1801 | 0-1 | Caro-Kann Defense: Panov Attack...9.O O-O-O 10.Re1 Bf6 | [about 60:50](https://www.youtube.com/watch?v=VEl-6jrdpDA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3650s) |
| <a id="game-087"></a>87 | x-7064262838 | 1816 | 0-1 | Dutch Defense: Classical Rubinstein Variation...4.g3 d5 5.Bg2 c6 | [about 0:10](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=10s) |
| <a id="game-088"></a>88 | ThinkChess0-inactive1 | 1830 | 0-1 | Caro-Kann Defense: 2.Nf3 d5 | [about 3:00](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=180s) |
| <a id="game-089"></a>89 | kip1981 | 1838 | 0-1 | Caro-Kann Defense: Advance Botvinnik Carls Defense 4.c3 Nc6 5.Nf3 Bg4 | [about 8:10](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=490s) |
| <a id="game-090"></a>90 | Arman_Amrenov | 1847 | 0-1 | Caro-Kann Defense: Exchange Variation...6.h3 Nf6 7.Nf3 g6 8.O O | [about 12:30](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=750s) |
| <a id="game-091"></a>91 | steppm | 1877 | 0-1 | Caro-Kann Defense: Exchange Variation...6.Nf3 Bg4 7.O O e6 | [about 19:00](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1140s) |
| <a id="game-092"></a>92 | markgauci93 | 1900 | 0-1 | Queens Pawn Opening: Accelerated London System 2...c6 3.e3 Bf5 | [about 22:30](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1350s) |
| <a id="game-093"></a>93 | yeebruh21 | 1917 | 0-1 | Semi-Slav Defense: Main Line Normal Variation 6.b3 Bb4 | [about 30:40](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1840s) |
| <a id="game-094"></a>94 | Sfeldmanmd | 1927 | 0-1 | Slav Defense: Exchange Variation 3...cxd5 4.Nf3 Nc6 | [about 35:00](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2100s) |
| <a id="game-095"></a>95 | chubbychessguy2000 | 1932 | 0-1 | Caro-Kann Defense: Exchange Variation 3...cxd5 4.Nf3 Nc6 | [about 40:00](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2400s) |
| <a id="game-096"></a>96 | usl1986 | 1949 | 0-1 | Nimzowitsch-Larsen Attack: Classical Variation 2.Bb2 c6 | [about 46:20](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2780s) |
| <a id="game-097"></a>97 | wilmer28 | 1986 | 0-1 | Caro-Kann Defense: Bronstein Larsen Variation | [about 48:50](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2930s) |
| <a id="game-098"></a>98 | voellig_schwerelos | 2002 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 | [about 52:10](https://www.youtube.com/watch?v=qRgmW6SW_b0&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3130s) |
| <a id="game-099"></a>99 | ezevallos | 2011 | 0-1 | Slav Defense: 3.e3 Nf6 4.Nc3 | [about 0:20](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-100"></a>100 | SeaofAse16 | 2019 | 0-1 | English Opening: Caro-Kann Defensive System...4.cxd5 cxd5 5.Nf3 Nc6 | [about 6:00](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=360s) |
| <a id="game-101"></a>101 | EricJ2005 | 2044 | 0-1 | Caro-Kann Defense: Advance Tal Variation 4...h6 | [about 10:10](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=610s) |
| <a id="game-102"></a>102 | Junttaone | 2072 | 0-1 | Caro-Kann Defense: Breyer Variation...6.Bg2 O-O 7.O O Re8 8.Re1 | [about 15:10](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=910s) |
| <a id="game-103"></a>103 | mb8586 | 2080 | 0-1 | Slav Defense: Modern Line...6.Nc3 Be7 7.e3 O-O | [about 18:00](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1080s) |
| <a id="game-104"></a>104 | sahilkuril | 2096 | 0-1 | Caro-Kann Defense: Classical Spassky Variation...9.Bd3 Bxd3 10.Qxd3 e6 | [about 20:50](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1250s) |
| <a id="game-105"></a>105 | djambito | 2104 | 0-1 | Queens Pawn Opening: 1...c6 | [about 23:40](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1420s) |
| <a id="game-106"></a>106 | eniac210 | 2111 | 0-1 | Queens Gambit: Declined Queens Knight Variation...4.Nf3 Nf6 5.Bg5 c6 | [about 27:20](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1640s) |
| <a id="game-107"></a>107 | jpuczai | 2147 | 0-1 | Caro-Kann Defense: Karpov Variation | [about 34:30](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2070s) |
| <a id="game-108"></a>108 | global500 | 2162 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 | [about 41:00](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2460s) |
| <a id="game-109"></a>109 | Armanchois123 | 2170 | 0-1 | Slav Defense: Slav Gambit Alekhine Attack 4...b5 | [about 46:40](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2800s) |
| <a id="game-110"></a>110 | KGV11 | 2202 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 | [about 49:30](https://www.youtube.com/watch?v=mKmkrye5lUs&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2970s) |
| <a id="game-111"></a>111 | Bajkeee | 2210 | 0-1 | Slav Defense: Slav Gambit Alekhine Attack | [about 0:20](https://www.youtube.com/watch?v=Y0LtCzfbdwA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-112"></a>112 | Asztrik | 2219 | 0-1 | Caro-Kann Defense: Modern Variation 3...g6 4.Ngf3 Bg7 5.c3 | [about 5:30](https://www.youtube.com/watch?v=Y0LtCzfbdwA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=330s) |
| <a id="game-113"></a>113 | kristianmsc | 2253 | 0-1 | Caro-Kann Defense: Advance Variation...4.c4 e6 5.Nc3 Ne7 | [about 8:50](https://www.youtube.com/watch?v=Y0LtCzfbdwA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=530s) |
| <a id="game-114"></a>114 | rostokas | 2261 | 0-1 | Polish Opening: Outflank Variation 2.Bb2 | [about 13:20](https://www.youtube.com/watch?v=Y0LtCzfbdwA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=800s) |
| <a id="game-115"></a>115 | ChessDestroyer2026 | 2268 | 0-1 | Slav Defense: Modern Quiet Variation...6.Nbd2 e6 7.Qc2 Nbd7 8.b3 | [about 18:50](https://www.youtube.com/watch?v=Y0LtCzfbdwA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1130s) |
| <a id="game-116"></a>116 | the_blue_pill | 2301 | 0-1 | Caro-Kann Defense: Advance Variation...5.Nb3 Nd7 6.Nf3 a6 | [about 26:00](https://www.youtube.com/watch?v=Y0LtCzfbdwA&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1560s) |
| <a id="game-117"></a>117 | AttackFirstThinkLater | 2292 | 1-0 | Caro-Kann Defense: Karpov Variation...6.Bd3 e6 7.N1f3 Bd6 | [about 0:20](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=20s) |
| <a id="game-118"></a>118 | hidey32 | 2307 | 0-1 | Slav Defense: Modern Line 3...Nf6 4.g3 dxc4 5.Bg2 | [about 7:20](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=440s) |
| <a id="game-119"></a>119 | simonbr | 2329 | 0-1 | Caro-Kann Defense: Breyer Variation...6.Bg2 O-O 7.O O Re8 | [about 13:40](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=820s) |
| <a id="game-120"></a>120 | exterminator444 | 2325 | 1-0 | Caro-Kann Defense: Advance Van der Wiel Attack 4...e6 5.g4 Bg6 6.Nge2 | [about 17:20](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1040s) |
| <a id="game-121"></a>121 | lhavas | 2337 | 0-1 | Caro-Kann Defense: Advance Bronstein Variation...7.h5 Bh7 8.Bd3 Bxd3 | [about 23:20](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1400s) |
| <a id="game-122"></a>122 | RobRam | 2359 | 0-1 | Kings-Indian Attack: Yugoslav Variation...6.b3 e6 7.Bb2 Be7 8.Nbd2 | [about 27:50](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1670s) |
| <a id="game-123"></a>123 | Strong_dragon | 2375 | 0-1 | Caro-Kann Defense: Advance Botvinnik Carls Defense 4.c3 Nc6 5.Nf3 | [about 35:00](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2100s) |
| <a id="game-124"></a>124 | 1italianiluca | 2389 | 0-1 | Slav Defense: Exchange Variation...6.e3 a6 7.Bd3 Bg4 8.f3 | [about 37:50](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2270s) |
| <a id="game-125"></a>125 | kaznelra | 2383 | 1-0 | Caro-Kann Defense: Karpov Variation...7.Bc4 Bf5 8.O O e6 | [about 43:40](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2620s) |
| <a id="game-126"></a>126 | JustAnotherPepega | 2392 | 0-1 | Caro-Kann Defense: Advance Short Variation with 4 Nf3...e6 5.Be2 h6 6.O O | [about 50:30](https://www.youtube.com/watch?v=FmT5SkOnEHE&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3030s) |
| <a id="game-127"></a>127 | Hollywood_Chess | 2408 | 0-1 | English Opening: Caro-Kann Defensive System...4.Nc3 e6 5.b3 Bd6 6.Bb2 | Supplier: off camera; captions suggest partially shown (see correction above) |
| <a id="game-128"></a>128 | vahid_ka65 | 2435 | 0-1 | Caro-Kann Defense: Karpov Kasparov Attack 6...e6 7.Bd3 | [about 4:30](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=270s) |
| <a id="game-129"></a>129 | brt6209 | 2451 | 0-1 | Caro-Kann Defense...3.e5: c5 4.d4 Nc6 5.c3 | [about 7:40](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=460s) |
| <a id="game-130"></a>130 | misterlamine | 2467 | 0-1 | Queens Pawn Opening: Zukertort Variation 2...c6 3.g3 Bf5 4.Bg2 | [about 12:50](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=770s) |
| <a id="game-131"></a>131 | Owenov | 2472 | 0-1 | Caro-Kann Defense: 2.Nc3 d5 3.d3 dxe4 | [about 19:40](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1180s) |
| <a id="game-132"></a>132 | AlexeiiRamirov | 2478 | 0-1 | Slav Defense: Exchange Variation...7.Rc1 Bf5 8.Nf3 Rc8 | [about 22:00](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1320s) |
| <a id="game-133"></a>133 | jeecon20 | 2496 | 0-1 | Slav Defense: Modern Quiet Schallopp Defense 5.Nc3 e6 | [about 26:40](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=1600s) |
| <a id="game-134"></a>134 | elmismoxd | 2533 | 0-1 | Caro-Kann Defense: Accelerated Panov Modern Variation 5.Nc3 g6 6.Bc4 Bg7 | [about 33:20](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2000s) |
| <a id="game-135"></a>135 | Dmitry_Gritsenko | 2547 | 0-1 | Caro-Kann Defense...3.Qe2: d4 4.Nd1 e5 | [about 39:50](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2390s) |
| <a id="game-136"></a>136 | vegan4animals | 2552 | 0-1 | Caro-Kann Defense: Panov Attack...8.Bc4 Nc6 9.O O-O-O 10.Re1 | [about 42:20](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2540s) |
| <a id="game-137"></a>137 | Lasierra78 | 2557 | 0-1 | Queens Gambit: Accepted Mannheim Variation...8.O O Be7 9.e3 O-O 10.Qe2 | [about 46:50](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=2810s) |
| <a id="game-138"></a>138 | Aemulus20 | 2571 | 0-1 | Caro-Kann Defense: Classical Spassky Variation...10.Qxd3 e6 11.Bd2 Ngf6 12.O O-O | [about 50:20](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3020s) |
| <a id="game-139"></a>139 | Turkish-Lion | 2576 | 0-1 | Slav Defense: Modern Quiet Schallopp Defense...6.Qb3 Qb6 7.c5 Qc7 | [about 53:00](https://www.youtube.com/watch?v=wNuYG9_1uf4&list=PLUjxDD7HNNTjVEZ_1I8E28uav9t_ltDKX&t=3180s) |
| <a id="game-140"></a>140 | Swordoftheword16 | 2609 | 0-1 | Caro-Kann Defense: Advance Tal Variation...5.g4 Bd7 6.h5 e6 | Supplier: beyond video endpoint; no episode link |
| <a id="game-141"></a>141 | Ajedrez_con_German | 2608 | 0-1 | Slav Defense: Modern Quiet Schallopp Defense...6.Bd3 Bg6 7.O O Nbd7 | Supplier: beyond video endpoint; no episode link |
| <a id="game-142"></a>142 | Nxh6 | 2605 | 1-0 | Caro-Kann Defense: Panov Attack...8.Bc4 Nc6 9.O O-O-O | Supplier: beyond video endpoint; no episode link |
| <a id="game-143"></a>143 | JogadorMedio | 2617 | 0-1 | Queens Pawn Opening: Pseudo Catalan Variation...8.Nd2 Be7 9.e4 dxe4 10.Ndxe4 | Supplier: beyond video endpoint; no episode link |
| <a id="game-144"></a>144 | nacer1989 | 2608 | 1-0 | Caro-Kann Defense: Fantasy Variation 3...Qb6 4.Nc3 | Supplier: beyond video endpoint; no episode link |
| <a id="game-145"></a>145 | ShaakSiv | 2614 | 0-1 | Semi-Slav Defense: Main Line Stoltz Variation...9.Bb2 Bb7 10.O O Qe7 11.Rad1 | Supplier: beyond video endpoint; no episode link |
| <a id="game-146"></a>146 | kiCaps | 2603 | 1-0 | Caro-Kann Defense: Classical Variation...9.Qxd3 e6 10.Bd2 Ngf6 11.O O-O | Supplier: beyond video endpoint; no episode link |
| <a id="game-147"></a>147 | subham777 | 2615 | 0-1 | Queens Gambit: Declined Semi-Tarrasch Main Line Pillsbury Variation...8.exd4 Be7 9.O O-O-O 10.Re1 | Supplier: beyond video endpoint; no episode link |
| <a id="game-148"></a>148 | xdwxdwxdw | 2621 | 0-1 | Queens Pawn Opening: Zukertort Variation...3.Bf4 Bf5 4.e3 e6 | Supplier: beyond video endpoint; no episode link |
