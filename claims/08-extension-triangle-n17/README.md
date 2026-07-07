# 08-extension-triangle-n17

**Problem variant:** triangle — reference triangle (0,0),(1,0),(0,1); value = 2 * min triangle area (normalized to a unit-area triangle; affine-invariant, so valid for any triangle)
**n = 17**

**Value (verified, 30 digits): 0.01551737283161423500000783318**

No published value exists for this case (published tables end at n=16);
submitted as a first 'best known' entry. Found by multistart basin-hopping
+ trust-region SLP maximization; less search time than classical entries.

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  28 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 17; triples checked: C(17,3) = 680 (asserted)
- exact value: 775868641580711750000391659/50000000000000000000000000000
- minimal triangles (ties): 28
- feasible: yes (exact test, both verifiers)
