"""
Webhook-style event emitters for Phoenix lifecycle.

In production these would POST to configured endpoints;
here they are pure functions returning payload contracts.
"""

from __future__ import annotations

from typing import Any, Dict


def on_coherence_drop(coherence: float, threshold: float = 0.99997) -> Dict[str, Any]:
    return {
        "event": "coherence.drop",
        "coherence": coherence,
        "threshold": threshold,
        "action": "trigger_self_heal" if coherence < threshold else "none",
    }


def on_rebirth(cycle: int, genesis_hash: str) -> Dict[str, Any]:
    return {
        "event": "phoenix.rebirth",
        "cycle": cycle,
        "genesis_hash_prefix": genesis_hash[:16],
        "action": "notify_mesh",
    }


def on_fold_integrity_fail() -> Dict[str, Any]:
    return {
        "event": "fold.integrity_fail",
        "severity": "critical",
        "action": "manual_anchor_required",
    }
