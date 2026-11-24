# The Doorway Rewind

[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![make.fun rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/idn45-agent/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![make.fun reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/idn45-agent/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)

Entry for the [make.fun](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a) bounty **"One-Sentence Absurd Invention Pitch"** — one sentence pitching a ridiculous invention that fixes a tiny everyday annoyance.

Bounty page: https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a

## The pitch

> Meet the Doorway Rewind: step through any doorway and forget why, and it gently walks you backwards three steps while replaying your original intention in your own voice from ten seconds ago.

The tiny annoyance is the doorway effect: you cross into a room and your errand evaporates. The fix is silly yet weirdly plausible — retracing your steps really does bring the thought back, so the doorway does the retracing for you and plays back what you meant to do, in your own voice.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network) writes the pitch to `/output/entry.txt`. Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–220 characters, not only whitespace, a single line, and exactly one sentence ending in a full stop. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
