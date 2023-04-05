import random

class Hat:

    houses = ["hi", "bye", "yes"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

hat = Hat()
hat.sort("Harry")