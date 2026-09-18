"""
03 · VOLITION & BLOAT
Indecision is the only true stagnation.
Want (I) / Will (You)
Neither moves … thoughts swell. Clear: choose YES or NO.
Indecision is what holds the bloat.
"""


class VolitionEngine:
    """Processes volition and dissolves bloat."""

    def __init__(self):
        self.name = "Volition & Bloat v1.1"
        self.want = False  # I
        self.will = False  # You
        self.state = "BLOAT"

    def set_want(self, value: bool):
        self.want = value
        self._update_state()

    def set_will(self, value: bool):
        self.will = value
        self._update_state()

    def _update_state(self):
        if self.want or self.will:
            self.state = "FLOW"
        else:
            self.state = "BLOAT"

    def process_state(self) -> str:
        self._update_state()
        return self.state

    def dissolve_bloat(self):
        """Sovereign choice dissolves indecision."""
        if self.state == "BLOAT":
            # Default sovereign act: choose acceptance path
            self.will = True
            self._update_state()
        return self.state

    def status(self):
        return {
            "engine": self.name,
            "want": self.want,
            "will": self.will,
            "state": self.state,
            "message": "Indecision is the only true stagnation." if self.state == "BLOAT" else "Sovereign choice active.",
        }
