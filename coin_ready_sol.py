# 1.3.4
################


def combine_coins(coin, numbers): return ', '.join(map(lambda s, n: s + str(n), [coin for i in numbers], numbers))

def combine_coins(coin, numbers):    return ', '.join([coin + str(i) for i in numbers])

if __name__ == "__main__":
    print(combine_coins('$', range(10)))
