"""
Schumann Resonance metrics

Earth–ionosphere cavity standing waves.
Fundamental ~7.83 Hz; observed drift typically 7.4–8.2 Hz.
Harmonics (approx.): 14.3, 20.8, 27.3, 33.8 Hz (~6.5 Hz spacing).
Q-factor of fundamental typically 4–8.
"""

from __future__ import annotations

import math
from typing import Dict, List

# Nominal mode table (geophysical literature)
SCHUMANN_MODES: Dict[str, float] = {
    "fundamental": 7.83,   # n=1
    "h2": 14.3,            # n=2
    "h3": 20.8,            # n=3
    "h4": 27.3,            # n=4
    "h5": 33.8,            # n=5
}

# φ-scaled family (used in stack for photonic tint / bio coupling)
PHI = (1 + 5**0.5) / 2


class SchumannMetrics:
    """Compute oscillators, harmonics, and φ-linked frequencies."""

    def __init__(self, fundamental: float = 7.83):
        self.f1 = fundamental

    def modes(self) -> Dict[str, float]:
        return {
            "fundamental": self.f1,
            "h2": self.f1 * (14.3 / 7.83),
            "h3": self.f1 * (20.8 / 7.83),
            "h4": self.f1 * (27.3 / 7.83),
            "h5": self.f1 * (33.8 / 7.83),
        }

    def phi_ladder(self) -> List[float]:
        """φ-powers of fundamental (photonic / neural-overlap exploration)."""
        return [self.f1 * (PHI ** n) for n in range(0, 6)]

    def oscillator(self, t: float, mode: str = "fundamental", depth: float = 0.05) -> float:
        """1 + depth * sin(2π f t) — used in bio-enhancement / pulse."""
        f = self.modes().get(mode, self.f1)
        return 1.0 + depth * math.sin(2 * math.pi * f * t)

    def cavity_estimate(self, earth_radius_m: float = 6.371e6) -> float:
        """
        Ideal thin-shell approximation f ≈ c / (2π R).
        Real cavity is lossy; observed peak drifts with ionosphere height.
        """
        c = 2.99792458e8
        return c / (2 * math.pi * earth_radius_m)

    def status(self) -> dict:
        return {
            "f1": self.f1,
            "modes": self.modes(),
            "phi_ladder": [round(x, 4) for x in self.phi_ladder()],
            "ideal_cavity_hz": round(self.cavity_estimate(), 4),
            "q_nominal_range": [4, 8],
            "drift_band_hz": [7.4, 8.2],
        }


if __name__ == "__main__":
    m = SchumannMetrics()
    print("Schumann metrics:", m.status())
