# 05-extension-square-n18

**Problem variant:** square — unit square [0,1]^2; value = min triangle area
**n = 18**

**Value (verified, 30 digits): 0.0144326564130846427223793085775**

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

- points: 18; triples checked: C(18,3) = 816 (asserted)
- exact value: 5773062565233857088951723431/400000000000000000000000000000
- minimal triangles (ties): 29
- feasible: yes (exact test, both verifiers)
