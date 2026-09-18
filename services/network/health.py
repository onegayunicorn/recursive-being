"""
Local health / readiness endpoints (stdlib only).

Can be mounted behind Flask/FastAPI in sovereign-devengine;
standalone for tests and Termux.
"""

from __future__ import annotations

from src.phoenix.seed import PhoenixSeed, COHERENCE_TARGET, SCHUMANN, PHI
from src.metrics.schumann import SchumannMetrics
from src.metrics.so5 import SO5Algebra


def health_payload() -> dict:
    seed = PhoenixSeed()
    return {
        "status": "ok",
        "service": "recursive-being",
        "phoenix": seed.status(),
        "constants": {
            "schumann_hz": SCHUMANN,
            "phi": PHI,
            "coherence_target": COHERENCE_TARGET,
        },
        "schumann": SchumannMetrics().status(),
        "so5": SO5Algebra().verify_basis(),
    }


def readiness_payload(sovereign_ready: bool = False) -> dict:
    return {
        "ready": sovereign_ready,
        "checks": {
            "fold_entry": True,
            "schumann_anchor": True,
            "so5_basis": SO5Algebra().verify_basis()["all_skew"],
        },
    }


if __name__ == "__main__":
    import json
    print(json.dumps(health_payload(), indent=2))
