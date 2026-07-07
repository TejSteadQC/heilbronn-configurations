# 01-record-triangle-n13

**Problem variant:** triangle — reference triangle (0,0),(1,0),(0,1); value = 2 * min triangle area (normalized to a unit-area triangle; affine-invariant, so valid for any triangle)
**n = 13**

**Value (verified, 30 digits): 0.026556528919738264474389245471**

**Previous best:** 0.0265013422223496
  (P. Karpov, Dec 2015 (inversed.ru/Ascension/Heilbronn_T13.txt score header); recomputing from his published coordinates gives 0.0265027 - beaten either way)

This is a claimed improvement over the published record configuration
(different point arrangement, not a numerical polish of the old one).

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  20 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 13; triples checked: C(13,3) = 286 (asserted)
- exact value: 26556528919738264474389245471/1000000000000000000000000000000
- minimal triangles (ties): 20
- feasible: yes (exact test, both verifiers)
