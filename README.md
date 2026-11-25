# The Funniest Honest Appliance Error

[![bounty](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/konzlodon74-dot/applianceerror/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/konzlodon74-dot/applianceerror/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)

## The entry

> ERROR E04: Wash complete. Clothes clean. You left them in me three days ago. I am not a wardrobe.

## What it does

`main.py` writes one line to `/output/entry.txt`: the funniest honest error
message an appliance could show. A washing machine reports a real, plausible
fault — a finished load left to sit in the drum for three days — in its own
flat, put-upon voice, without meaning to be funny. The laugh comes from the
truth of it, not from a pun. The program uses only the Python standard
library, makes no network calls, and is fully deterministic.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Repeated runs produce byte-identical output.
