# 2.5
################


class Animal:
    """The Animal super class."""

    zoo_lst = list()
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """Init the animal class.

        Args:
        name(str):  Animal name
        hunger(int): Hunger level of the animal"""
        self._name = name
        self._hunger = hunger
        Animal.zoo_lst.append(self)

    def get_name(self):
        """Get the animal name."""
        return self._name

    def is_hungry(self):
        """Check if animal is hungry."""
        return self._hunger > 0

    def feed(self):
        """Feed the animal."""
        self._hunger -= 1

    def talk(self):
        """animal talk function."""
        pass


class Dog(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name, hunger)

    def __str__(self):
        return "{} {}".format("Dog", self._name)

    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):

    def __init__(self, name, hunger):
        Animal.__init__(self, name, hunger)

    def __str__(self):
        return "{} {}".format("Cat", self._name)

    def talk(self):
        print("meow")

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):

    def __init__(self, name, hunger, stink_count=6):
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    def __str__(self):
        return "{} {}".format("Skunk", self._name)

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger):
        Animal.__init__(self, name, hunger)

    def __str__(self):
        return "{} {}".format("Unicorn", self._name)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):

    def __init__(self, name, hunger, color="Green"):
        Animal.__init__(self, name, hunger)
        self._color = color

    def __str__(self):
        return "{} {}".format("Dragon", self._name)

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


if __name__ == "__main__":
    brownie = Dog("Brownie", 10)
    zelda = Cat("Zelda", 3)
    stinky = Skunk("Stinky", 0)
    keith = Unicorn("Keith", 7)
    lizzy = Dragon("Lizzy", 1450)
    doggo = Dog("Doggo", 80)
    kitty = Cat("Kitty", 80)
    stinky_Jr = Skunk("Stinky Jr.", 80)
    clair = Unicorn("Clair", 80)
    mcFly = Dragon("McFly", 80)

    for animal in Animal.zoo_lst:
        if animal.is_hungry():
            print(animal)
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print(Animal.zoo_name)

