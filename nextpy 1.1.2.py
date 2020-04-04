# 1.1.2
################


def double_string(my_str):
    return 2 * my_str


def double_letter(my_str):
    return ''.join((map(double_string, my_str)))


if __name__ == "__main__":
    test_input = 'we are the champions!'
    print(double_letter(test_input))
