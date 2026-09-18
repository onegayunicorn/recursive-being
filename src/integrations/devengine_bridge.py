"""
Bridge: Recursive Architect ↔ sovereign-devengine

Exposes handshake / Claw / Paean concepts as status objects
so the Recursive dashboard can reflect local-first deploy state.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class HandshakeStatus:
    paired: bool = False
    pin_active: bool = False
    pin_expires_in_s: int = 0
    device_id: Optional[str] = None


@dataclass
class ClawStatus:
    healthy: bool = False
    last_command: Optional[str] = None
    build_ready: bool = False


@dataclass
class PaeanBridgeStatus:
    sync_ok: bool = False
    deploy_ok: bool = False
    root_pinned: bool = True


class DevEngineBridge:
    """
    Lightweight status adapter for sovereign-devengine services.

    In production these would be filled by HTTP calls to:
      - handshake daemon  (:5000)
      - claw_agent CLI / status endpoint
      - /paean/sync  /paean/deploy
    """

    def __init__(self):
        self.handshake = HandshakeStatus()
        self.claw = ClawStatus()
        self.paean = PaeanBridgeStatus()

    def update_handshake(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self.handshake, k):
                setattr(self.handshake, k, v)

    def update_claw(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self.claw, k):
                setattr(self.claw, k, v)

    def update_paean(self, **kwargs):
        for k, v in kwargs.items():
            if hasattr(self.paean, k):
                setattr(self.paean, k, v)

    def is_sovereign_ready(self) -> bool:
        """True when local stack can build/deploy without cloud."""
        return (
            self.handshake.paired
            and self.claw.healthy
            and self.paean.root_pinned
        )

    def status(self) -> dict:
        return {
            "bridge": "DevEngineBridge",
            "handshake": self.handshake.__dict__,
            "claw": self.claw.__dict__,
            "paean": self.paean.__dict__,
            "sovereign_ready": self.is_sovereign_ready(),
        }
