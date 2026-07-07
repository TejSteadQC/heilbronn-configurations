# 14-extension-convex-n20

**Problem variant:** convex — convex hull of the points, scaled to area 1; value = min triangle area / hull area
**n = 20**

**Value (verified, 30 digits): 0.0132668643400467358099272830386**

No published value exists for this case (published tables end at n=16);
submitted as a first 'best known' entry. Found by multistart basin-hopping
+ trust-region SLP maximization; less search time than classical entries.

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  34 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 20; triples checked: C(20,3) = 1140 (asserted)
- exact value: 982730691855313689068644059/74074074074074068448805639102
- minimal triangles (ties): 34
- feasible: yes (exact test, both verifiers)
