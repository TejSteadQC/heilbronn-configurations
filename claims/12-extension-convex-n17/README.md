# 12-extension-convex-n17

**Problem variant:** convex — convex hull of the points, scaled to area 1; value = min triangle area / hull area
**n = 17**

**Value (verified, 30 digits): 0.0187314546401800889017165631159**

No published value exists for this case (published tables end at n=16);
submitted as a first 'best known' entry. Found by multistart basin-hopping
+ trust-region SLP maximization; less search time than classical entries.

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  29 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 17; triples checked: C(17,3) = 680 (asserted)
- exact value: 37462909280360195756099916031/2000000000000000958423525276547
- minimal triangles (ties): 29
- feasible: yes (exact test, both verifiers)
