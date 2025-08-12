from animal import Animal

class Lion(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species, sound)

    def lion_sound(self):
        return super().make_sound()
    