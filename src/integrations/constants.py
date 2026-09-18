"""
Shared Sovereign Stack constants.
Mirrored in:
  - sovereign-devengine/docs/photonic-rendering.md
  - 5D-Manifold-Evolution (PHI, PHI5, Schumann modulation)
  - recursive-being engines (Pulse, Coherence)
"""

SCHUMANN_HZ = 7.83
PHI = 1.6180339887
PHI2 = PHI * PHI          # ≈ 2.618
PHI5 = PHI ** 5           # phase load factor in 5D engine

# Core weights (TYRONE Ω)
HONESTY = 1.0
ACCEPTANCE = 1.0
BLOAT = 0.0

# PHOTONIC-Ω 5-channel tint (from sovereign-devengine)
PHOTONIC_CHANNELS = {
    "base":   {"freq": SCHUMANN_HZ,          "color": "#336699"},
    "violet": {"freq": SCHUMANN_HZ * PHI,    "color": "#b333e6"},
    "life":   {"freq": SCHUMANN_HZ * 2,      "color": "#33e666"},
    "gold":   {"freq": SCHUMANN_HZ * PHI2,   "color": "#ffd933"},
    "field":  {"freq": SCHUMANN_HZ / PHI,    "color": "#80e6b3"},
}

# Luminance bloom thresholds
BLOOM_LOW = 0.75
BLOOM_HIGH = 0.92
