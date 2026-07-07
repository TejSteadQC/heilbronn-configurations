# 03-exact-convex-n18

**Problem variant:** convex — convex hull of the points, scaled to area 1; value = min triangle area / hull area
**n = 18**

**Value (verified, 30 digits): 0.0182388954634908723600644432595**

No published value exists for this case (published tables end at n=16);
submitted as a first 'best known' entry. Found by multistart basin-hopping
+ trust-region SLP maximization; less search time than classical entries.

## Exact solution

This configuration is D6-symmetric (12 hull points at angles 60k±α on a
circle, 6 interior points on the mirror axes at radius q) and admits a
closed form. The value is the smallest real root of

    1944 v^3 - 648 v^2 + 66 v - 1 = 0

i.e. v = (2 - u)/18 where u = cbrt(3/2 + sqrt(717)/18) + cbrt(3/2 - sqrt(717)/18).
Parameters: q^2 = real root of 3u^3+11u^2+13u-3; tan^2(α) = real root of
81t^3+159t^2+139t-3. Derivation + 60-digit verification: exact.py.

## Files

- `coordinates.txt` — point coordinates (15 decimals), exactly feasible
- `images/` — Friedman-style renders; each image shows a maximal set of
  pairwise non-overlapping minimal-area triangles (together they cover all
  36 triangles attaining the minimum)
- `verify_output.json` — outputs of two independently-written exact verifiers
  (rational-arithmetic and integer-arithmetic; they agree bit-for-bit on the
  exact value fraction and feasibility of all points)

## Verification summary

- points: 18; triples checked: C(18,3) = 816 (asserted)
- exact value: 5211112989568819048894923327/285714285714285625167971022578
- minimal triangles (ties): 36
- feasible: yes (exact test, both verifiers)
