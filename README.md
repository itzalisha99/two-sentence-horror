# Two-Sentence Horror

[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![Rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/itzalisha99/two-sentence-horror/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![Reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/itzalisha99/two-sentence-horror/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)

A make.fun entry for **Two-Sentence Horror**: the scariest horror story in exactly two sentences, up to 400 characters.

## The story

> My mother squeezed my hand just before she passed. I was holding her right hand — the one the stroke had paralysed.

## Why it should win

- The first sentence reads as a tender deathbed moment.
- The second sentence turns it: the hand that squeezed could not move — so something else was in the room, holding on.
- The horror is implied, never explained; the reader fills in the worst of it.
- Precise and concrete: one hand, one stroke, one impossible squeeze. Every word earns its place.
- 115 characters, exactly two sentences — short, which also helps the byte tie-break.

## How it works

`main.py` (Python stdlib only, deterministic) validates the story against the bounty gate first — 1–400 characters, exactly two sentences, UTF-8, not only whitespace — then writes it to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
