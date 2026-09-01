# Third-party notices

This file records external projects and assets that are used now or approved as project defaults. Their licenses apply to the respective components.

## Lichess

- Project: Lichess (`lila`)
- Source: https://github.com/lichess-org/lila
- Copyright: the Lichess authors and contributors
- License: GNU Affero General Public License v3.0 or later, except for components identified separately in Lichess's `COPYING.md`
- Use here: design and interaction reference; compatible source may be incorporated in future with file-level provenance preserved

Lichess is credited as the primary aesthetic and chess-interface convention for this project. This project is independent and is not affiliated with or endorsed by Lichess.

## Chessground

- Project: Chessground
- Source: https://github.com/lichess-org/chessground
- Copyright: the Chessground authors and contributors
- License: GNU General Public License v3.0 or later
- Use here: approved default for future interactive chessboards

## Cburnett chess pieces

- Work: Cburnett chess-piece artwork
- Author: Colin M. L. Burnett
- Lichess source: https://github.com/lichess-org/lila/tree/master/public/piece/cburnett
- License recorded by Lichess: GNU General Public License v2.0 or later
- Use here: default piece convention and piece geometry embedded in generated SVG diagrams

The generated SVG diagrams under `guides/assets/` embed Cburnett-derived piece geometry. Their source form is the SVG itself. Preserve this notice when redistributing or modifying those diagrams.

## python-chess

- Project: python-chess
- Source: https://github.com/niklasf/python-chess
- Copyright: Niklas Fiekas and contributors
- License: GNU General Public License v3.0 or later
- Use here: legal move validation and reproducible SVG diagram rendering

## Important asset boundary

Lichess's asset directory contains several different licenses, including non-commercial and otherwise restricted sets. Inclusion in the Lichess repository does not by itself make an asset reusable under this repository's AGPL license. Check the upstream `COPYING.md` and record every imported asset here before use.
