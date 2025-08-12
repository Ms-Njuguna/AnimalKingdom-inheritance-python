from animal import Animal

class Elephant(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species, sound)

    def elephant_sound(self):
        return super().make_sound()
    