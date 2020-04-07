# 2.3.3
################


class Animal:
    count_animals = 0

    def __init__(self, name='Octavio'):
        self._name = name
        self._age = 0
        Animal.count_animals += 1

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


if __name__ == "__main__":
    cat = Animal('Motek')
    octopus = Animal()

    print(str(cat.get_name()))
    print(str(octopus.get_name()))

    cat.set_name('Yago')

    print(str(cat.get_name()))
    print(str(octopus.get_name()))
    print(Animal.count_animals)
