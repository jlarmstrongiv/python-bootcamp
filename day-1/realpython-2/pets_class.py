# Parent class
class Dog:

  # Class attribute
  species = 'mammal'

  # Initializer / Instance attributes
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.is_hungry = True

  # instance method
  def description(self):
    return "{} is {} years old".format(self.name, self.age)

  # instance method
  def speak(self, sound):
    return "{} says {}".format(self.name, sound)

  def eat(self):
    self.is_hungry = False

  def walk(self):
    print(f'{self.name} is walking!')

# Child class (inherits from Dog class)


class RussellTerrier(Dog):
  def run(self, speed):
    return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)


class Bulldog(Dog):
  def run(self, speed):
    return "{} runs {}".format(self.name, speed)

class Pets:
  def __init__(self, dogs):
    self.dogs = dogs
  def walk(self):
    for dog in self.dogs:
      dog

my_dogs = [
  RussellTerrier('Spot', 5),
  Bulldog('Roadkill', 13),
]

my_pets = Pets(my_dogs)

print(f'I have {len(my_pets.dogs)} dogs')
dogs_are_fed = False
for dog in my_pets.dogs:
  print(f'{dog.name} is {dog.age}')
  dog.eat()
  if (dog.is_hungry is True):
    dogs_are_fed = False
print(f'And they’re all {dog.species}, of course.')
if (dogs_are_fed):
  print("My dogs are hungry.")
else:
  print("My dogs are not hungry.")
my_pets.walk()
