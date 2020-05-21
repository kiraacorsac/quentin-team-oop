class WalkingCreature:
    def __init__(self):
        print("Initing a walking creature")

    def walk(self):
        print(self.name, "is walking")


class LoudCreature:
    def __init__(self):
        print("Initing a loud creature")

    def make_sound(self):
        print(self.name, "making it's sound")


class Animal(WalkingCreature, LoudCreature):
    def __init__(self):
        super().__init__()


class Doggo(Animal):
    def __init__(self, name):
        super().__init__()
        self.name = name


jake = Doggo("Jake")