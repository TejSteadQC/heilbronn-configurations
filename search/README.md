# Search code

The optimization code that produced the configurations in `../claims/`.
Python 3, requires `numpy` and `scipy` (plus `mpmath` for `refine.py`-level
verification; the exact verifiers in `../verifiers/` are stdlib-only).

## Core

- **`heil.py`** — geometry and the local maximizer. The key routine is
  `polish(X, variant)`: trust-region successive linear programming on the
  nonsmooth maximin objective. At each step it solves the LP

  ```
  maximize t
  s.t.  area_ijk(X) + grad(area_ijk) . dX  >=  t   for ALL C(n,3) triples
        domain constraints on X + dX
        |dX| <= r   (component-wise trust region)
  ```

  re-fixing triangle orientations each outer round and shrinking `r` on
  failure. Because every triple shares the same floor variable `t`, the LP
  equalizes the active (minimal) triangles automatically — configurations
  converge to the KKT structure where dozens of triangle areas tie at the
  optimum. Variants: `square` ([0,1]^2), `triangle` (reference simplex,
  affine-invariant, value = 2*min area), `convex` (free points, value =
  min area / hull area, hull-area growth constrained via its linearization).

- **`search.py`** — single-stream multistart + basin-hopping driver, and the
  `TARGETS` table of published values used as calibration during development.

- **`attack.py`** — multiprocess basin-hopping "attack" on one `(variant, n)`
  case: 12 workers, each mixing global/subset Gaussian shakes, 1-2 point
  teleports, and occasional fresh restarts, all polished with `heil.polish`.

## Search strategies layered on top

- **`grow.py`** — seeds `n` from the best `n-1` configuration by point
  insertion (candidate positions scored before polishing) and from `n+1` by
  deletion. Cheap and surprisingly strong: several records came from this.
- **`sym.py`** — search restricted to cyclic rotation groups (`rot2`, `rot3`,
  ..., orbits plus optional fixed center), optimizing only the orbit
  representatives via the same SLP with a symmetry Jacobian, then re-polished
  in full space. This found the D6-symmetric convex n=18 configuration whose
  exact value is derived in `../claims/03-exact-convex-n18/exact.py`.
- **`mirror.py`** — same idea for a single reflection axis (k point-pairs +
  points on the axis); covers n where cyclic groups fit awkwardly.
- **`refine.py`** — repeated shrinking-trust-region polish to push a
  configuration to ~1e-15 convergence before exact verification.
- **`consensus.py`** — the campaign driver used for n >= 21: independent
  discovery streams (fresh / boundary-biased / grow-seeded starts) run in
  parallel with confirmation streams that restart from a strongly scrambled
  champion (3-5 points teleported); a case stops only when 3 confirmation
  streams independently climb back to the champion value, and any stream that
  beats the champion voids all votes. Wall-clock cost per case is recorded in
  a `timings.json` ledger.

## Workflow that produced the claims

1. Multistart/attack until a case stops improving (`attack.py`).
2. Structural moves: grow seeding, symmetric and mirror searches.
3. `refine.py` to full convergence, exact-feasibility repair (points nudged
   onto/inside the boundary at the ulp level).
4. Exact verification with the two independent verifiers in `../verifiers/`.
5. For symmetric solutions, exactification: identify the orbits of tied
   triangles, impose equal areas symbolically, eliminate (Groebner basis) —
   see the convex n=18 claim.

Historical note: the records for n <= 16 on Friedman's pages were found with
simulated annealing (Comellas-Yebra 2002), metaheuristics (Karpov's Ascension),
and LLM-evolved programs (AlphaEvolve 2025); the SLP-equalization approach here
is closest in spirit to Comellas-Yebra's local refinement, applied as the inner
loop of every search rather than as a final step.
