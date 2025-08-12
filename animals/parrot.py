from animal import Animal

class Parrot(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species, sound)

    def parrot_sound(self):
        return super().make_sound()
    