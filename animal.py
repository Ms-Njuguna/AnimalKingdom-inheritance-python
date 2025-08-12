
class Animal():
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"The sound made by {self.name} :({self.species}) is {self.sound}")

    def __str__(self):
        return f"{self.name} the {self.species}"