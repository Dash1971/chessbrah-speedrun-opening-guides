# Aman Hambleton's London System — sources and recovered game index

[Guide](../guides/london-system.md) · [130 recovered game scores](../pgn/london-system-games.pgn) · [22 annotated excerpts](../pgn/london-system-repertoire.pgn) · [Validation and Stockfish findings](london-system-validation.md)

## Primary series and account identity

- Teacher: **GM Aman Hambleton**, Chessbrah.
- Official channel playlist: [London System Series](https://www.youtube.com/playlist?list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx), 18 videos, from Part 1 through FINALE.
- The [introduction, Part 1 at 0:16](https://www.youtube.com/watch?v=3bULUDwHYtc&t=16s) starts the run around 800 and explains that the edited series shows White's games. Aman also identifies the historical handle in [Part 15 at 10:10](https://www.youtube.com/watch?v=MHqTZWomK6A&t=610s).
- The video handle is **systemplayer**. The historical account is now **[systematic](https://www.chess.com/member/systematic)**, Chess.com player ID **188452309**, joined June 29, 2022. The current account called systemplayer was created in 2024 and is not the account in these 2022 videos.
- Identity was traced through the [aziz4ab June 2022 public archive](https://api.chess.com/pub/player/aziz4ab/games/2022/06): its game against systematic has the same opponent, time control, opening moves and subsequent score as the first video. The on-screen pregame ratings differ from the archive's postgame ratings; these are not two different games.
- First match: [systematic–aziz4ab, June 30](https://www.chess.com/game/live/50356815043), opening visible in [Part 1 at 0:55](https://www.youtube.com/watch?v=3bULUDwHYtc&t=55s).
- Last match: [systematic–fidemax, August 18](https://www.chess.com/game/live/54591542165), visible near the end of the [FINALE](https://www.youtube.com/watch?v=Zkcyyj9xTT8&t=4899s). The archive records White at 2498 after this game; do not turn the series' round-number target into a claim of a 2500 postgame rating.

## Retrieval and scope

Recovered on **2026-11-24** through Chess.com's [read-only Published Data API](https://www.chess.com/news/view/published-data-api), using the account's [June](https://api.chess.com/pub/player/systematic/games/2022/06), [July](https://api.chess.com/pub/player/systematic/games/2022/07) and [August](https://api.chess.com/pub/player/systematic/games/2022/08) archives.

The publication contains **130 standard-chess games with White, all 300-second blitz**, chronologically between the first matched post-reset game and the finale game, inclusive. It excludes **23 earlier White games before the reset**, **47 intervening 60-second bullet games**, all Black games and all 2024 activity. The corpus includes the anti-Englund and anti-Benoni games inside the run; they are labelled as repertoire boundaries in the guide rather than renamed Londons.

The [unchanged Chess.com source export](london-system-original-games.pgn) preserves the original API text and checksum. The main published PGN adds YouTube headers and opening comments while retaining every original header, move, clock annotation and result, including the renamed handle systematic and the Chess.com Link header. Wins, draws and losses are all retained. All 130 games now have a verified sampled point in the edited videos, as described below; these points are not exact game-start markers.

[Machine-readable provenance](london-system-games.json) records the separate source and enriched-corpus hashes, per-game source PGN and move hashes, account ID and selection. [The retrieval script](../scripts/fetch_london_games.py) exports the unchanged source selection; [the enrichment script](../scripts/enrich_london_video_links.py) adds the reviewed video metadata. Both stop if their identity or coverage checks fail.

## Caption coverage and video inventory

All 18 English auto-caption tracks were recovered through their ending. The guide uses selected opening, review and teaching passages across the full playlist; recovery of complete tracks is not a claim of a word-by-word review of every utterance. Auto-captions can confuse chess notation. PGN replay and the actual position take precedence over a phonetic caption.

The initial archive-window assignments used sampled boundary opponents; Parts 5 and 14 initially relied on adjoining boundaries and captions. The video-link follow-up has now sampled full-resolution points for **all 130 games across all 18 videos**, including Parts 5 and 14. Storyboard board-position candidates were checked against displayed opponent labels and the source score; renamed opponents were corroborated by their positions and ratings. One candidate for game 86 was rejected because it showed the preceding game, and a later verified frame was substituted. These checks establish game/review points, not exact starts.

| Part | Video | Uploaded | Duration | Caption segments | Archive game window |
| --- | --- | --- | --- | --- | --- |
| 1 | [Grandmaster Teaches The London System | Part 1](https://www.youtube.com/watch?v=3bULUDwHYtc) | 2022-08-06 | 49:40 | 1119 | 1–6 |
| 2 | [Grandmaster Teaches The London System | Part 2](https://www.youtube.com/watch?v=pkOkSGuQvh8) | 2022-08-10 | 28:20 | 622 | 7–11 |
| 3 | [Grandmaster Teaches The London System | Part 3](https://www.youtube.com/watch?v=OidsHHg6Nm0) | 2022-08-16 | 49:55 | 829 | 12–17 |
| 4 | [Grandmaster Teaches The London System | Part 4](https://www.youtube.com/watch?v=rwsumP3aq_I) | 2022-08-20 | 56:28 | 1126 | 18–24 |
| 5 | [Grandmaster Teaches The London System | Part 5](https://www.youtube.com/watch?v=0hlDcA0Zc9M) | 2022-08-29 | 1:15:53 | 1221 | 25–32 |
| 6 | [Grandmaster Teaches The London System | Part 6](https://www.youtube.com/watch?v=PqFwbmSvm38) | 2022-09-17 | 1:05:03 | 1095 | 33–40 |
| 7 | [Grandmaster Teaches The London System | Part 7](https://www.youtube.com/watch?v=-guvn4tkgmU) | 2022-10-04 | 37:35 | 547 | 41–46 |
| 8 | [Grandmaster Teaches The London System | Part 8](https://www.youtube.com/watch?v=5iqm-aq7sEA) | 2022-10-10 | 51:22 | 588 | 47–53 |
| 9 | [Grandmaster Teaches The London System | Part 9](https://www.youtube.com/watch?v=rfbOu4mA-hQ) | 2022-10-20 | 46:51 | 657 | 54–58 |
| 10 | [Grandmaster Teaches The London System | Part 10](https://www.youtube.com/watch?v=NtcXbhKBWwI) | 2022-10-27 | 38:53 | 665 | 59–65 |
| 11 | [Grandmaster Teaches The London System | Part 11](https://www.youtube.com/watch?v=vyxK0vqxowo) | 2022-11-02 | 1:08:06 | 1004 | 66–72 |
| 12 | [Grandmaster Teaches The London System | Part 12](https://www.youtube.com/watch?v=EOfNcvkpQp8) | 2022-11-11 | 57:20 | 699 | 73–79 |
| 13 | [Grandmaster Teaches The London System | Part 13](https://www.youtube.com/watch?v=izNk3Dd4zZA) | 2022-11-21 | 56:18 | 595 | 80–86 |
| 14 | [Grandmaster Teaches The London System | Part 14](https://www.youtube.com/watch?v=3PohHinhSHY) | 2022-11-28 | 1:16:46 | 1178 | 87–95 |
| 15 | [Grandmaster Teaches The London System | Part 15](https://www.youtube.com/watch?v=MHqTZWomK6A) | 2022-12-06 | 1:27:00 | 1205 | 96–105 |
| 16 | [Grandmaster Teaches The London System | Part 16](https://www.youtube.com/watch?v=klPQ8hPGCnU) | 2022-12-17 | 1:39:10 | 1370 | 106–116 |
| 17 | [Grandmaster Teaches The London System | Part 17](https://www.youtube.com/watch?v=qm5t3xAdJMk) | 2022-12-23 | 55:36 | 839 | 117–121 |
| 18 | [Grandmaster Teaches The London System | FINALE](https://www.youtube.com/watch?v=Zkcyyj9xTT8) | 2022-12-27 | 1:23:19 | 1074 | 122–130 |

Total: **16,433 caption segments**, approximately **18.06 hours** of published video. Caption ending times can exceed the video metadata duration by a second or two because of segment timing.

## YouTube links inside both PGNs

All **130 complete games** and **22 study excerpts** now carry `YouTubeEpisode`, `YouTubeURL`, `YouTubeEpisodeURL`, `YouTubeTimestamp`, `YouTubeLinkType` and `LinkPrecision` headers. Their opening comments also contain the URL so the link remains visible in readers that hide custom tags. The excerpts inherit their source game's video reference.

The precision label is **`game-point`**, with link type **`play-or-review`**: the timestamp points to a verified sampled moment within that game's play or review. It is **not an exact game-start marker, an exact chapter start, or automatically the teaching moment for the excerpt's theme**. The in-guide teaching links below are separate references.

[The video-link manifest](london-system-video-links.json) lists all 130 checked points. The unchanged original source PGN is retained separately; metadata enrichment does not change the game scores, clocks, results or original player headers. Video frames and captions remain local working evidence and are not redistributed.

## Teaching references used in the guide

These links locate caption passages, not independently measured game-start times.

| Part | Passage | Teaching focus |
| --- | --- | --- |
| 1 | [10:00](https://www.youtube.com/watch?v=3bULUDwHYtc&t=600s), [12:52](https://www.youtube.com/watch?v=3bULUDwHYtc&t=772s) | Queen still watching h5; c4 against early ...Bf5 |
| 2 | [0:51](https://www.youtube.com/watch?v=pkOkSGuQvh8&t=51s), [6:39](https://www.youtube.com/watch?v=pkOkSGuQvh8&t=399s) | c4/Nc3 without central tension; Be2 against ...e5-e4 |
| 3 | [17:49](https://www.youtube.com/watch?v=OidsHHg6Nm0&t=1069s), [20:42](https://www.youtube.com/watch?v=OidsHHg6Nm0&t=1242s) | Recapture changes after c4; ...Nc6 as a cue for more space |
| 4 | [16:25](https://www.youtube.com/watch?v=rwsumP3aq_I&t=985s), [54:59](https://www.youtube.com/watch?v=rwsumP3aq_I&t=3299s) | Early ...Qb6 is awkward; exceptions against ...c5 and ...e5 |
| 5 | [1:12](https://www.youtube.com/watch?v=0hlDcA0Zc9M&t=72s), [35:18](https://www.youtube.com/watch?v=0hlDcA0Zc9M&t=2118s) | c3 and queenside development against ...c5; simple anti-Englund plan |
| 6 | [3:38](https://www.youtube.com/watch?v=PqFwbmSvm38&t=218s), [6:25](https://www.youtube.com/watch?v=PqFwbmSvm38&t=385s) | Why routine c3 can be passive; ...Qc8 versus ...Qb6 |
| 7 | [0:46](https://www.youtube.com/watch?v=-guvn4tkgmU&t=46s), [8:04](https://www.youtube.com/watch?v=-guvn4tkgmU&t=484s) | exf4 is conditional on the c-pawn; coordinated development |
| 8 | [4:02](https://www.youtube.com/watch?v=5iqm-aq7sEA&t=242s), [24:07](https://www.youtube.com/watch?v=5iqm-aq7sEA&t=1447s) | Central expansion against symmetry; queenside pressure |
| 9 | [15:38](https://www.youtube.com/watch?v=rfbOu4mA-hQ&t=938s), [25:01](https://www.youtube.com/watch?v=rfbOu4mA-hQ&t=1501s) | Be2 and a bishop shelter; delay the c-pawn when Black retains options |
| 10 | [6:43](https://www.youtube.com/watch?v=NtcXbhKBWwI&t=403s), [12:20](https://www.youtube.com/watch?v=NtcXbhKBWwI&t=740s) | Nc3 versus ...d5/...g6; shelter the bishop against the Dutch |
| 11 | [0:29](https://www.youtube.com/watch?v=vyxK0vqxowo&t=29s), [4:34](https://www.youtube.com/watch?v=vyxK0vqxowo&t=274s) | Decision rules; an attacking example that still ended in a loss |
| 12 | [38:38](https://www.youtube.com/watch?v=EOfNcvkpQp8&t=2318s) | Develop the queenside promptly when ...c5 threatens pressure |
| 13 | [9:38](https://www.youtube.com/watch?v=izNk3Dd4zZA&t=578s), [31:10](https://www.youtube.com/watch?v=izNk3Dd4zZA&t=1870s) | Space against ...d6; converting an attack into extra pawns |
| 14 | [1:11](https://www.youtube.com/watch?v=3PohHinhSHY&t=71s), [33:19](https://www.youtube.com/watch?v=3PohHinhSHY&t=1999s) | Flexible c-pawn; c3 and queenside development against ...c5 |
| 15 | [38:01](https://www.youtube.com/watch?v=MHqTZWomK6A&t=2281s), [1:00:11](https://www.youtube.com/watch?v=MHqTZWomK6A&t=3611s) | Move-order errors still matter; adapting to ...b6 |
| 16 | [0:36](https://www.youtube.com/watch?v=klPQ8hPGCnU&t=36s), [23:26](https://www.youtube.com/watch?v=klPQ8hPGCnU&t=1406s) | Choosing Nc3 or Nd2; Qb1 and exd4 |
| 17 | [1:55](https://www.youtube.com/watch?v=qm5t3xAdJMk&t=115s), [24:31](https://www.youtube.com/watch?v=qm5t3xAdJMk&t=1471s) | Ne5/f4 plans; active responses to bishop-hunting knights |
| 18 | [11:10](https://www.youtube.com/watch?v=Zkcyyj9xTT8&t=670s), [20:40](https://www.youtube.com/watch?v=Zkcyyj9xTT8&t=1240s) | The ...Qxb2 gambit; a correction after ...Ng5 |

## Complete recovered game index

Ratings are preserved as returned by the archive. Game numbers here agree with the guide, manifest, engine records and study excerpts. Each video link is a checked point within the game or review, with precision `game-point`; it is not a game start.

| Game | UTC date | Black | Result | Episode | Video point | Chess.com |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 2022.06.30 | aziz4ab | 1-0 | 1 | [2:10](https://www.youtube.com/watch?v=3bULUDwHYtc&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=130s) | [Game](https://www.chess.com/game/live/50356815043) |
| 2 | 2022.06.30 | Medprince110 | 1-0 | 1 | [13:40](https://www.youtube.com/watch?v=3bULUDwHYtc&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=820s) | [Game](https://www.chess.com/game/live/50357446737) |
| 3 | 2022.06.30 | LaurentiuPatrascu | 1-0 | 1 | [21:10](https://www.youtube.com/watch?v=3bULUDwHYtc&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1270s) | [Game](https://www.chess.com/game/live/50359745849) |
| 4 | 2022.06.30 | Rustamova15 | 1-0 | 1 | [28:10](https://www.youtube.com/watch?v=3bULUDwHYtc&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1690s) | [Game](https://www.chess.com/game/live/50359856813) |
| 5 | 2022.06.30 | w-FarsightedComp | 1-0 | 1 | [38:00](https://www.youtube.com/watch?v=3bULUDwHYtc&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2280s) | [Game](https://www.chess.com/game/live/50360462541) |
| 6 | 2022.06.30 | looser_noob2000 | 1-0 | 1 | [46:50](https://www.youtube.com/watch?v=3bULUDwHYtc&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2810s) | [Game](https://www.chess.com/game/live/50361554577) |
| 7 | 2022.06.30 | Eddiedj | 1-0 | 2 | [3:00](https://www.youtube.com/watch?v=pkOkSGuQvh8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=180s) | [Game](https://www.chess.com/game/live/50363951779) |
| 8 | 2022.06.30 | luisito66666 | 1-0 | 2 | [12:20](https://www.youtube.com/watch?v=pkOkSGuQvh8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=740s) | [Game](https://www.chess.com/game/live/50365144541) |
| 9 | 2022.06.30 | midou212 | 1-0 | 2 | [18:20](https://www.youtube.com/watch?v=pkOkSGuQvh8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1100s) | [Game](https://www.chess.com/game/live/50366947239) |
| 10 | 2022.06.30 | luciano111111111111111111 | 1-0 | 2 | [21:50](https://www.youtube.com/watch?v=pkOkSGuQvh8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1310s) | [Game](https://www.chess.com/game/live/50367004941) |
| 11 | 2022.06.30 | juanzubiri | 1-0 | 2 | [26:50](https://www.youtube.com/watch?v=pkOkSGuQvh8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1610s) | [Game](https://www.chess.com/game/live/50367534285) |
| 12 | 2022.07.06 | BPBOROMIR | 1-0 | 3 | [2:00](https://www.youtube.com/watch?v=OidsHHg6Nm0&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=120s) | [Game](https://www.chess.com/game/live/50804401939) |
| 13 | 2022.07.06 | U2Morris | 1-0 | 3 | [10:50](https://www.youtube.com/watch?v=OidsHHg6Nm0&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=650s) | [Game](https://www.chess.com/game/live/50805520883) |
| 14 | 2022.07.06 | karuppu767 | 1-0 | 3 | [19:50](https://www.youtube.com/watch?v=OidsHHg6Nm0&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1190s) | [Game](https://www.chess.com/game/live/50805601451) |
| 15 | 2022.07.06 | urghhhhhhhhhhh | 1-0 | 3 | [21:40](https://www.youtube.com/watch?v=OidsHHg6Nm0&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1300s) | [Game](https://www.chess.com/game/live/50806202867) |
| 16 | 2022.07.06 | PANCHOTE22 | 1-0 | 3 | [32:10](https://www.youtube.com/watch?v=OidsHHg6Nm0&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1930s) | [Game](https://www.chess.com/game/live/50807388857) |
| 17 | 2022.07.06 | wwwly | 1-0 | 3 | [39:00](https://www.youtube.com/watch?v=OidsHHg6Nm0&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2340s) | [Game](https://www.chess.com/game/live/50808580727) |
| 18 | 2022.07.06 | TulioVAB | 1-0 | 4 | [1:40](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=100s) | [Game](https://www.chess.com/game/live/50810940367) |
| 19 | 2022.07.06 | Yahweh42069 | 1-0 | 4 | [16:50](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1010s) | [Game](https://www.chess.com/game/live/50812746695) |
| 20 | 2022.07.06 | KINGMANUJI | 1-0 | 4 | [20:10](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1210s) | [Game](https://www.chess.com/game/live/50813356935) |
| 21 | 2022.07.06 | QueenJazzyK | 1-0 | 4 | [25:10](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1510s) | [Game](https://www.chess.com/game/live/50813944043) |
| 22 | 2022.07.06 | evil_emil | 1-0 | 4 | [34:00](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2040s) | [Game](https://www.chess.com/game/live/50876998567) |
| 23 | 2022.07.06 | Kelenneth | 1-0 | 4 | [46:10](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2770s) | [Game](https://www.chess.com/game/live/50878220497) |
| 24 | 2022.07.06 | tkenyon | 1-0 | 4 | [51:10](https://www.youtube.com/watch?v=rwsumP3aq_I&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3070s) | [Game](https://www.chess.com/game/live/50879394977) |
| 25 | 2022.07.06 | mblaoc | 1-0 | 5 | [3:10](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=190s) | [Game](https://www.chess.com/game/live/50880602409) |
| 26 | 2022.07.06 | ellwright | 0-1 | 5 | [13:30](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=810s) | [Game](https://www.chess.com/game/live/50881257961) |
| 27 | 2022.07.06 | dkostopoulos | 1-0 | 5 | [27:10](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1630s) | [Game](https://www.chess.com/game/live/50883528457) |
| 28 | 2022.07.06 | timurussi | 1-0 | 5 | [36:10](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2170s) | [Game](https://www.chess.com/game/live/50884176795) |
| 29 | 2022.07.06 | Filab1 | 1-0 | 5 | [45:50](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2750s) | [Game](https://www.chess.com/game/live/50884791729) |
| 30 | 2022.07.06 | jrmalcovich2017 | 1-0 | 5 | [50:50](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3050s) | [Game](https://www.chess.com/game/live/50886017747) |
| 31 | 2022.07.06 | kuzynightmare92 | 1-0 | 5 | [59:30](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3570s) | [Game](https://www.chess.com/game/live/50887155437) |
| 32 | 2022.07.06 | chavan8050 | 1-0 | 5 | [1:07:20](https://www.youtube.com/watch?v=0hlDcA0Zc9M&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4040s) | [Game](https://www.chess.com/game/live/50887759125) |
| 33 | 2022.07.08 | Avikandalib | 1-0 | 6 | [2:20](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=140s) | [Game](https://www.chess.com/game/live/50980202245) |
| 34 | 2022.07.08 | BlindNickIRL | 1-0 | 6 | [16:30](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=990s) | [Game](https://www.chess.com/game/live/50980776803) |
| 35 | 2022.07.08 | blacklisted8 | 1-0 | 6 | [26:10](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1570s) | [Game](https://www.chess.com/game/live/50981434911) |
| 36 | 2022.07.08 | InfiniteApproach72 | 1-0 | 6 | [29:30](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1770s) | [Game](https://www.chess.com/game/live/50984367793) |
| 37 | 2022.07.08 | BlanketsInPigs | 0-1 | 6 | [39:30](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2370s) | [Game](https://www.chess.com/game/live/50985610025) |
| 38 | 2022.07.08 | ramnath246 | 1-0 | 6 | [55:50](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3350s) | [Game](https://www.chess.com/game/live/50986784559) |
| 39 | 2022.07.08 | Mentors4MeCEO | 1-0 | 6 | [57:10](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3430s) | [Game](https://www.chess.com/game/live/50987347609) |
| 40 | 2022.07.08 | yungstarbeams | 1-0 | 6 | [58:40](https://www.youtube.com/watch?v=PqFwbmSvm38&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3520s) | [Game](https://www.chess.com/game/live/50987436027) |
| 41 | 2022.07.08 | blunderdose | 1-0 | 7 | [4:30](https://www.youtube.com/watch?v=-guvn4tkgmU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=270s) | [Game](https://www.chess.com/game/live/51043797301) |
| 42 | 2022.07.08 | clevs1103 | 1-0 | 7 | [7:30](https://www.youtube.com/watch?v=-guvn4tkgmU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=450s) | [Game](https://www.chess.com/game/live/51045627839) |
| 43 | 2022.07.08 | jefflawson | 1-0 | 7 | [17:30](https://www.youtube.com/watch?v=-guvn4tkgmU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1050s) | [Game](https://www.chess.com/game/live/51046781415) |
| 44 | 2022.07.08 | dfamous1 | 1-0 | 7 | [23:10](https://www.youtube.com/watch?v=-guvn4tkgmU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1390s) | [Game](https://www.chess.com/game/live/51047362263) |
| 45 | 2022.07.08 | Famous915 | 1-0 | 7 | [28:20](https://www.youtube.com/watch?v=-guvn4tkgmU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1700s) | [Game](https://www.chess.com/game/live/51047998805) |
| 46 | 2022.07.08 | ThAnt82 | 1-0 | 7 | [31:30](https://www.youtube.com/watch?v=-guvn4tkgmU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1890s) | [Game](https://www.chess.com/game/live/51048035907) |
| 47 | 2022.07.08 | Iusus | 1-0 | 8 | [1:20](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=80s) | [Game](https://www.chess.com/game/live/51049181173) |
| 48 | 2022.07.08 | rollin-nolan206 | 1-0 | 8 | [4:30](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=270s) | [Game](https://www.chess.com/game/live/51050404763) |
| 49 | 2022.07.08 | kokobon | 1-0 | 8 | [13:00](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=780s) | [Game](https://www.chess.com/game/live/51052758003) |
| 50 | 2022.07.08 | GaiaTerra | 1-0 | 8 | [21:40](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1300s) | [Game](https://www.chess.com/game/live/51053476565) |
| 51 | 2022.07.08 | ENOLchess | 1/2-1/2 | 8 | [24:30](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1470s) | [Game](https://www.chess.com/game/live/51053976605) |
| 52 | 2022.07.08 | sudduchess | 1-0 | 8 | [36:30](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2190s) | [Game](https://www.chess.com/game/live/51054618489) |
| 53 | 2022.07.08 | ploose | 1-0 | 8 | [46:30](https://www.youtube.com/watch?v=5iqm-aq7sEA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2790s) | [Game](https://www.chess.com/game/live/51055221461) |
| 54 | 2022.07.10 | crookedrooked | 1-0 | 9 | [1:40](https://www.youtube.com/watch?v=rfbOu4mA-hQ&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=100s) | [Game](https://www.chess.com/game/live/51155387223) |
| 55 | 2022.07.10 | Pippenho | 1-0 | 9 | [10:20](https://www.youtube.com/watch?v=rfbOu4mA-hQ&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=620s) | [Game](https://www.chess.com/game/live/51157212185) |
| 56 | 2022.07.10 | mhallexpantaran | 1-0 | 9 | [18:10](https://www.youtube.com/watch?v=rfbOu4mA-hQ&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1090s) | [Game](https://www.chess.com/game/live/51157789599) |
| 57 | 2022.07.10 | fedebaredes | 1-0 | 9 | [27:50](https://www.youtube.com/watch?v=rfbOu4mA-hQ&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1670s) | [Game](https://www.chess.com/game/live/51158404931) |
| 58 | 2022.07.10 | ChessJob | 1-0 | 9 | [37:10](https://www.youtube.com/watch?v=rfbOu4mA-hQ&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2230s) | [Game](https://www.chess.com/game/live/51158996073) |
| 59 | 2022.07.19 | hsingh69 | 1-0 | 10 | [2:50](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=170s) | [Game](https://www.chess.com/game/live/51996105431) |
| 60 | 2022.07.19 | caioschaves | 1-0 | 10 | [8:10](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=490s) | [Game](https://www.chess.com/game/live/51998959937) |
| 61 | 2022.07.19 | PanzerRui9 | 1-0 | 10 | [11:10](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=670s) | [Game](https://www.chess.com/game/live/51999682499) |
| 62 | 2022.07.19 | Ahirsa1953 | 1-0 | 10 | [14:40](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=880s) | [Game](https://www.chess.com/game/live/52000182985) |
| 63 | 2022.07.19 | Azarnina | 1-0 | 10 | [25:10](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1510s) | [Game](https://www.chess.com/game/live/52000814175) |
| 64 | 2022.07.19 | LoloBolero | 1-0 | 10 | [30:30](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1830s) | [Game](https://www.chess.com/game/live/52001457411) |
| 65 | 2022.07.19 | lucianonachif | 1-0 | 10 | [32:50](https://www.youtube.com/watch?v=NtcXbhKBWwI&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1970s) | [Game](https://www.chess.com/game/live/52001983605) |
| 66 | 2022.07.20 | costalseas | 0-1 | 11 | [3:30](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=210s) | [Game](https://www.chess.com/game/live/52076442787) |
| 67 | 2022.07.20 | tal-vez | 1-0 | 11 | [15:50](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=950s) | [Game](https://www.chess.com/game/live/52078304341) |
| 68 | 2022.07.20 | TomGeKu | 1-0 | 11 | [24:40](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1480s) | [Game](https://www.chess.com/game/live/52079490979) |
| 69 | 2022.07.20 | DinuBlore | 1-0 | 11 | [42:40](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2560s) | [Game](https://www.chess.com/game/live/52080554011) |
| 70 | 2022.07.20 | krake17 | 1-0 | 11 | [45:10](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2710s) | [Game](https://www.chess.com/game/live/52081884549) |
| 71 | 2022.07.20 | Reppie67 | 1-0 | 11 | [54:00](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3240s) | [Game](https://www.chess.com/game/live/52083100493) |
| 72 | 2022.07.20 | CastellanoViejo | 1-0 | 11 | [1:07:20](https://www.youtube.com/watch?v=vyxK0vqxowo&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4040s) | [Game](https://www.chess.com/game/live/52084237147) |
| 73 | 2022.07.20 | MezzomortoRafikOuchene | 1-0 | 12 | [0:50](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=50s) | [Game](https://www.chess.com/game/live/52086651501) |
| 74 | 2022.07.20 | eadk | 1-0 | 12 | [14:30](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=870s) | [Game](https://www.chess.com/game/live/52088357461) |
| 75 | 2022.07.20 | axxxbyy | 1-0 | 12 | [20:40](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1240s) | [Game](https://www.chess.com/game/live/52089566457) |
| 76 | 2022.07.20 | viniaug | 1-0 | 12 | [26:10](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1570s) | [Game](https://www.chess.com/game/live/52089669017) |
| 77 | 2022.07.20 | Gringobiloba | 0-1 | 12 | [27:30](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1650s) | [Game](https://www.chess.com/game/live/52090833187) |
| 78 | 2022.07.20 | arthur_bach | 1-0 | 12 | [42:10](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2530s) | [Game](https://www.chess.com/game/live/52092552809) |
| 79 | 2022.07.20 | hh33zz | 1-0 | 12 | [54:30](https://www.youtube.com/watch?v=EOfNcvkpQp8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3270s) | [Game](https://www.chess.com/game/live/52093177629) |
| 80 | 2022.07.21 | zedipo | 1-0 | 13 | [4:40](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=280s) | [Game](https://www.chess.com/game/live/52181458181) |
| 81 | 2022.07.21 | ChessSmarty01 | 1-0 | 13 | [8:30](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=510s) | [Game](https://www.chess.com/game/live/52182664415) |
| 82 | 2022.07.21 | Stingray1960 | 1-0 | 13 | [10:40](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=640s) | [Game](https://www.chess.com/game/live/52183204997) |
| 83 | 2022.07.21 | nesir78 | 1-0 | 13 | [33:20](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2000s) | [Game](https://www.chess.com/game/live/52183808511) |
| 84 | 2022.07.21 | chessmechanic-coaching | 1-0 | 13 | [34:00](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2040s) | [Game](https://www.chess.com/game/live/52184445883) |
| 85 | 2022.07.21 | Kemoss | 1-0 | 13 | [51:30](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3090s) | [Game](https://www.chess.com/game/live/52186798299) |
| 86 | 2022.07.22 | zatonoichi | 1-0 | 13 | [54:38](https://www.youtube.com/watch?v=izNk3Dd4zZA&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3278s) | [Game](https://www.chess.com/game/live/52186865013) |
| 87 | 2022.08.08 | geovin | 1-0 | 14 | [5:40](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=340s) | [Game](https://www.chess.com/game/live/53730032083) |
| 88 | 2022.08.08 | Torben10 | 1-0 | 14 | [10:10](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=610s) | [Game](https://www.chess.com/game/live/53731256429) |
| 89 | 2022.08.08 | chikoverde | 1-0 | 14 | [15:20](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=920s) | [Game](https://www.chess.com/game/live/53732416629) |
| 90 | 2022.08.08 | Vhangani | 1-0 | 14 | [25:00](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1500s) | [Game](https://www.chess.com/game/live/53733015913) |
| 91 | 2022.08.08 | grinder286 | 1-0 | 14 | [34:20](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2060s) | [Game](https://www.chess.com/game/live/53733625255) |
| 92 | 2022.08.08 | dhidikp | 1-0 | 14 | [49:00](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2940s) | [Game](https://www.chess.com/game/live/53734244289) |
| 93 | 2022.08.08 | jahadek | 1-0 | 14 | [53:50](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3230s) | [Game](https://www.chess.com/game/live/53734794643) |
| 94 | 2022.08.08 | johnantione | 0-1 | 14 | [1:04:30](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3870s) | [Game](https://www.chess.com/game/live/53736625987) |
| 95 | 2022.08.08 | hecsedli | 1-0 | 14 | [1:14:30](https://www.youtube.com/watch?v=3PohHinhSHY&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4470s) | [Game](https://www.chess.com/game/live/53738959179) |
| 96 | 2022.08.09 | mastercj2330 | 1-0 | 15 | [3:30](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=210s) | [Game](https://www.chess.com/game/live/53826613871) |
| 97 | 2022.08.09 | kingforaknight | 1-0 | 15 | [8:20](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=500s) | [Game](https://www.chess.com/game/live/53827190027) |
| 98 | 2022.08.09 | Chrisn1231 | 1-0 | 15 | [21:20](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1280s) | [Game](https://www.chess.com/game/live/53827821201) |
| 99 | 2022.08.10 | Art-A | 1-0 | 15 | [32:30](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1950s) | [Game](https://www.chess.com/game/live/53830170385) |
| 100 | 2022.08.10 | JAPR0 | 0-1 | 15 | [40:50](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2450s) | [Game](https://www.chess.com/game/live/53830742107) |
| 101 | 2022.08.10 | salilsurendran | 1-0 | 15 | [47:50](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2870s) | [Game](https://www.chess.com/game/live/53831353201) |
| 102 | 2022.08.10 | freddypeguero | 1-0 | 15 | [51:10](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3070s) | [Game](https://www.chess.com/game/live/53832624019) |
| 103 | 2022.08.14 | AstroIgor1 | 1-0 | 15 | [1:01:30](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3690s) | [Game](https://www.chess.com/game/live/54250753167) |
| 104 | 2022.08.14 | medranokiller | 1-0 | 15 | [1:14:20](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4460s) | [Game](https://www.chess.com/game/live/54253204661) |
| 105 | 2022.08.14 | EduBueno | 1-0 | 15 | [1:22:30](https://www.youtube.com/watch?v=MHqTZWomK6A&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4950s) | [Game](https://www.chess.com/game/live/54253813259) |
| 106 | 2022.08.14 | sandager | 1-0 | 16 | [8:30](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=510s) | [Game](https://www.chess.com/game/live/54254993399) |
| 107 | 2022.08.14 | davidpaykinOnTwitch | 1-0 | 16 | [10:00](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=600s) | [Game](https://www.chess.com/game/live/54256201285) |
| 108 | 2022.08.14 | MRJ47 | 1-0 | 16 | [18:30](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1110s) | [Game](https://www.chess.com/game/live/54257401773) |
| 109 | 2022.08.14 | Migcha | 1-0 | 16 | [25:00](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1500s) | [Game](https://www.chess.com/game/live/54258542445) |
| 110 | 2022.08.14 | frankLSD | 1-0 | 16 | [33:50](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2030s) | [Game](https://www.chess.com/game/live/54259157407) |
| 111 | 2022.08.14 | Espiralquantica | 1-0 | 16 | [46:20](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2780s) | [Game](https://www.chess.com/game/live/54260405337) |
| 112 | 2022.08.15 | Anibalcabrera21 | 1-0 | 16 | [59:10](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3550s) | [Game](https://www.chess.com/game/live/54261544667) |
| 113 | 2022.08.15 | AsaHoffmann | 1-0 | 16 | [1:01:50](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3710s) | [Game](https://www.chess.com/game/live/54261583231) |
| 114 | 2022.08.16 | Victzzz | 0-1 | 16 | [1:13:00](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4380s) | [Game](https://www.chess.com/game/live/54413359867) |
| 115 | 2022.08.16 | thaltico | 1-0 | 16 | [1:22:40](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4960s) | [Game](https://www.chess.com/game/live/54415204061) |
| 116 | 2022.08.16 | papa_1960 | 1-0 | 16 | [1:36:20](https://www.youtube.com/watch?v=klPQ8hPGCnU&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=5780s) | [Game](https://www.chess.com/game/live/54416433775) |
| 117 | 2022.08.17 | Gionabaldo2 | 1-0 | 17 | [4:00](https://www.youtube.com/watch?v=qm5t3xAdJMk&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=240s) | [Game](https://www.chess.com/game/live/54499831195) |
| 118 | 2022.08.17 | pointblanc9 | 1-0 | 17 | [13:20](https://www.youtube.com/watch?v=qm5t3xAdJMk&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=800s) | [Game](https://www.chess.com/game/live/54500437765) |
| 119 | 2022.08.17 | Knights_B4_Bishops | 1-0 | 17 | [27:40](https://www.youtube.com/watch?v=qm5t3xAdJMk&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1660s) | [Game](https://www.chess.com/game/live/54501679419) |
| 120 | 2022.08.17 | giardinetta | 1-0 | 17 | [42:20](https://www.youtube.com/watch?v=qm5t3xAdJMk&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2540s) | [Game](https://www.chess.com/game/live/54502747463) |
| 121 | 2022.08.17 | chessrol | 1-0 | 17 | [47:10](https://www.youtube.com/watch?v=qm5t3xAdJMk&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2830s) | [Game](https://www.chess.com/game/live/54504578481) |
| 122 | 2022.08.17 | safenorsound | 1-0 | 18 | [2:00](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=120s) | [Game](https://www.chess.com/game/live/54505767975) |
| 123 | 2022.08.17 | hightide | 0-1 | 18 | [12:10](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=730s) | [Game](https://www.chess.com/game/live/54507609327) |
| 124 | 2022.08.17 | speedyplayer2-inac | 1-0 | 18 | [24:20](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=1460s) | [Game](https://www.chess.com/game/live/54508871989) |
| 125 | 2022.08.17 | baronmesmer | 1-0 | 18 | [35:10](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2110s) | [Game](https://www.chess.com/game/live/54510667445) |
| 126 | 2022.08.17 | falk6464 | 1-0 | 18 | [38:10](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2290s) | [Game](https://www.chess.com/game/live/54511180359) |
| 127 | 2022.08.18 | Timotije67 | 1/2-1/2 | 18 | [46:40](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=2800s) | [Game](https://www.chess.com/game/live/54588057473) |
| 128 | 2022.08.18 | Boninknights | 1-0 | 18 | [57:50](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3470s) | [Game](https://www.chess.com/game/live/54589729435) |
| 129 | 2022.08.18 | Topmiscia | 1-0 | 18 | [1:04:20](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=3860s) | [Game](https://www.chess.com/game/live/54590932663) |
| 130 | 2022.08.18 | fidemax | 1-0 | 18 | [1:16:00](https://www.youtube.com/watch?v=Zkcyyj9xTT8&list=PLUjxDD7HNNTiljFCufDXDSjEQH1cIdbSx&t=4560s) | [Game](https://www.chess.com/game/live/54591542165) |

## Attribution and material boundaries

The teaching source is Aman Hambleton's freely published Chessbrah series. The guide is an original editorial study aid, with its own structure, explanations and labelled engine analysis. It does not reproduce a paid course or present auto-captions as a verbatim transcript. The videos remain with their rights holders; the game scores come directly from public Chess.com archives. Raw caption files, downloaded video metadata and sampled video frames are working evidence and are not redistributed in this repository. Cburnett-derived piece geometry and python-chess retain the notices in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
