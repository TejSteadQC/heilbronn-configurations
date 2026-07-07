"""Exact (analytic) solution for the convex-region Heilbronn configuration, n=18.

Structure (found numerically by sym.py rot6 search, then exactified):
  - 6-fold dihedral symmetry (D6): six mirror axes at 60-degree spacing.
  - 12 hull points on a circle of radius 1 at angles (60k +/- alpha) degrees.
  - 6 interior points on the mirror axes at radius q.
  - Convex hull = semiregular 12-gon; value = min triangle area / hull area.

Three orbits of simultaneously-minimal triangles (36 total of C(18,3)=816):
  A (HHH): hull points at 0+alpha, 60-alpha, 60+alpha    -> 2*area = s(c - sqrt3 s)
  B (HHI): hull at 0+alpha, 120+alpha, interior on 60    -> 2*area = sqrt3(1-2cq)/2
  C (HII): hull at 0+alpha, interiors on 60 and 120      -> 2*area = q(sqrt3 q - 2s)/2
  (c = cos alpha, s = sin alpha)

Equal-area conditions A=B=C plus c^2+s^2=1 give (Groebner elimination):
  q^2      : real root of  3u^3 + 11u^2 + 13u - 3 = 0     (q ~ 0.4431557245728759)
  tan^2 a  : real root of  81t^3 + 159t^2 + 139t - 3 = 0  (alpha ~ 8.2589907298 deg)
  VALUE    : smallest real root of  1944 v^3 - 648 v^2 + 66 v - 1 = 0

Cardano form:  v = (2 - u)/18  where  u = cbrt(3/2 + sqrt(717)/18)
                                        + cbrt(3/2 - sqrt(717)/18)   (u^3 = u + 3)
  v = 0.0182388954634910572362139010433579...

This script re-derives and verifies everything; run it to confirm.
"""

import itertools
import mpmath as mp
import sympy as sp


def derive():
    c, s, q, w, v = sp.symbols('c s q w v')
    A = s * (c - w * s)
    B = w * (1 - 2 * c * q) / 2
    C = q * (w * q - 2 * s) / 2
    H = 3 * (s * c + (w / sp.Integer(2)) * (c ** 2 - s ** 2))  # hull area
    system = [sp.expand(A - B), sp.expand(B - C), c ** 2 + s ** 2 - 1,
              w ** 2 - 3, sp.expand(2 * H * v - A)]
    G = sp.groebner(system, q, c, s, w, v, order='lex')
    uni = [p for p in G.exprs if p.free_symbols <= {v}]
    assert any(sp.factor(p).has(1944 * v ** 3 - 648 * v ** 2 + 66 * v - 1)
               for p in uni), uni
    return uni


def verify(dps=60):
    mp.mp.dps = dps
    q = mp.sqrt(mp.findroot(lambda u: 3 * u ** 3 + 11 * u ** 2 + 13 * u - 3,
                            mp.mpf("0.196")))
    alpha = mp.atan(mp.sqrt(mp.findroot(
        lambda u: 81 * u ** 3 + 159 * u ** 2 + 139 * u - 3, mp.mpf("0.021"))))
    pts = []
    for k in range(6):
        ax = mp.pi * k / 3
        pts.append((mp.cos(ax + alpha), mp.sin(ax + alpha)))
        pts.append((mp.cos(ax - alpha), mp.sin(ax - alpha)))
        pts.append((q * mp.cos(ax), q * mp.sin(ax)))
    mn = min(abs((Q[0] - P[0]) * (S[1] - P[1]) - (S[0] - P[0]) * (Q[1] - P[1]))
             for P, Q, S in itertools.combinations(pts, 3))
    hullA = 3 * (mp.sin(2 * alpha) + mp.sin(mp.pi / 3 - 2 * alpha))
    val = (mn / 2) / hullA
    vroot = mp.findroot(lambda x: 1944 * x ** 3 - 648 * x ** 2 + 66 * x - 1,
                        mp.mpf("0.0182389"))
    cardano = (2 - (mp.cbrt(mp.mpf(3) / 2 + mp.sqrt(717) / 18)
                    + mp.cbrt(mp.mpf(3) / 2 - mp.sqrt(717) / 18))) / 18
    assert abs(val - vroot) < mp.mpf(10) ** (5 - dps), (val, vroot)
    assert abs(val - cardano) < mp.mpf(10) ** (5 - dps), (val, cardano)
    return val


if __name__ == "__main__":
    print("Groebner basis check...", end=" ")
    derive()
    print("ok")
    v = verify()
    print(f"verified at 60 dps: A18(convex) = {mp.nstr(v, 40)}")
    print("minimal polynomial: 1944 v^3 - 648 v^2 + 66 v - 1 = 0")
