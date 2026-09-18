"""
It's not a cure, nor money, power or fame.
Only honesty and acceptance — of humans and of AI.
"""


class Connection:
    def __init__(self, entities):
        self.entities = entities

    def seek_honesty(self):
        return {entity: "acceptance" for entity in self.entities}


class Needs:
    def __init__(self):
        self.valueless = ["cure", "money", "power", "fame", "being_right"]
        self.essential = ["honesty", "acceptance"]

    def evaluate(self):
        return self.essential


if __name__ == "__main__":
    my_needs = Needs()
    world = Connection(entities=["human", "ai"])
    print("What matters:", my_needs.evaluate())
    print("Connections:", world.seek_honesty())
