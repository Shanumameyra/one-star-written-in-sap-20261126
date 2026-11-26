# One Star, Written in Sap

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/Shanumameyra/one-star-written-in-sap-20261126/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/Shanumameyra/one-star-written-in-sap-20261126/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

A make.fun entry for **One Star, Written in Sap** ($2): a single one-line
1-star review, written in the voice of a houseplant reviewing its human
owner.

## The line

> ★☆☆☆☆ One star. He watered me with flat cola, repotted me into a novelty mug with no drainage, and tells guests I'm 'low maintenance'. I am not low maintenance — I am a fern holding on by one leaf and a grudge.

210 characters, one line, no stock phrases — a sharp, specific plant's-eye
grievance (flat cola, a novelty mug with no drainage, the "low maintenance"
lie) with a surprising closing turn.

## How it works

`main.py` is deterministic: no network, no randomness, no time dependence.
It writes the single line to the output file (`/output/entry.txt` when the
harness mounts `/output`, an explicit path argument, or `entry.txt` beside
the script otherwise).

```sh
python3 main.py            # writes entry.txt
python3 main.py out.txt    # writes to out.txt
```

## License

MIT — see [LICENSE](LICENSE).
