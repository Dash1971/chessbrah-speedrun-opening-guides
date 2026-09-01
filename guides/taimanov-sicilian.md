# The Taimanov, as Aman Hambleton Plays It

A practical guide to Aman's Taimanov speedrun, from 400 to 2400. The aim is to learn "where the pieces go," the order in which they usually go there, and the positions in which that order must change.

Source series: [Aman's Taimanov Speedrun](https://www.youtube.com/playlist?list=PLUjxDD7HNNTjZAD99gBAKVm_ZipXTtNYn)

Companion study: [annotated repertoire PGN](../pgn/taimanov-sicilian-repertoire.pgn)

All boards are shown from Black's side, matching Aman's point of view in the speedrun. Green arrows show Black's plans, blue arrows show piece routes or lines, red marks an immediate tactical target, and gold circles mark the square that makes the idea work.

### Guide map

- **Build the system:** [core setup](#1-the-core-system), [read White's setup](#before-playing-the-setup-read-whites-moves), [meet `e5`](#before-nf6-give-the-knight-a-square), [d4 exchanges](#2-when-to-exchange-on-d4), and [c6 recaptures](#3-the-c6-recapture-decision)
- **Play the main structures:** [short castling](#4-white-castles-short-build-on-the-queenside), [English Attack](#5-the-english-attack-be3-qd2-f3-and-long-castling), the [`e5`/`...b4` counter-threat](#the-e5-counter-threat-b4), [quiet development](#6-quiet-be2-and-bd3-setups), and [bxc6](#7-the-bxc6-structure)
- **Handle deviations:** [Maroczy](#8-the-maroczy-bind-with-5c4), [Bowdler](#9-the-bowdler-attack-with-3bc4), [Alapin](#10-the-alapin-with-2c3), [other sidelines](#11-smith-morra-early-c4-and-f4-systems), and [Nb3/b3](#12-nb3-and-b3bb2-systems)
- **Convert the position:** [recurring themes](#13-recurring-tactical-and-positional-themes), [endgames](#14-structures-and-endgames), [practical play](#15-practical-play), and the [final checklist](#16-practical-checklist)

## 1. The core system

The basic Open Sicilian route is:

`1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 Qc7`

Aman starts with `2...e6` because it keeps more options open than `2...Nc6`. In a normal Open Sicilian, Black then brings the b8-knight to c6, the queen to c7, and only then plays `...a6`. At the start of the series, Aman describes the task simply: remember ["where the pieces go" and "what order we play the moves in"](https://www.youtube.com/watch?v=s6qTfdsNGrY&t=640s).

Black's usual destinations are:

- pawns on `e6`, `a6`, and `b5` after the c-pawn exchanges on d4;
- queen on `c7`;
- queenside knight on `c6`;
- dark-squared bishop on `b7`;
- rook on `c8` when the c-file is useful;
- kingside pieces on `f6` and `e7`, followed by castling when tactics permit.

The common route is `...Nc6`, `...Qc7`, `...a6`, `...b5`, and `...Bb7`. The rook often follows to c8. The d-pawn usually stays on d7 until Black needs `...d6` or `...d5`. This is the setup to learn, but White's moves decide whether Black can play it in this order.

<div>
  <img src="assets/taimanov/diagram-01-core-setup.svg" alt="Core Taimanov setup after 8...Bb7, viewed from Black's side" width="480"/>
  <p><strong>The core setup after 8...Bb7.</strong> Black has played <code>...e6</code>, <code>...Nc6</code>, <code>...Qc7</code>, <code>...a6-b5</code>, and <code>...Bb7</code>. The green arrow shows <code>...b4</code>; the blue arrow shows the c6-knight's pressure on d4. The gold ring on d7 is a reminder that the d-pawn is still flexible.</p>
</div>

<div>
  <img src="assets/taimanov/diagram-02-target-position.svg" alt="A typical Taimanov position with queen c7, bishop b7, and rook c8" width="480"/>
  <p><strong>A typical target position.</strong> The queen, bishop, and rook work together from c7, b7, and c8. Black can play <code>...b4</code> when it gains time, while the d-pawn can still move to d6 or d5 as needed.</p>
</div>

### Two rules for the move order

1. Keep the d-pawn at home unless it has a job. Play `...d6` to answer `e5`, or `...d5` when the centre can be challenged. Keeping the pawn on d7 also means several `Qa4+` ideas do not work.
2. Develop first on the side opposite White's king. If White castles short, build the queenside. If White is preparing to castle long, bring out the kingside pieces first. Aman states this rule directly in the [KNeres post-game analysis](https://www.youtube.com/watch?v=iivW3TFDIi8&t=742s).

### Before playing the setup, read White's moves

The setup is the default, not the answer to every position. Make this first decision before playing `...Nc6`, `...Qc7`, and `...a6`:

- **White plays `d4` and must recapture with a piece:** take on d4 and use the normal Taimanov order.
- **White plays `c3`:** attack e4 with `...Nf6`. In Aman's words, ["you have to attack the e-pawn"](https://www.youtube.com/watch?v=AmDns9omB7g&t=396s). Do not put the queen on c7 and knight on c6 as if this were an Open Sicilian.
- **White plays `c4`:** `...b5` is no longer available in the normal way. Use `...Nf6`, `...Bc5`, and `...Qb6` against the centre.
- **White plays `Bc4` before `d4`:** play `...e6`, `...a6`, and `...b5` before bringing out the b8-knight. Aman calls this ["pawns first"](https://www.youtube.com/watch?v=_usnXzNrTU8&t=1267s).
- **White does not open the centre with `d4`:** remember that this is a Closed Sicilian. Do not force the Open Sicilian setup without checking what White is doing.

### Before `...Nf6`, give the knight a square

White's `e4-e5` push is one of the series' most repeated warnings. Before putting the knight on f6, know where it will go after `e5`:

- d5, e4, or g4 may be useful in the exact position;
- `...d6` gives the knight d7 as a safe retreat;
- a retreat to g8 usually means Black chose the wrong order.

Aman's version is blunt: ["If your knight has to go back to g8, you have messed the opening up"](https://www.youtube.com/watch?v=iivW3TFDIi8&t=179s). This is why `...d6` often comes before `...Nf6` when White has prepared `f4-e5`.

### Move-order refinements

- Delay castling while White is still arranging the attack. The queenside setup moves remain useful, so Black can often wait until White's intentions are clear.
- Do not commit to `...b5` too early when White's b1-knight has not chosen a square. After `Nc3`, `...b5-b4` gains time; before `Nc3`, White may meet `...b4` with `Nbd2` in one move.
- If the only aim is to place the bishop on b7, `...b6` may be cleaner than `...a6-b5`, especially when an early `a4` would start an unnecessary argument.
- If White plays `d3` and later `d4`, Black has reached the normal structure with a free tempo.
- If `Nb5` attacks the queen on c7, `...Qb8` followed by `...a6` is a common answer. Check that it works in the position before using it.

## 2. When to exchange on d4

After White plays `d4`, Aman normally captures when White must answer with a piece:

- `Nxd4` or `Qxd4`: the normal Open Sicilian structure;
- `cxd4`: be careful, because exchanging may hand White a broad pawn centre.

If White can answer with `cxd4`, stop and check. The exchange may give White a broad pawn centre. This is why `c3` changes the setup: Black should attack e4 before White plays d4.

## 3. The c6 recapture decision

The speedrun uses two simple defaults:

- if the queen is already on c7 and `...Qxc6` is safe, recapture with the queen and keep the pawn structure intact;
- if the queen is not ready, `...bxc6` is often "nice and simple": follow with `...d5`, and after `exd5` usually recapture `cxd5`.

Then check the position. An immediate `e5` can change the answer, a bishop recapture can be best, and `...dxc6` is sometimes required for a concrete reason. The Maroczy section gives one such exception. The question is whether the resulting structure and the `e5` break are safe.

The same structural idea appears after `...Ne5-c4 Bxc4`: `...Qxc4` often keeps the c-file and queenside pawns healthier than `...bxc4`.

<div>
  <img src="assets/taimanov/diagram-03-qxc6-battery.svg" alt="Taimanov queen recapture on c6 aligned with the bishop on b7" width="480"/>
  <p><strong>After 9...Qxc6.</strong> Black keeps the pawns together and puts the queen beside the b7-bishop. The queen attacks e4, marked in red. The diagonal toward g2 is still blocked, so Black must calculate <code>e5</code> before continuing the setup.</p>
</div>

## 4. White castles short: build on the queenside

The ideal plan is:

1. `...a6` prepares `...b5` and controls b5.
2. `...b5` gains space and opens the long diagonal.
3. `...Bb7` activates the dark-squared bishop.
4. `...Rc8` uses the half-open c-file when tactics allow.
5. Add `...Nf6`, `...Be7`, and `...O-O` in the order demanded by the position.

Do not play the last three moves mechanically. Before every routine developing move, check White's `e5`, `Nd5`, and captures on c6.

## 5. The English Attack: Be3, Qd2, f3, and long castling

`Be3` and `Qd2` usually announce queenside castling. Switch priorities:

- develop `...Nf6` early;
- use `...Ng4` if the bishop on e3 is genuinely unprotected;
- reinforce with `...d6` when White's `f3/g4/g5` plan needs a stable answer;
- race with `...b5-b4`, then consider `...a5-a4-a3`;
- use `...Qa5`, `...Bb4`, and sometimes `...Bxc3` to attack dark squares around the king.

There are two different h-pawn ideas:

- **Before White plays `g4`:** Aman likes `...h5` to slow the pawn storm. If White prepares `g4` with `h3`, Black can answer `...h4`. Aman explains that `...h5` ["slows down White's moves"](https://www.youtube.com/watch?v=iivW3TFDIi8&t=133s); it does not prevent them forever.
- **After White has played `g4`:** `...h6` can meet `g5` with `...hxg5`. White may have to recapture with a piece, and opening the g-file can expose White's own king. This depends on the exact position.

Be suspicious of `...Bxa3`. Check both knight captures on b5 before grabbing the pawn.

<div>
  <img src="assets/taimanov/diagram-05-english-attack.svg" alt="English Attack position after Black has played b4 against the c3 knight" width="480"/>
  <p><strong>The English Attack race after 12...b4.</strong> The c3-knight must make a decision, and <code>...bxc3</code> may open lines around White's king. Black can follow with <code>...a5-a4-a3</code>. The point is to make contact with the king before White's kingside attack arrives.</p>
</div>

### The `e5` counter-threat: `...b4!`

In the KNeres post-game analysis, Aman calls this a very important Taimanov idea. White has castled queenside, Black has a pawn on b5, and `e5` attacks the f6-knight. Instead of moving the knight at once, first look for `...b4`.

The mechanism is:

1. `e5` attacks the f6-knight.
2. `...b4!` counterattacks the c3-knight instead of answering White's threat.
3. If the c3-knight moves, d5 becomes available to Black's f6-knight.
4. If White plays `exf6`, Black can continue `...bxc3`, attacking the queen on d2. White must deal with the pawn because `...cxd2+` would take the queen with check. One line is `Qxc3 Qxc3 bxc3 Bxf6`, with comfortable play for Black.

<div>
  <img src="assets/taimanov/diagram-13-e5-b4-counter-threat.svg" alt="Taimanov position where e5 attacks the f6-knight and Black counters with b4 against the c3-knight" width="480"/>
  <p><strong>After 11.e5: counterattack before retreating.</strong> White's red arrow is the threat <code>e5xf6</code>. Black replies <code>...b4!</code>, attacking the c3-knight and loosening its control of d5. The blue route shows the reward: once c3 is cleared, the f6-knight can often reach d5 instead of retreating. This is the position Aman used to teach the motif.</p>
</div>

`...b4` itself is not check. The line works because White's king is on c1, queen on d2, and knight on c3, while Black's b-pawn is already on b5. If those details change, calculate again.

## 6. Quiet Be2 and Bd3 setups

Against a passive `Be2`, look for immediate pressure on e4 with `...Bb4` and sometimes `...Nxe4`.

Against `Bd3`, the key move is often `...Ne5`. Aman calls e5 the ["perfect pivot square"](https://www.youtube.com/watch?v=NYTGOoqx7Tk&t=1574s):

- it attacks the bishop;
- it prepares `...Nc4`;
- `...Nc4` is strongest when White's queen is on d2, because queen and bishop can be forked;
- with the queen on e2, the jump may achieve much less;
- with a white knight on b3, insert `...b4` when needed so `Na5` does not solve White's problems.

After `...Nc4 Bxc4`, prefer `...Qxc4` when it preserves the c-file and pawn chain. Avoid exchanging on d3 merely to let `cxd3` repair White's structure and activate the c-file.

<div>
  <img src="assets/taimanov/diagram-06-ne5-pivot.svg" alt="Knight on e5 attacking a bishop on d3 and preparing Nc4" width="480"/>
  <p><strong>The <code>...Ne5-c4</code> route.</strong> On e5 the knight attacks Bd3 and prepares <code>...Nc4</code>. With White's queen on d2, a knight on c4 attacks both queen and bishop. With the queen on e2, or a knight on b3 ready for Na5, the same route may do much less.</p>
</div>

## 7. The bxc6 structure

After `Nxc6 bxc6`, the doubled c-pawns are useful if they support an immediate `...d5`.

Typical plans:

- `...d5`, meeting `exd5` with `cxd5` when appropriate;
- `...Nd7-c5` to hit a bishop on d3;
- `...Ba6` to offer the light-squared bishop for an important defender;
- `...a5-a4` to stop b3 and restrict White's queenside;
- `...Qb6` and `...Na6-b4` to pressure a2 and b2.

The `cxd5` recapture is important: it removes the doubled c-pawn and usually leaves connected central pawns. Taking with the e-pawn can create an extra pawn island and open a file toward Black's king. Once the central majority is established, it must eventually advance with `...e5-e4` or `...d5-d4`; if the pawns never move, Black has structure but no winning attempt.

<div>
  <img src="assets/taimanov/diagram-04-bxc6-d5.svg" alt="The bxc6 structure at the moment Black can recapture cxd5" width="480"/>
  <p><strong>Use the c6-pawn to build the centre.</strong> After <code>...bxc6</code>, <code>...d5</code>, and <code>exd5</code>, the c6-pawn recaptures on d5. The doubled pawns disappear and Black gets connected pawns on d5 and e6.</p>
</div>

The king can sometimes remain on e8 because the centre is closed and castling would invite `Qg4` or `Bh6`. This is a practical option, not a blanket rule.

## 8. The Maroczy Bind with 5.c4

After `5.c4`, do not force the normal `...b5` plan. White controls that square.

Use:

- `...Nf6` to hit e4;
- `...Bc5` to pressure the d4-knight;
- `...Qb6` to attack d4 and b2;
- checks on b4 or a5 when they create a real tactical problem.

Model tactic:

`1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.c4 Nf6 6.Nc3 Bc5 7.Be3 Qb6 8.Na4 Bb4+ 9.Bd2 Qxd4`

The point is to take the hanging knight. Retreating the queen after `Bd2` would lose the tactical justification for the check.

<div>
  <img src="assets/taimanov/diagram-07-maroczy-tactic.svg" alt="Maroczy Bind tactic with queen on b6 attacking the knight on d4" width="480"/>
  <p><strong>After 9.Bd2, take the knight.</strong> White has blocked the check, but the knight on d4 is loose. Black should play <code>9...Qxd4</code>; retreating the queen would miss the point of <code>...Bb4+</code>.</p>
</div>

## 9. The Bowdler Attack with 3.Bc4

The e6-pawn protects f7 and takes d5 away from White's bishop.

Aman's preferred move order is pawns before pieces:

`1.e4 c5 2.Nf3 e6 3.Bc4 a6 4.Nc3 b5`

If the bishop retreats to b3, `...c4` can force it to a4 and leave it badly placed. The bishop is restricted, not trapped: `Ba4` remains legal.

Only use `...c4` against a bishop on b3. If the bishop retreats to d3, or White has played d3 and controls c4, return to normal development. Against an early a4, `...b6` and `...Bb7` often preserve the same strategic idea without forcing `...b5`.

<div>
  <img src="assets/taimanov/diagram-08-bowdler-clamp.svg" alt="Bowdler bishop restricted after Black plays c4, with Ba4 shown as the escape" width="480"/>
  <p><strong>The bishop still has Ba4.</strong> After <code>...c4</code>, the bishop follows the gold route to a4. Black has gained space and time, and <code>...b4</code> can chase the c3-knight, but the bishop is not trapped.</p>
</div>

## 10. The Alapin with 2.c3

Do not force the standard Taimanov formation:

`1.e4 c5 2.c3 Nf6`

The rule is about the pawn on c3, not the move number. After `1.e4 c5 2.Nf3 e6 3.c3`, use `3...Nf6` for the same reason: attack e4 before White builds the full centre.

After `e5` and `c4`, Aman prefers retreating the knight to c7 rather than b6. From c7 it can support `...d6`, `...b5`, and `...Ne6`.

Undermine the e5-pawn with `...d6`, and if it can be removed safely, play `...dxe5` before returning to the familiar `...e6` structure. In these positions `...b6` and `...Bb7` are often more useful than an automatic `...a6-b5` expansion.

<div>
  <img src="assets/taimanov/diagram-09-alapin-reset.svg" alt="Alapin position after the black knight retreats to c7" width="480"/>
  <p><strong>Against c3, attack e4 first.</strong> After <code>e5</code> and <code>c4</code>, the knight goes to c7 rather than b6. From c7 it can reach e6, support <code>...d6</code>, and leave <code>...b5</code> available.</p>
</div>

## 11. Smith-Morra, early c4, and f4 systems

### Smith-Morra

The speedrun declines with `1.e4 c5 2.d4 cxd4 3.c3 d3`, returning the pawn and keeping the c-file closed. A practical setup is `...Nc6`, `...d6`, `...g6`, `...Bg7`, and `...Bg4` to reduce White's attacking force.

This is the choice Aman uses in the speedrun; accepting the gambit is also playable.

<div>
  <img src="assets/taimanov/diagram-10-morra-declined.svg" alt="Smith-Morra declined setup with Bg4 targeting the f3 knight" width="480"/>
  <p><strong>The declined Morra setup.</strong> Returning the pawn with <code>...d3</code> keeps the c-file closed. Black develops with <code>...Nc6</code>, <code>...d6</code>, <code>...g6</code>, and <code>...Bg4</code>, aiming to trade White's f3-knight.</p>
</div>

### Early c4 / English structures

After an early c4 that prevents `...b5`, switch plans. In the symmetrical English structure, fianchetto with `...g6` and `...Bg7`; `...Nge7` can be more harmonious than forcing the normal Taimanov piece placement.

### f4 systems

Against f4, `e4-e5` carries extra force and e5 may no longer be available to Black's knight. Useful adjustments include:

- `...d6` to challenge the e5 advance;
- rerouting the knight through a5-c4;
- developing a kingside knight through h6-f5;
- using `...h5-h4` and `...Nh5-g3` when White has weakened g3.

<div>
  <img src="assets/taimanov/diagram-11-f4-adaptation.svg" alt="Taimanov adaptation against f4 with a black pawn on d4 and knight route to f5" width="480"/>
  <p><strong>Against f4, play in the centre.</strong> <code>...d4</code> takes space and makes e5 a target. Because White's f-pawn controls e5, Black's knight can use e7 and f5 instead.</p>
</div>

### Additional practical sidelines

- Against an early `Qxd4`, develop with `...Nc6` and gain the tempo Black wanted anyway.
- Against `a4` hitting a pawn already on b5, consider pushing past with `...b4` rather than automatically capturing or defending.
- If `Nb5` attacks the queen on c7, `...Qb8` followed by `...a6` is a common answer.
- Against `Bg5`, `...Be7` can welcome `Bxf6`: Black gains the bishop pair and White gives up an important dark-squared bishop.
- Against `Qg4`, `...g6` is often the simple answer to `Qxg7` and `Bh6` ideas, though the weakened dark squares still need respect.
- The `2.a3` Wing Gambit is a separate Sicilian problem. Accepting it is possible, but do not confuse its piece retreats with the normal Taimanov setup.

## 12. Nb3 and b3/Bb2 systems

Against Nb3 or a b3/Bb2 setup:

- preserve the dark-squared bishop whenever practical;
- do not rush `...Bb7` into a setup designed to trade that bishop;
- use `...a6` to reduce `Bb5xc6` ideas;
- consider `...d4` to close the b2-bishop's diagonal;
- meet a kingside pawn expansion in the centre before spending a tempo on a rook lift.

In the annotated PGN, `...Ne5` replaces an immediate `...Rb8` because the central move is urgent and the rook move is too slow.

<div>
  <img src="assets/taimanov/diagram-12-nb3-counter.svg" alt="Nb3 and kingside pawn expansion met by the central move Ne5" width="480"/>
  <p><strong>Meet the attack in the centre.</strong> White has castled long and played g4, but <code>...Ne5</code> attacks that pawn, prepares <code>...Nc4</code>, and keeps <code>...b4</code> ready. This is why the immediate <code>...Rb8</code> was too slow: Black already has three forcing ideas.</p>
</div>

## 13. Recurring tactical and positional themes

### The long-diagonal battery

The queen on c7 and bishop on b7 often work together along the long diagonal. When a defender leaves f3 or f1, check `...Qxg2`; when the queen also attacks h2, `...Ng4` may create mating ideas. This is also why `...Qxc6` can be useful after `Nxc6`: the queen joins the bishop without losing a tempo.

### Preserve the dark-squared bishop

White's bishop on e3 often supports the entire kingside pawn storm, so `...Ng4` or a favorable exchange can remove an important attacker. Black's own bishop on b7 is normally the piece to preserve. If a bishop trade is desirable, use the light-squared bishop with ideas such as `...Ba6` or `...Qb6` followed by `...Ba6`.

### Can Black play `...d5`?

Ask whether Black can play `...d5` without allowing a strong `e5`. If `e5` still sends a knight to a bad square, prepare the break first.

### Open files and a second target

On an open file, the queen often belongs behind the doubled rooks. If the front rooks are exchanged, a queen recapture may keep control of the file. If White can defend one pawn forever, keep the pressure and look for another target on the other side of the board. Aman describes this as ["poking and prodding on the other side"](https://www.youtube.com/watch?v=GxGqIrEye4w&t=3424s).

## 14. Structures and endgames

Aman repeatedly treats the queenless Sicilian as something Black should welcome when the concrete position permits it. His point is structural, not a promise that every Sicilian ending is better: if the other factors are equal, Black's compact central pawns and active pieces often make the ending comfortable.

Practical themes from the speedrun:

- do not avoid a sound queen trade merely because the opening began as a fighting Sicilian;
- keep the `d7`- and `e6`-pawns when their compact wall restricts White and supports the king;
- use `...f6` to challenge e5, open the f- or g-file, and give the king an active route;
- activate the dark-squared bishop, often on c5 or b7, before simplifying;
- advance `...h5-h4` when the centre is stable and the kingside pawns can gain space;
- judge each trade by the resulting activity and pawn structure, not by a blanket rule;
- judge doubled pawns by the squares they control and the files they open, not by appearance alone;
- with one bishop against the bishop pair, place pawns mainly on the colour your remaining bishop does not control;
- leave the king in the centre when the position is closed and castling would merely give White a target.

One recurring model is a strong bishop plus the `d7/e6` wall, followed by `...f6`, activity on the g-file, and an advancing h-pawn. Aman explicitly describes these positions as comfortable rather than automatically winning: Black can still be outplayed, and tactical or positional details can reverse the structural preference.

## 15. Practical play

- Prefer a simple continuation that you understand to a marginally more accurate move that demands a long calculation.
- Use knowledge of the setup to save time for the decisions that matter: recaptures, `e5`, castling direction, and tactical jumps.
- Get the pieces out. Do not spend several tempi trying to win one pawn while pieces remain undeveloped.
- Do not spend a tempo on a check or attack that lets White play a useful defensive move for free.
- Practise the structure "with colors reversed" from White's side through `c4`, `Nf3`, `b3`, `Bb2`, castling, and `Rc1`. It helps make the familiar squares automatic.

## 16. Practical checklist

Before each move, ask:

1. Is this an Open Sicilian, or have `c3`, `c4`, or `Bc4` changed the move order?
2. If I play `...Nf6`, where does the knight go after `e5`?
3. If `e5` attacks the f6-knight after long castling, does `...b4` attack c3 and clear d5?
4. If White takes on c6, should I use the queen or the b-pawn? Is there a concrete reason for another recapture?
5. Where is White's king, and which side should I develop first?
6. Is `...b5` still possible, and has White's b1-knight committed yet?
7. Does `...Ne5-c4` attack something in this position?
8. Am I keeping the dark-squared bishop when the structure calls for it?

Learn the setup, but keep reading the board. As Aman puts it early in the series: ["stick to the setup"](https://www.youtube.com/watch?v=yVIB7_Q7sLk&t=1698s)—until White gives you a reason to change it.
