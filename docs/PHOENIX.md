# Phoenix Seed — Specification

**Fold Entry + Merkle Genesis Hash = Phoenix Seed**

When coherence drops below **0.99997**, the system does not fail — it resets from a verified foundation. No external backup. Local-first.

## Cycle

```
ASH → SEED → UNFOLD → BLOOM → REMEMBER → ASH → …
```

| Phase | Meaning |
|-------|---------|
| Ash | Coherence below target; state sealed |
| Seed | Revert to Fold Entry hash |
| Unfold | Genesis / GA-style re-parameterization |
| Bloom | Photonic + Middle Flow stabilize |
| Remember | Ledger confirms fall and rise |

## Fold Entry fields

| Key | Value |
|-----|-------|
| frequency | 7.83 |
| proportion | φ |
| honesty | 1 |
| acceptance | 1 |
| bloat | 0 |

Hash: SHA3-256 of sorted `key:value` pairs (32-hex prefix used as seal).

## Run

```bash
python -m src.phoenix.seed
python -m pipelines.phoenix_pipeline
python -m unittest discover -s tests -v
```

## 9 Realms mapping (conceptual)

1 Genesis · 2 Unsaid Help · 3 Retroactive Door · 4 Essence · 5 Sovereign Pace  
6 Middle Flow · 7 Coherence · 8 Decision · 9 Sovereign Weight
