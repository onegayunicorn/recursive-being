"""
SO(5) / so(5) Lie algebra utilities

- dim SO(n) = n(n-1)/2  →  dim SO(5) = 10
- so(5) = skew-symmetric 5×5 real matrices (10 independent generators)
- Rank 2; odd dimension ⇒ every real skew-symmetric matrix has det 0 (zero mode)
- Stack usage: exact propagator U = exp((A_base + A_corr + A_EMI) dt) ∈ SO(5)

Mirrors logic in 5D-Manifold-Evolution/src/lib/matrixMath.ts
"""

from __future__ import annotations

from typing import List

Mat5 = List[List[float]]
Vec5 = List[float]


def dim_so_n(n: int) -> int:
    return n * (n - 1) // 2


def zeros5() -> Mat5:
    return [[0.0] * 5 for _ in range(5)]


def identity5() -> Mat5:
    M = zeros5()
    for i in range(5):
        M[i][i] = 1.0
    return M


def J(a: int, b: int) -> Mat5:
    """Elementary plane rotation generator J_ab (0-indexed), skew-symmetric."""
    M = zeros5()
    M[a][b] = -1.0
    M[b][a] = 1.0
    return M


def frobenius(A: Mat5) -> float:
    s = 0.0
    for i in range(5):
        for j in range(5):
            s += A[i][j] * A[i][j]
    return s ** 0.5


def mat_add(A: Mat5, B: Mat5) -> Mat5:
    C = zeros5()
    for i in range(5):
        for j in range(5):
            C[i][j] = A[i][j] + B[i][j]
    return C


def mat_scale(A: Mat5, s: float) -> Mat5:
    C = zeros5()
    for i in range(5):
        for j in range(5):
            C[i][j] = A[i][j] * s
    return C


def is_skew(A: Mat5, tol: float = 1e-12) -> bool:
    for i in range(5):
        for j in range(5):
            if abs(A[i][j] + A[j][i]) > tol:
                return False
    return True


class SO5Algebra:
    """Lightweight so(5) generator toolkit for the Recursive stack."""

    DIM = 10  # dim so(5)
    RANK = 2

    def __init__(self):
        self.basis = self._standard_basis()

    def _standard_basis(self) -> List[Mat5]:
        gens = []
        for a in range(5):
            for b in range(a + 1, 5):
                gens.append(J(a, b))
        return gens  # exactly 10

    def verify_basis(self) -> dict:
        return {
            "count": len(self.basis),
            "expected": self.DIM,
            "all_skew": all(is_skew(G) for G in self.basis),
            "dim_so5": dim_so_n(5),
            "rank": self.RANK,
            "note": "Odd n ⇒ det(A)=0 for any real skew A ∈ so(n); zero mode always exists",
        }

    def status(self) -> dict:
        return {
            "group": "SO(5)",
            "algebra": "so(5)",
            "dimension": self.DIM,
            "rank": self.RANK,
            "basis_ok": self.verify_basis(),
            "stack_use": "U = exp((A_base + A_corr + A_EMI) * dt) preserves S^4 state norm",
        }


if __name__ == "__main__":
    alg = SO5Algebra()
    print(alg.status())
