class WalkingCreature:
    def __init__(self, walking_speed, **kwargs):
        super(WalkingCreature, self).__init__(**kwargs)
        self.walking_speed = walking_speed
        print("Initing a walking creature")

    def walk(self):
        print(self.name, "is walking at " + str(self.walking_speed) + "km/h")


class LoudCreature:
    def __init__(self, loudness, **kwargs):
        super(LoudCreature, self).__init__(**kwargs)
        self.loudness =loudness
        print("Initing a loud creature")

    def make_sound(self):
        print(self.name, "making it's sound, it's " + str(self.loudness) + "dbs")


class Animal(WalkingCreature, LoudCreature):
    def __init__(self, name, walking_speed, loudness):
        super(Animal, self).__init__(walking_speed=walking_speed, loudness=loudness)
        self.name = name



genericAnimal = Animal("Alfred", 10, 20)
genericAnimal.walk()
genericAnimal.make_sound()
