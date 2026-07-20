# Heilbronn configurations: new records and n=17–20 extensions

New best-known point configurations for the three Heilbronn-type problems tracked on
[Erich Friedman's Packing Center](https://erich-friedman.github.io/packing/):

- [Heilbronn in a square](https://erich-friedman.github.io/packing/heilbronn/) —
  n points in a unit square, maximize the smallest triangle area
- [Heilbronn in a triangle](https://erich-friedman.github.io/packing/heiltri/) —
  same, in a unit-area triangle (affine-invariant)
- [Heilbronn in a convex region](https://erich-friedman.github.io/packing/heilconvex/) —
  same, over all unit-area convex regions (the region is the hull of the points)

Configurations were found by multistart basin-hopping over a trust-region
successive-LP local maximizer (with symmetry-restricted searches and point
insertion/deletion moves), then verified exactly.

## Summary of claims

### Improved records (n ≤ 16)

| problem | n | new value | previous best |
|---|---|---|---|
| triangle | 13 | **0.0265565…** | 0.0265013 (P. Karpov, 2015) |
| convex | 15 | **0.0245640…** | .0244+ (D. Cantrell, 2007) |

Both are new point arrangements, not refinements of the previous configurations.

### Exact solution

The convex n=18 configuration (D6-symmetric: 12 hull points on a circle at angles
60°k ± α, 6 interior points on the mirror axes at radius q) has the closed form

```
A18 = smallest real root of 1944 v³ − 648 v² + 66 v − 1
    = (2 − u)/18,  u = ∛(3/2 + √717/18) + ∛(3/2 − √717/18)
    = 0.0182388954634910572…
```

Derivation and 60-digit verification: [`claims/03-exact-convex-n18/exact.py`](claims/03-exact-convex-n18/exact.py).

### First entries for n = 17–20

No values for n > 16 appear to have been published for any of the three problems.
These are "best known" first entries (they have received far less search time than
the classical range and can very likely be improved):

| n | square | triangle | convex |
|---|---|---|---|
| 17 | 0.0164812 | 0.0155174 | 0.0187315 |
| 18 | 0.0144327 | 0.0133935 | 0.0182389 (exact) |
| 19 | 0.0126774 | 0.0111615 | 0.0145273 |
| 20 | 0.0108560 | 0.0101084 | 0.0132669 |

## Repository layout

Each claim is a self-contained folder under [`claims/`](claims/README.md):

```
claims/NN-type-variant-nK/
  README.md            the claim: value, previous best, verification summary
  coordinates.txt      15-decimal coordinates, exactly feasible
  images/              one image per set of pairwise non-overlapping minimal triangles
  verify_output.json   outputs of the two independent verifiers below
  exact.py             (convex n=18 only) symbolic derivation + verification
```

The optimization code that found these configurations is in
[`search/`](search/README.md) (trust-region successive-LP local maximizer,
multistart basin-hopping, symmetry-restricted searches; numpy/scipy).

## Verification

Every coordinate file was checked by **two independently written verifiers**
([`verifiers/verify_a.py`](verifiers/verify_a.py),
[`verifiers/verify_b.py`](verifiers/verify_b.py)) — written in a clean-room setting
against the problem statement only, one using exact rational arithmetic
(`fractions.Fraction`), the other exact scaled-integer arithmetic. Both:

- parse coordinates as exact decimals (no floating point),
- enumerate all C(n,3) triples (count asserted),
- compute areas by the shoelace formula exactly,
- test domain feasibility exactly (closed domains),
- for the convex variant, compute the hull and its area exactly.

They agree bit-for-bit on the exact value fraction of every configuration, and all
points are exactly inside their domains. To re-verify any claim:

```
python3 verifiers/verify_a.py triangle claims/01-record-triangle-n13/coordinates.txt
python3 verifiers/verify_b.py triangle claims/01-record-triangle-n13/coordinates.txt
```

(`VARIANT` is `square`, `triangle` — the reference triangle (0,0),(1,0),(0,1) with
value = 2·min area — or `convex`.)

## Notes

- The triangle and convex pages' n=11 / n=13,14 entries were improved by AlphaEvolve
  (DeepMind, 2025; [results notebook](https://github.com/google-deepmind/alphaevolve_results));
  the comparisons above are against the strongest published values, not only the
  Packing Center tables.
- Values are lower bounds on the respective optima; none of the new entries are
  claimed optimal.
