from animals.elephant import Elephant
from animals.lion import Lion
from animals.parrot import Parrot

# Create objects
elephant1 = Elephant("Dumbo", "Loxodonta", "trumpeting")
lion1 = Lion("Simba", "Katanga", "roaring")
parrot1 = Parrot("Paparoti", "Green Parakeet", "chirping")

# Display info
print(elephant1)
elephant1.elephant_sound()

print(lion1)
lion1.lion_sound()

print(parrot1)
parrot1.parrot_sound()
