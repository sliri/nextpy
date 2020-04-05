# 1.3.2
################


def is_prime(number):
    """Check if a number is a prime number"""
    return 0 not in [number % i for i in list(range(2, (number//2)+1))]


if __name__ == "__main__":
    test_input = 29
    print(is_prime(test_input))
