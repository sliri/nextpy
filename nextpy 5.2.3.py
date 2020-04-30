# 5.2.3
################

import itertools


def calculate_combinations(cash_bills_dict, total_sum):
    cash_list = []
    final_list = []
    for keys, values in cash_bills_dict.items():
        cash_list.extend([keys] * values)
    for num in range(1, len(cash_list) + 1):
        money = itertools.combinations(cash_list, num)
        for each in money:
            if sum(each) == 100:
                final_list.append(each)
    final_list = set(final_list)
    print(final_list)
    print("There are %s combinations" % len(final_list))
    return final_list


if __name__ == "__main__":
    cash_bills_dict = {20: 3, 10: 5, 5: 2, 1: 5}
    total_sum = 100
    calculate_combinations(cash_bills_dict, total_sum)
