# 02-record-convex-n15

**Problem variant:** convex — convex hull of the points, scaled to area 1; value = min triangle area / hull area
**n = 15**

**Value (verified, 30 digits): 0.0245640556132301679615750232227**

**Previous best:** .0244+ (worst-case ceiling 0.0245)
  (D. Cantrell, June 2007 (erich-friedman.github.io/packing/heilconvex/, 4-digit value only))

This is a claimed improvement over the published record configuration
(different point arrangement, not a numerical polish of the old one).

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  25 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 15; triples checked: C(15,3) = 455 (asserted)
- exact value: 49128111226460317685888607941/1999999999999999257563094398721
- minimal triangles (ties): 25
- feasible: yes (exact test, both verifiers)
