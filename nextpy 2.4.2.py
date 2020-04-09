# 2.4.2
################


class BigThing:

    def __init__(self, some_input):
        self.some_input = some_input

    def size(self):
        if isinstance(self.some_input, int) or isinstance(self.some_input, float):
            return self.some_input
        else:
            return len(self.some_input)


class BigCat(BigThing):
    def __init__(self, some_input, weight=0):
        BigThing.__init__(self, some_input)
        self.weight = weight
        if 15 < weight < 20:
            print('FAT')
        elif weight > 20:
            print('VERY FAT')
        else:
            print('OK')


if __name__ == "__main__":
    cutie = BigCat("mitzy", 22)
    print(cutie.size())
