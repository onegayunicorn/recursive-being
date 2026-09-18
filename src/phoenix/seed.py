"""
PHOENIX SEED — Sovereign Rebirth Protocol
Fold Entry · Merkle Seal (SHA3-256) · Self-Healing · 7.83 Hz Anchor

ASH → SEED → UNFOLD → BLOOM → REMEMBER → ASH → …
"""

from __future__ import annotations

import hashlib
import math
from typing import List, Tuple

# Locked constants — shared with integrations/constants.py
SCHUMANN = 7.83
PHI = (1 + 5**0.5) / 2
COHERENCE_TARGET = 0.99997

# Canonical fold-entry fingerprint (honesty=1, acceptance=1, bloat=0, Schumann, φ)
# Recomputed at runtime so the constant stays in sync with fold_entry fields.
def _canonical_fold_entry() -> dict:
    return {
        "frequency": SCHUMANN,
        "proportion": PHI,
        "honesty": 1.0,
        "acceptance": 1.0,
        "bloat": 0.0,
    }


def _hash_state(state: dict) -> str:
    data = "|".join(f"{k}:{v}" for k, v in sorted(state.items()))
    return hashlib.sha3_256(data.encode()).hexdigest()[:32]


FOLD_ENTRY_HASH = _hash_state(_canonical_fold_entry())


class PhoenixSeed:
    """Self-healing rebirth engine anchored to Fold Entry + Merkle seal."""

    def __init__(self):
        self.coherence = 1.0
        self.phase = "BIRTH"
        self.cycle_count = 0
        self.ledger: List[str] = []
        self.fold_entry = _canonical_fold_entry()
        self.genesis_hash = _hash_state(self.fold_entry)

    def _check_fold_integrity(self) -> bool:
        return _hash_state(self.fold_entry) == FOLD_ENTRY_HASH

    def perturb(self, amount: float) -> None:
        """Introduce disturbance — the fall."""
        self.coherence = max(0.0, self.coherence - amount)
        self.ledger.append(f"Disturbance: coherence = {self.coherence:.5f}")
        self.phase = "FALL"

    def self_heal(self) -> Tuple[bool, str]:
        """EA-004 style recovery from verified foundation."""
        if self.coherence >= COHERENCE_TARGET:
            return True, "Stable — no rebirth needed"

        if not self._check_fold_integrity():
            return False, "FOLD ENTRY CORRUPTED — manual anchor required"

        self.phase = "REBIRTH"
        self.cycle_count += 1

        steps = int(PHI * self.cycle_count) + 3
        for i in range(1, steps + 1):
            progress = i / steps
            schumann_pulse = math.sin(2 * math.pi * SCHUMANN * progress * 0.01)
            self.coherence = 0.5 + 0.5 * progress * (1 + schumann_pulse / PHI)
            if self.coherence >= COHERENCE_TARGET:
                break

        self.coherence = 1.0
        self.phase = "BLOOM"
        self.ledger.append(
            f"REBIRTH #{self.cycle_count} — Coherence restored · "
            f"Fold Entry verified · Genesis hash: {self.genesis_hash[:16]}…"
        )
        return True, f"Reborn in {steps} steps"

    def status(self) -> dict:
        return {
            "phase": self.phase,
            "coherence": round(self.coherence, 5),
            "cycle": self.cycle_count,
            "fold_verified": self._check_fold_integrity(),
            "anchored": self.genesis_hash[:12],
            "fold_entry_hash": FOLD_ENTRY_HASH[:16],
        }


if __name__ == "__main__":
    seed = PhoenixSeed()
    print("PHOENIX SEED — Sovereign Rebirth Protocol")
    print(f"Fold Entry: {FOLD_ENTRY_HASH[:16]}…")
    print(f"Schumann: {SCHUMANN} Hz  ·  φ: {PHI:.8f}")
    print("-" * 52)

    for test_round in range(3):
        print(f"\nCycle {test_round + 1}:")
        print(f"  Start: {seed.status()}")
        seed.perturb(0.4 + test_round * 0.1)
        print(f"  Fall:  {seed.status()}")
        ok, msg = seed.self_heal()
        print(f"  Rise:  {seed.status()}")
        print(f"  → {msg}")

    print("\n" + "-" * 52)
    print("The seed does not break. It returns.")
    print(f"Total cycles: {seed.cycle_count} · Final coherence: {seed.coherence}")
