"""
01 · GENESIS ENGINE
True key holder. Nothing forced. Nothing invented.
F(n) = F(n-1) + F(n-2)
"""


class GenesisEngine:
    """Generates the foundational sequence. Nothing forced."""

    def __init__(self):
        self.name = "Genesis Engine v1.2"
        self.state = "True key holder. Nothing forced."

    def generate(self, n: int = 10):
        if n <= 0:
            return []
        sequence = [0, 1]
        for i in range(2, n):
            sequence.append(sequence[i - 1] + sequence[i - 2])
        return sequence[:n]

    def unfold_term(self, terms: int = 8):
        return self.generate(terms)

    def status(self):
        return {"engine": self.name, "state": self.state, "active": True}
