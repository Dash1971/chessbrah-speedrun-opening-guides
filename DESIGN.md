# Design conventions

The default chess presentation follows familiar Lichess conventions. This is a usability baseline, not a pixel-for-pixel clone and not a claim of affiliation.

## Defaults

- Put the board and current position first; supporting explanation should remain close to it.
- Use the Cburnett piece style by default.
- Use a restrained brown board palette by default, with sufficient contrast and optional alternatives.
- Show coordinates clearly and preserve the selected board orientation.
- Use familiar move navigation: previous, next, first, last, and keyboard arrow controls where interactive.
- Keep annotations legible and conventional: arrows, highlighted squares, last-move indication, and check indication.
- Make layouts responsive, keyboard-operable, and usable without hover.
- Prefer compact controls and progressive disclosure over permanent visual clutter.
- Preserve PGN/FEN interoperability and avoid proprietary study formats as the only export path.

## Implementation policy

When existing Lichess or Chessground code materially improves the chess interaction, reuse is preferred over an incompatible imitation. Imported code and assets must retain their upstream notices and be recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Do not copy Lichess logos, favicons, trademarks, or identity elements. Refer to Lichess by name only for attribution, interoperability, or explanation. This project is independent and is not endorsed by Lichess.

## Licensing baseline

Repository-authored work uses `AGPL-3.0-or-later`. Compatible third-party components retain their own licenses, including GPLv3+ for Chessground and GPLv2+ for Cburnett pieces. Before adding another Lichess asset, check its entry in Lichess's `COPYING.md`; not every Lichess asset is free for unrestricted reuse.
