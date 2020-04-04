# 1.1.3
################


def modulo4_checker(num):
    return num % 4 == 0


def four_dividers(num):
    return list(filter(modulo4_checker, list(range(1, num+1))))


if __name__ == "__main__":
    test_input = 12
    print(four_dividers(test_input))
