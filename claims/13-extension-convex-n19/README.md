# 13-extension-convex-n19

**Problem variant:** convex — convex hull of the points, scaled to area 1; value = min triangle area / hull area
**n = 19**

**Value (verified, 30 digits): 0.0145273046042192686714260879552**

No published value exists for this case (published tables end at n=16);
submitted as a first 'best known' entry. Found by multistart basin-hopping
+ trust-region SLP maximization; less search time than classical entries.

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  33 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 19; triples checked: C(19,3) = 969 (asserted)
- exact value: 9684869736146177290305955323/666666666666666541111503268766
- minimal triangles (ties): 33
- feasible: yes (exact test, both verifiers)
