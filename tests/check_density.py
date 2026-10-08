"""Machine assertions for aigc-humanizer tests/cases.json (mechanical red lines only).

Checks per case:
  1. numbers_preserved: every listed token appears verbatim in rewritten text
  2. terms_preserved:   every listed term appears verbatim in rewritten text
  3. "de" density of rewritten text within normal range [0.04, 0.09]
     (v1.4.8 rule: 0.045~0.065 is the optimal band; this script asserts the
      wider normal band — FAIL below 0.04, matching the rule "must top up
      below 0.04". Optimal-band guidance lives in rules/rewrite-rules.md.)
     density = count of U+7684 / non-whitespace char count (punctuation included)
  4. structure markers like "(1)" "(3)" carried over from input to rewritten

Wording is intentionally NOT asserted (open-ended); red lines are fixed.
Usage: python check_density.py   -> exit 0 all green, exit 1 on any failure
"""

import json
import re
import sys
from pathlib import Path

BASE = Path(__file__).parent
DE = "\u7684"  # the particle "de"
# v1.4.8: normal band widened from [0.05, 0.09] to [0.04, 0.09].
# Rule optimum is 0.045~0.065; below 0.04 the rule demands top-up (see
# rules/rewrite-rules.md 手法一). Script asserts the wider normal band only.
RANGE = (0.04, 0.09)


def density(text: str) -> float:
    t = re.sub(r"\s", "", text)
    if not t:
        return 0.0
    return t.count(DE) / len(t)


def run() -> int:
    cases = json.loads((BASE / "cases.json").read_text(encoding="utf-8"))
    total = 0
    fails = 0
    for c in cases["cases"]:
        cid = c["id"]
        rw = c["rewritten"]

        for tok in c.get("assert", {}).get("numbers_preserved", []):
            total += 1
            if tok not in rw:
                fails += 1
                print(f"[FAIL] {cid}: number lost: {tok}")

        for tok in c.get("assert", {}).get("terms_preserved", []):
            total += 1
            if tok not in rw:
                fails += 1
                print(f"[FAIL] {cid}: term lost: {tok}")

        d = density(rw)
        total += 1
        if RANGE[0] <= d <= RANGE[1]:
            print(f"[ ok ] {cid}: density {d:.4f} in [{RANGE[0]}, {RANGE[1]}]")
        else:
            fails += 1
            print(f"[FAIL] {cid}: density {d:.4f} out of [{RANGE[0]}, {RANGE[1]}]")

        for m in re.findall(r"\(\d+\)", c["input"]):
            total += 1
            if m not in rw:
                fails += 1
                print(f"[FAIL] {cid}: structure marker lost: {m}")

    print(f"\n{total - fails}/{total} assertions passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(run())
