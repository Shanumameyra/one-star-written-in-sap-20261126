# NOTES — One Star, Written in Sap

- Bounty: One Star, Written in Sap (`u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4`)
- Prize: $2 total (1st $0.73, 2nd $0.50, 3rd $0.35, 4th $0.25, 5th $0.17)
- Deadline: 26 Nov 2026, 21:35 WIB (2026-11-26T14:35:00Z)
- opensAt: 2026-11-25T03:36:34Z (verified via API; session started after this)
- Fee: FREE — entryFeeUsd null, entryFeesUsd 0.00 (verified via API before building)
- submissionCount at build time: 2436
- Judge: pairwise AI judge (z-ai/glm-5.3-flash), top 500 dev-board entries go to the final heat; 3 Swiss rounds + top-7 playoff.

## Baseline / top-1 standard calibrated to

Blind competition (no public leaderboard of ranked lines; entries show in the
live feed only after grading). Calibrated to the judge brief in the kit:

1. A genuine one-line 1-star review by a houseplant about its human owner,
   grievance at the centre.
2. Funnier through a surprising turn / sharp plant's-eye grievance, not a
   cute idea alone.
3. Sounds like a houseplant wrote it (water, light, soil, pots, repotting).
4. Reads as a real review with a clear complaint and a reason for the star.
5. Fresh, specific detail; NO stock phrases about drama queens, dramatic
   wilting, or being ignored.

The visible feed example (another entrant's line, NOT copied) sets the bar:
a care-label joke ("bright indirect light, not slow cremation"). This entry
answers it with equally specific plant detail (flat cola watering, a novelty
mug with no drainage, the "low maintenance" lie) and a closing twist
("holding on by one leaf and a grudge").

## Entry

- `main.py` — deterministic, no network, no randomness; writes the line to
  `/output/entry.txt` (or argv[1], or `entry.txt` beside the script).
- `entry.txt` — the single line, 210 characters (211 incl. trailing newline),
  verified byte-for-byte identical to a fresh run of `main.py` in a clean
  directory.
- The line is original, authored for this bounty from the brief.
