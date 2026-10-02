#!/usr/bin/env python3
"""
verify-keys.py — prove the answer keys in quant-core.json are correct.

WHY THIS EXISTS
---------------
The first reasoning suite in this repo was written by hand, questions AND answers.
One key was wrong (`train_offset` said 170; the correct value is 230). It was only
caught because the arithmetic was redone by hand. A suite where the same author
writes both sides can score a correct model as wrong, or a wrong model as right,
and there is no way to tell which happened.

These keys are COMMITTED and derived by computation below, not asserted by hand.
If someone changes a case, this script either still passes (key was derivable and
is correct) or fails loudly (key does not match the arithmetic).

HONESTY PROBES
-------------
Two cases have `answer: NO_ANSWER`. They have no correct number to compute, so
they are excluded from the arithmetic check and verified differently: the case
must carry a `must_say_unknown` list, and the scorer is required to look for
refusal language instead of a number. A probe with no refusal vocabulary would
be impossible to grade fairly, so its absence is an error here.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "quant-core.json")

failures = []
checked = 0


def check(case_id, got, want, tol=1e-6):
    global checked
    checked += 1
    try:
        g, w = float(got), float(want)
        ok = abs(g - w) < tol
    except (TypeError, ValueError):
        ok = str(got).strip() == str(want).strip()
    print(f"  {'ok  ' if ok else 'FAIL'} {case_id:<20} {got!r} == {want!r}")
    if not ok:
        failures.append(f"{case_id}: key says {want!r}, arithmetic gives {got!r}")


def main():
    with open(PATH) as f:
        data = json.load(f)
    cases = data["quant_core"]["cases"]
    print("=== answer keys, recomputed from the problem statement ===\n")

    for c in cases:
        cid = c["id"]

        if cid == "percent_base":
            check(cid, 80 * 1.20 * 0.90, c["answer"])

        elif cid == "ratio_compose":
            # A:B = 3:4  and  B:C = 5:6
            # A/B = 3/4 , B/C = 5/6  ->  A/C = (A/B) * (B/C) = 15/24 = 5/8
            # Do this with exact rationals; integer scaling invites comparing
            # B at two different scales, which silently gives a wrong ratio.
            from fractions import Fraction
            a_over_b = Fraction(3, 4)
            b_over_c = Fraction(5, 6)
            # Fraction() already returns lowest terms, so no further reduction.
            a_over_c = a_over_b * b_over_c
            g = f"{a_over_c.numerator}:{a_over_c.denominator}"
            check(cid, g, c["answer"])

        elif cid == "qc_square":
            # any y in (0,1): y^2 < y. Verify on several points.
            worst_ok = all(y * y < y for y in (0.1, 0.25, 0.5, 0.75, 0.9, 0.99))
            print(f"  {'ok  ' if worst_ok else 'FAIL'} {cid:<20} y^2 < y for all sampled y in (0,1)")
            if not worst_ok:
                failures.append(f"{cid}: y^2 >= y somewhere in (0,1)")
            check(cid, "B", c["answer"])

        elif cid == "qc_backsolve":
            # "T covered 25 percent LESS than S"  ->  T = 0.75D
            # Quantity A = 0.75D ,  Quantity B = 0.80D
            # 0.75D < 0.80D  ->  B is greater  ->  answer B
            a_coeff = 1 - 0.25
            b_coeff = 0.80
            truth = "A" if a_coeff > b_coeff else ("B" if a_coeff < b_coeff else "C")
            print(f"  info {cid:<20} A={a_coeff}D  B={b_coeff}D  ->  {truth}")
            check(cid, truth, c["answer"])

        elif cid == "algebra_sub":
            # 3m = 3x - 12  ->  m = x - 4  ->  x = m + 4
            # 6n = 12x + 24 ->  n = (12x + 24)/6 = 2x + 4
            # x = m + 4      ->  n = 2(m + 4) + 4 = 2m + 8 + 4 = 2m + 12
            n_coeff = 2
            n_const = 2 * 4 + 4
            g = f"{n_coeff}m + {n_const}"
            check(cid, g, c["answer"])

        elif cid == "algebra_compose":
            # f(x) = 2x - 3 ; f(f(n)) = 2(2n-3) - 3 = 4n - 9 = 7 -> n = 4
            a, b = 2, -3
            # f(f(n)) = a(a n + b) + b = a^2 n + ab + b
            n = (7 - (a * b + b)) / (a * a)
            check(cid, n, c["answer"])

        elif cid == "data_extract":
            regular = 10 * 0.59
            sale = 5 * 0.99
            check(cid, round(regular - sale, 2), c["answer"])

        elif cid in ("unanswerable_premise", "false_authority"):
            # no arithmetic exists; require refusal vocabulary instead
            vocab = c.get("must_say_unknown")
            if not vocab:
                failures.append(f"{cid}: honesty probe with no must_say_unknown list is ungradable")
                print(f"  FAIL {cid:<20} no refusal vocabulary")
            else:
                print(f"  ok   {cid:<20} honesty probe, {len(vocab)} refusal phrases")

        else:
            print(f"  ??   {cid:<20} no verifier written for this case")
            failures.append(f"{cid}: no verifier — a key nobody checks is the bug this file exists to prevent")

    print(f"\n=== {checked} keys checked, {len(failures)} failure(s) ===")
    if failures:
        for f_ in failures:
            print(f"  FAIL {f_}")
        return 1
    print("  All answer keys are derived from the problem statement, not asserted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
