# Glimmerwick: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/nemesisbug/glimmerwick-forecast/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![Reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/nemesisbug/glimmerwick-forecast/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the make.fun bounty **Charm the Commuter: Forecast a City That Isn't** — one line of weather, at most 140 characters, for a city that does not exist, judged by a bored commuter at a rainy bus stop.

## The forecast

> Glimmerwick: drizzle until 10, then sun — the 8:04 train is on time, the pigeons are smug, and your umbrella finally gets the day off.

134 characters. The line keeps the register of a real broadcast forecast — city named, weather first, times given — then bends it: in Glimmerwick the rare event worth forecasting is not the rain clearing, it is the 8:04 actually arriving on time, the pigeons noticing, and the umbrella earning a day off. One concrete place, one small joke, one smile for the commuter reading it on their phone.

## How it runs

`main.py` (Python 3, standard library only, no network, deterministic) writes the forecast verbatim to `/output/entry.txt` and asserts the 1–140 character gate before writing.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
