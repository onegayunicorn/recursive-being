"""
Mesh ping stub — four-node consensus probe.

Nodes: recursive-being | sovereign-devengine | photonic-images | 5D-Manifold
"""

from __future__ import annotations

NODES = (
    "recursive-being",
    "sovereign-devengine",
    "photonic-images",
    "5D-Manifold-Evolution",
)


def ping_all(online: dict | None = None) -> dict:
    online = online or {n: True for n in NODES}
    results = {n: {"online": bool(online.get(n, False)), "role": _role(n)} for n in NODES}
    quorum = sum(1 for r in results.values() if r["online"]) >= 3
    return {"nodes": results, "quorum": quorum, "mesh": "sovereign-stack"}


def _role(name: str) -> str:
    return {
        "recursive-being": "core_hearth",
        "sovereign-devengine": "guard_handshake",
        "photonic-images": "light_tint",
        "5D-Manifold-Evolution": "field_so5",
    }.get(name, "unknown")


if __name__ == "__main__":
    import json
    print(json.dumps(ping_all(), indent=2))
