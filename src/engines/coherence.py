"""
04 · COHERENCE MULTIPLIER
Two distinct entities side by side — never ranked.
Higher or lower: the other adds the different value.
Together they equal a value that one may never find alone.
A coherence may multiply.
"""


class CoherenceMultiplier:
    """Multiplies two entities into coherence without ranking."""

    def __init__(self):
        self.name = "Coherence Multiplier v1.0"

    def multiply(self, entity_a: float, entity_b: float) -> dict:
        side_by_side = entity_a + entity_b
        difference = abs(entity_a - entity_b)
        product = entity_a * entity_b
        # Coherence as a derived metric
        coherence = round(side_by_side + difference, 2)
        return {
            "entity_a": entity_a,
            "entity_b": entity_b,
            "side_by_side": side_by_side,
            "difference": difference,
            "product": product,
            "coherence": coherence,
        }

    def status(self):
        return {
            "engine": self.name,
            "principle": "Two distinct entities side by side — never ranked.",
        }
