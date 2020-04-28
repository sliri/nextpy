# 4.2.2
################


def parse_ranges(ranges_string):
    first_generator = (word.split('-') for word in ranges_string.split(','))
    second_generator = (num for s in first_generator for num in range(int(s[0]), int(s[1]) + 1))
    return list(second_generator)


if __name__ == "__main__":
    print(list(parse_ranges("1-2,4-4,8-10")))
