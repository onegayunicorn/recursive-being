# Schumann Resonance & SO(5) Lie Algebra

Exploration notes locked into the Sovereign Stack.

---

## Schumann Resonance

Standing electromagnetic waves in the Earth–ionosphere cavity, excited by global lightning (~50 flashes/s).

| Mode | Nominal frequency | Notes |
|------|-------------------|--------|
| Fundamental (n=1) | **7.83 Hz** | Dominant; stack pulse / bio anchor |
| 2nd | ~14.3 Hz | Near alpha/low-beta EEG band |
| 3rd | ~20.8 Hz | Sensitive to solar activity |
| 4th | ~27.3 Hz | Weaker |
| 5th | ~33.8 Hz | Higher modes fade into noise |

**Observed drift:** fundamental typically **7.4–8.2 Hz**.  
**Q-factor:** roughly **4–8** for a healthy cavity.  
**Ideal thin-shell estimate:** $f \approx c/(2\pi R_{\oplus}) \approx 7.5$ Hz (lossy cavity shifts the real peak).

### Stack usage

- `SCHUMANN = 7.83` in Phoenix Seed, Pulse engine, Photonic tint, 5D bio-enhancement
- Oscillator form: $1 + d\sin(2\pi f t)$ with small depth $d$ (e.g. 0.05)
- φ-ladder: $f_1 \cdot \varphi^n$ for photonic channel spacing

Code: `src/metrics/schumann.py`

---

## SO(5) Lie Algebra

| Property | Value |
|----------|--------|
| Group | SO(5) — rotations of $\mathbb{R}^5$ |
| Algebra | $\mathfrak{so}(5)$ — $5\times5$ real skew-symmetric matrices |
| Dimension | $\dim SO(n) = n(n-1)/2$ → **10** |
| Rank | **2** |
| Generators | $J_{ab}$ plane rotations, $a < b$, $a,b \in \{0..4\}$ |

**Odd dimension:** every real skew-symmetric $A \in \mathfrak{so}(5)$ has $\det A = 0$ → guaranteed **zero mode** (null direction on $S^4$).

### Stack usage (5D-Manifold-Evolution)

$$
U = \exp\bigl((A_{\mathrm{base}} + A_{\mathrm{corr}} + A_{\mathrm{EMI}})\,dt\bigr) \in SO(5)
$$

- $A_{\mathrm{base}}$ — photonic + bio-weighted generator (scaled to $\varphi^5$)
- $A_{\mathrm{corr}}$ — closed-loop residual correction (stays in $\mathfrak{so}(5)$)
- $A_{\mathrm{EMI}}$ — environmental torque (RF / grid / solar profiles)

State $x \in S^4$ evolves as $x \leftarrow Ux$; norm is preserved (identity survives rebirth).

Code: `src/metrics/so5.py` (Python mirror) · `5D-Manifold-Evolution/src/lib/matrixMath.ts` (runtime)

---

## Link to Phoenix

When coherence $< 0.99997$, Phoenix returns to **Fold Entry** (Schumann + φ + honesty/acceptance).  
SO(5) propagation is the continuous “field” that the seed regenerates into; Schumann is the discrete clock of that field.
