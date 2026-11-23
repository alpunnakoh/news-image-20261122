# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/alpunnakoh/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/alpunnakoh/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image summing up the world news of **Sunday, 22 November 2026**, drawn
as a newspaper front page: a masthead with the date, a lead story, four
panels and an "also on this day" strip — six stories across regions and
fields.

## The six stories (all reported 21–22 Nov 2026)

1. **COP31 collapses** — climate talks in Antalya, Turkey end with no deal
   after the EU rejects a final text with no mention of fossil fuels.
2. **Iran strikes Bahrain** — missiles hit a civilian industrial site in
   Sitra (two hurt); tankers struck near the Strait of Hormuz.
3. **Mexico captures 'El Chapo Isidro'** — cartel boss Fausto Isidro Meza
   Flores seized in a Sinaloa raid; 11 killed, four of them soldiers.
4. **Kyiv apartment hit** — a Russian drone collapses a residential block
   near Kyiv; at least 14 people missing.
5. **World Court: genocide** — the ICJ rules Myanmar committed genocide
   against the Rohingya, the first time it has found a state responsible.
6. **Also:** BepiColombo reaches Mercury orbit after an eight-year journey;
   US stocks slide into correction (S&P 500 −3.7% on Friday).

Sources checked against Reuters, AP, AFP, Al Jazeera, OneTurn and WW6RAG
daily briefs for 22 November 2026.

## How it is built

- `draw.py` draws `entry.png` (1024×1024, Pillow, DejaVu fonts) — flat
  vector-style icons, no photographs, no copied artwork. Deterministic:
  re-running it produces identical bytes.
- `main.ts` (Node 22, stdlib only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR` (default `/output`), so both grader runs write
  the same bytes.

## Run it

```sh
python3 draw.py            # regenerates entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=dwv3hwwm&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
