from math import sqrt, floor


def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    for i in range(2, floor(sqrt(n) + 1)):
        if n % i == 0:
            return False
        return True
