# 1.1.4
################

import functools


def list2str(num):
    """Convert an integer to a list of  its digits, each of which is a string"""
    return list(str(num))


def str2int(num):
    """Convert an integer to a list of digits, each of which is an integer"""
    return list(map(int, num))


def add(x, y):
    """Add two numbers"""
    return x + y


def sum_of_digits(number):
    """Get an integer, return the sum of its digits"""
    return functools.reduce(add, (str2int(list2str(number))))


if __name__ == "__main__":
    test_input = 1858
    print(sum_of_digits(test_input))
