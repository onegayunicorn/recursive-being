# Sovereign Stack Integration

How **recursive-being**, **sovereign-devengine**, **photonic-images**, and **5D-Manifold-Evolution** form one architecture.

---

## 1. Shared Constants (single source of truth)

| Symbol | Value | Used by |
|--------|-------|---------|
| `SCHUMANN_HZ` | 7.83 | Pulse engine, PHOTONIC-Ω shaders, 5D bio-enhancement |
| `PHI` | 1.6180339887 | 5-channel tint, SO(5) phase load, Golden Sync channel |
| `HONESTY` | 1 | Recursive weights |
| `ACCEPTANCE` | 1 | Recursive weights |
| `BLOAT` | 0 | Volition engine |

Defined in `src/integrations/constants.py` and mirrored in:
- `sovereign-devengine/docs/photonic-rendering.md`
- `5D-Manifold-Evolution/src/lib/matrixMath.ts` (PHI, PHI5)

---

## 2. Layer Map

```
┌─────────────────────────────────────────────────────────────┐
│  TYRONE Ω  (recursive-being)                                │
│  Genesis · Middle Flow · Volition · Coherence · Weight      │
│  Modes: Third Eye / Beholder / Both                         │
└───────────────────────────┬─────────────────────────────────┘
                            │ coherence ↔ systemCoherence
                            │ equilibrium ↔ bioField / phase
┌───────────────────────────▼─────────────────────────────────┐
│  5D-Manifold-Evolution                                      │
│  SO(5) Lie propagator · PhotonicEngine · Density Matrix     │
│  Environmental forces · Root spinors · PWM channels         │
└───────────────────────────┬─────────────────────────────────┘
                            │ 5-channel tint / Schumann drive
┌───────────────────────────▼─────────────────────────────────┐
│  sovereign-devengine                                        │
│  Handshake (PIN) · Claw Agent · Paean Bridge · Xbox         │
│  PHOTONIC-Ω GLSL dual-pass · Launcher UI                    │
└───────────────────────────┬─────────────────────────────────┘
                            │ assets / sprites / maps
┌───────────────────────────▼─────────────────────────────────┐
│  photonic-images                                            │
│  generate2dsprite · generate2dmap · game-asset-core         │
│  design-ui · building-games skills                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Data Flow Bridges

### A. Recursive Architect ↔ 5D Manifold

| Recursive Engine | 5D Metric |
|------------------|-----------|
| Middle Flow `equilibrium` | `envState.systemCoherence` |
| Coherence Multiplier | `coherenceRetentionPct` |
| Sovereign Pulse (7.83 Hz) | `schumannMod` in bio-enhancement |
| Volition (BLOAT / FLOW) | feedbackActive + residual norm |
| Genesis sequence | trajectoryHistory phase steps |

Bridge: `src/integrations/manifold_bridge.py`

### B. Dev Engine ↔ Photonic Render

- Shader constants from `docs/photonic-rendering.md`
- 5-channel tint driven by Schumann × φ^n
- Launcher visualizes manifold + recursive dashboard side-by-side

### C. Photonic-Images ↔ Everything

- Asset generation for Godot / UWP builds (Dev Engine)
- UI chrome for Recursive dashboard and 5D visualizer
- Map / level pipelines for games that ride the Middle Flow

---

## 4. Clone & Wire

```bash
# Umbrella workspace
mkdir -p ~/sovereign-stack && cd ~/sovereign-stack

git clone https://github.com/onegayunicorn/recursive-being.git
git clone https://github.com/onegayunicorn/sovereign-devengine.git
git clone https://github.com/onegayunicorn/photonic-images.git
git clone https://github.com/onegayunicorn/5D-Manifold-Evolution.git

# Recursive core
cd recursive-being && pip install -r requirements.txt
python -m src.core.recursive_architect

# Dev engine (separate terminal)
cd ../sovereign-devengine
cp .env.example .env   # fill XBOX_* if needed
make setup && make handshake   # :5000
make dev                       # launcher :8080

# 5D Manifold visualizer
cd ../5D-Manifold-Evolution
npm install && npm run dev     # :3000

# Photonic image workspace (Grok Build sandbox style)
cd ../photonic-images
npm install && npm run dev
```

---

## 5. Design Principles (shared)

1. **Local-first** — no mandatory cloud account.
2. **Observable** — every internal state is a dashboard metric.
3. **Sovereign choice dissolves bloat** — indecision is the only stagnation.
4. **Honesty + Acceptance** — the only non-zero weights.
5. **Schumann + φ** — the common clock of the photonic layer.

---

*Not by plans or being comfortable — by finding the side that's not in control.*
