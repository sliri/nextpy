# 1.3.3
################


is_funny = lambda string: all([char in "ha" for char in string])

if __name__ == "__main__":
    test_input = 'hahhhav'
    print(is_funny(test_input))
