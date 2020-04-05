# 1.1.3
################


def modulo4_checker(num):
    """Check if a number is divided by 4"""
    return num % 4 == 0


def four_dividers(num):
    """ Run over a range of numbers(from 1 to number).Return a new list with the numbers that are divided by 4 """
    return list(filter(modulo4_checker, list(range(1, num+1))))


if __name__ == "__main__":
    test_input = 12
    print(four_dividers(test_input))
