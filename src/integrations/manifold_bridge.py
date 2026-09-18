"""
Bridge: Recursive Architect ↔ 5D-Manifold-Evolution

Maps SO(5) PhotonicEngine metrics into TYRONE Ω engines
so coherence, equilibrium, and pulse stay synchronized.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from .constants import SCHUMANN_HZ, PHI, PHI5


@dataclass
class ManifoldSnapshot:
    """Minimal snapshot of 5D PhotonicEngine state."""
    t: float = 0.0
    state: List[float] = field(default_factory=lambda: [0.4472] * 5)  # 1/√5
    phase: float = 0.0
    bio_growth: float = 1.0
    e_field: float = 0.0
    schumann_mod: float = 1.0
    system_coherence: float = 0.692
    coherence_retention_pct: float = 100.0
    bio_field_strength: float = 495.0
    feedback_active: bool = True
    feedback_norm: float = 0.0


class ManifoldBridge:
    """
    Translates 5D manifold telemetry into Recursive Architect language.

    Usage (when 5D engine is running in another process / notebook):
        bridge = ManifoldBridge()
        bridge.ingest(snapshot_from_ts)
        print(bridge.to_middle_flow())
        print(bridge.to_coherence())
        print(bridge.to_volition())
    """

    def __init__(self):
        self.latest: Optional[ManifoldSnapshot] = None

    def ingest(self, snap: ManifoldSnapshot | dict):
        if isinstance(snap, dict):
            self.latest = ManifoldSnapshot(**{k: v for k, v in snap.items() if k in ManifoldSnapshot.__dataclass_fields__})
        else:
            self.latest = snap
        return self.latest

    def to_middle_flow(self) -> dict:
        """Map coherence → equilibrium-style metric for Middle Flow Engine."""
        if not self.latest:
            return {"equilibrium": 0.0, "balance_pct": 50.0, "source": "idle"}
        # Higher coherence → closer to equilibrium (lower difference)
        coh = self.latest.system_coherence
        equilibrium = round(1.0 - coh, 4)  # 0 = perfect balance
        balance_pct = round(coh * 100, 1)
        return {
            "equilibrium": equilibrium,
            "balance_pct": balance_pct,
            "schumann_mod": self.latest.schumann_mod,
            "source": "5D-Manifold",
        }

    def to_coherence(self) -> dict:
        """Feed Coherence Multiplier from manifold retention metrics."""
        if not self.latest:
            return {"coherence": 0.0, "source": "idle"}
        # Use channel 0 and channel 4 as the two entities side-by-side
        a = abs(self.latest.state[0])
        b = abs(self.latest.state[4])
        return {
            "entity_a": round(a, 4),
            "entity_b": round(b, 4),
            "side_by_side": round(a + b, 4),
            "difference": round(abs(a - b), 4),
            "product": round(a * b, 4),
            "coherence": round(self.latest.system_coherence, 4),
            "retention_pct": self.latest.coherence_retention_pct,
            "source": "5D-Manifold",
        }

    def to_volition(self) -> dict:
        """Feedback residual → BLOAT vs FLOW."""
        if not self.latest:
            return {"state": "BLOAT", "source": "idle"}
        # Active closed-loop feedback with low residual = FLOW
        if self.latest.feedback_active and self.latest.feedback_norm < 0.15:
            state = "FLOW"
        else:
            state = "BLOAT"
        return {
            "state": state,
            "feedback_norm": self.latest.feedback_norm,
            "feedback_active": self.latest.feedback_active,
            "source": "5D-Manifold",
        }

    def to_pulse(self) -> dict:
        """Schumann-driven pulse status."""
        return {
            "frequency_hz": SCHUMANN_HZ,
            "schumann_mod": self.latest.schumann_mod if self.latest else 1.0,
            "phase": self.latest.phase if self.latest else 0.0,
            "phi5_load": PHI5,
            "source": "5D-Manifold",
        }

    def status(self) -> dict:
        return {
            "bridge": "ManifoldBridge",
            "connected": self.latest is not None,
            "middle_flow": self.to_middle_flow(),
            "coherence": self.to_coherence(),
            "volition": self.to_volition(),
            "pulse": self.to_pulse(),
        }
