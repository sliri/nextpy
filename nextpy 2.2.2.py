# 2.2.2
################


class Animal:
    def __init__(self):
        self.name = 'Name'
        self.age = 0

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


if __name__ == "__main__":
    cat = Animal()
    octopus = Animal()

    cat.birthday()
    print(str(cat.get_age()))
    print(str(octopus.get_age()))
