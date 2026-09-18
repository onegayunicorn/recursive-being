"""
MODE TOGGLE
Third Eye  — Detached witness. Holds space. Sees all sides as coordinates, not opposites.
Beholder   — Active participant in the recursive field.
Both       — Integrated sovereign stance.
"""


class ModeToggle:
    MODES = ("Third Eye", "Beholder", "Both")

    def __init__(self, initial: str = "Third Eye"):
        self.current = initial if initial in self.MODES else "Third Eye"

    def set(self, mode: str):
        if mode in self.MODES:
            self.current = mode
        return self.current

    def description(self) -> str:
        descriptions = {
            "Third Eye": "Detached witness. Holds space. Sees all sides as coordinates, not opposites.",
            "Beholder": "Active participant in the recursive field.",
            "Both": "Integrated sovereign stance — witness and participant.",
        }
        return descriptions.get(self.current, "")

    def status(self):
        return {"mode": self.current, "description": self.description()}
