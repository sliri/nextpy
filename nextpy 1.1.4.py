# 1.1.4
################

import functools


def list2str(num):
    return list(str(num))


def str2int(num):
    return list(map(int, num))


def add(x, y):
    return x + y


def sum_of_digits(number):
    return functools.reduce(add, (str2int(list2str(number))))


if __name__ == "__main__":
    test_input = 1858
    print(sum_of_digits(test_input))
