# 1.1.2
################


def double_string(my_str):
    """Get a string ,return a "double" (origin+replica) string """
    return 2 * my_str


def double_letter(my_str):
    """Run over all letters in a string, double(origin+replica) each letter, return the new created string  """
    return ''.join((map(double_string, my_str)))


if __name__ == "__main__":
    test_input = 'we are the champions!'
    print(double_letter(test_input))
