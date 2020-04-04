# 1.3.1
################


def intersection(list_1, list_2):
    return [item for item in set(list_1) if item in set(list_2)]


if __name__ == "__main__":
    list1 = [5, 5, 6, 6, 7, 7]
    list2 = [1, 5, 9, 5, 6]
    print(intersection(list1, list2))
