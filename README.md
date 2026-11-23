[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/peeranky-alt/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/peeranky-alt/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

# The World in One Day — Sunday 22 November 2026

Entry for make.fun competition `news-image-20261122`: one image that sums up the
world news of Sunday 22 November 2026.

## The image (dense edition)

A one-day briefing drawn programmatically (PIL) so every letter is crisp:
a lead story plus a 4×8 grid of 32 more — **33 stories across 9 regions
and fields**, every one reported on 22 November 2026 (checked against live
news sources that day: Al Jazeera, Reuters, CNN, The Hindu, Daily Summary Of,
GameSpot, Space.com, The Rio Times).

- **Lead — Democrats take the House:** at least 258 seats, the largest
  majority since 1992, after Chuck Hubbard beats Virginia Foxx in North
  Carolina on a recount; Foxx concedes.
- **North America —** Trump tells federal contractors to check with the
  White House before answering Congress; GTA 6 sees 40.8m players on
  Sunday; the 49ers beat the Vikings 35-10 in Mexico City; a teen gamer
  helps the FBI rescue a missing girl; a special team is set up to stop
  air-traffic outages before Thanksgiving.
- **South America —** Bolsonaro in intensive care with an intestinal
  obstruction; Boca Juniors win the Sudamericana 2-0; a Nicaraguan
  revolution commander dies at 86.
- **Europe —** Liverpool hammer Manchester United 4-0 on Pochettino's
  debut; cost-of-living protests enter a third day; Finland says the war
  is spilling over after a drone hits a Russian cargo ship; a former
  Italian police chief is found dead amid a Sicily bombing inquiry;
  Theresa May tells her successor to 'move on' from Brexit.
- **Middle East —** two supertankers hit mines off Hormuz; COP31 ends
  without a deal; a drone hits the Russian warship Merkury off Libya;
  drones kill 4 near Khartoum and damage a UN building; Houthis claim a
  Saudi refinery hit; Zelenskyy urges the US to release Patriot missiles;
  settlers burn vehicles in the West Bank.
- **Africa —** blast at a Benghazi naval base ammunition depot; a boat
  capsize in Nigeria kills 29 mourners; Tinubu orders an end to a
  Katsina party feud.
- **Asia —** factory fire in Banten, Indonesia leaves 36 missing; Nepal's
  PM arrives in Delhi; India and China hold border talks; Iran unveils a
  dual-missile launcher; Myanmar calls an ASEAN review 'unfair'.
- **Oceania —** former NSW politician Fred Nile dies aged 92.
- **Science —** SpaceX sets a same-pad launch turnaround record (two
  launches in 32 hours); China targets Moon ice by 2030; NASA lets AI
  plan Mars rover drives, with humans verifying.

## How it runs

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It runs with no network and writes identical bytes on every
run:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the entry image (1024×1024 PNG)
- `main.py` — the program that writes it to `/output/entry.png`
- `LICENSE` — MIT
