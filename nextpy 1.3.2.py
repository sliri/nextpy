# 1.3.2
################

"""Check if a number is a prime number"""
is_prime = lambda number: all([number % i for i in list(range(2, (number // 2) + 1))])

if __name__ == "__main__":
    test_input = 107
    print(is_prime(test_input))
