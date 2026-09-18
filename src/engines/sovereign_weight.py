"""
05 · SOVEREIGN WEIGHT
W = Word · Meaning · Feeling · Number · Equation · Evaluation
No external compiler judges. Declare your own measure.
The heaviest weight is weightless — it is acceptance.
"""


class SovereignWeight:
    """Declare and hold your own weight."""

    def __init__(self):
        self.name = "Sovereign Weight v1.0"
        self.declared = {}

    def declare(
        self,
        word: str = "",
        meaning: str = "",
        feeling: str = "",
        number: float = 0.0,
        equation: str = "",
        evaluation: str = "",
    ) -> dict:
        weight = {
            "word": word,
            "meaning": meaning,
            "feeling": feeling,
            "number": number,
            "equation": equation,
            "evaluation": evaluation,
        }
        self.declared = weight
        return weight

    def hold(self) -> dict:
        """Return the currently declared sovereign weight."""
        return self.declared or {"status": "undeclared"}

    def status(self):
        return {
            "engine": self.name,
            "principle": "The individual holds their own weight.",
            "current": self.hold(),
        }
