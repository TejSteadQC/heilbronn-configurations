# 06-extension-square-n19

**Problem variant:** square — unit square [0,1]^2; value = min triangle area
**n = 19**

**Value (verified, 30 digits): 0.012677395800094596388392533392**

No published value exists for this case (published tables end at n=16);
submitted as a first 'best known' entry. Found by multistart basin-hopping
+ trust-region SLP maximization; less search time than classical entries.

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  32 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 19; triples checked: C(19,3) = 969 (asserted)
- exact value: 792337237505912274274533337/62500000000000000000000000000
- minimal triangles (ties): 32
- feasible: yes (exact test, both verifiers)
