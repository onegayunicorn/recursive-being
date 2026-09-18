"""
02 · MIDDLE FLOW ENGINE
Motion, not stillness.
Push (Ambition) ↔ Pull (Rest)
Equilibrium is the ride.
"""


class MiddleFlowEngine:
    """Balances push and pull into middle flow."""

    def __init__(self, push: float = 0.5, pull: float = 0.5):
        self.name = "Middle Flow Engine v1.2"
        self.push = push  # Ambition
        self.pull = pull  # Rest
        self._equilibrium = 0.0

    def set_push(self, value: float):
        self.push = max(0.0, min(1.0, value))
        self._recalc()

    def set_pull(self, value: float):
        self.pull = max(0.0, min(1.0, value))
        self._recalc()

    def _recalc(self):
        # Simple balance: difference scaled into equilibrium metric
        self._equilibrium = round(abs(self.push - self.pull), 4)

    def equilibrium(self) -> float:
        self._recalc()
        return self._equilibrium

    def balance_pct(self) -> float:
        """Return a stability percentage (higher = more balanced)."""
        diff = abs(self.push - self.pull)
        return round((1.0 - diff) * 100, 1)

    def status(self):
        return {
            "engine": self.name,
            "push": self.push,
            "pull": self.pull,
            "equilibrium": self.equilibrium(),
            "balance": f"{self.balance_pct()}%",
            "state": "Motion, not stillness.",
        }
