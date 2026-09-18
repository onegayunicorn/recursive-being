"""
Phoenix pipeline: ASH → SEED → UNFOLD → BLOOM → REMEMBER

Orchestrates Fold Entry verification, optional manifold sync, and ledger entry.
"""

from __future__ import annotations

from src.phoenix.seed import PhoenixSeed, COHERENCE_TARGET


def run_phoenix_cycle(disturbance: float = 0.35) -> dict:
    seed = PhoenixSeed()
    before = seed.status()
    seed.perturb(disturbance)
    after_fall = seed.status()
    ok, msg = seed.self_heal()
    after = seed.status()
    return {
        "ok": ok,
        "message": msg,
        "before": before,
        "after_fall": after_fall,
        "after": after,
        "target": COHERENCE_TARGET,
        "ledger": seed.ledger,
    }


if __name__ == "__main__":
    result = run_phoenix_cycle()
    print(result)
