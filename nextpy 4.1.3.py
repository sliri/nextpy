# 4.1.3
################


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    prime_generator = (n for n in range(n + 1, n ** n) if is_prime(n))
    for prime_number in prime_generator:
        return prime_number


if __name__ == "__main__":
    print(first_prime_over(1000000))
