"""
Bridge: Recursive Architect ↔ photonic-images + PHOTONIC-Ω render core

Provides channel / tint / bloom helpers shared with:
  - sovereign-devengine/src/rendering
  - 5D-Manifold-Evolution CHANNELS
  - photonic-images asset pipelines
"""

from __future__ import annotations
from .constants import (
    SCHUMANN_HZ,
    PHI,
    PHI2,
    PHOTONIC_CHANNELS,
    BLOOM_LOW,
    BLOOM_HIGH,
)


class PhotonicBridge:
    """
    Shared photonic vocabulary for the Sovereign Stack.
    """

    CHANNELS = PHOTONIC_CHANNELS

    def channel_list(self):
        return [
            {"name": name, **meta}
            for name, meta in self.CHANNELS.items()
        ]

    def tint_at(self, t: float) -> dict:
        """
        Return weighted 5-channel mix driven by Schumann/φ oscillators.
        Mirrors the dual-pass composite stage in photonic_core.glsl.
        """
        import math
        weights = {}
        for name, meta in self.CHANNELS.items():
            freq = meta["freq"]
            # oscillator in [0, 1]
            w = 0.5 + 0.5 * math.sin(2 * math.pi * freq * t)
            weights[name] = round(w, 4)
        return {"t": t, "weights": weights, "colors": {n: m["color"] for n, m in self.CHANNELS.items()}}

    def bloom_gate(self, luminance: float) -> float:
        """Smoothstep-style luminance gate (matches GLSL pipeline)."""
        if luminance <= BLOOM_LOW:
            return 0.0
        if luminance >= BLOOM_HIGH:
            return 1.0
        x = (luminance - BLOOM_LOW) / (BLOOM_HIGH - BLOOM_LOW)
        return x * x * (3 - 2 * x)

    def status(self) -> dict:
        return {
            "bridge": "PhotonicBridge",
            "schumann_hz": SCHUMANN_HZ,
            "phi": PHI,
            "channels": self.channel_list(),
            "bloom": {"low": BLOOM_LOW, "high": BLOOM_HIGH},
        }
