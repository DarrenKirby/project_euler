# See what I did with the name there? haha

import math


### SECTION 1: primes

def get_primes(n: int) -> list[int]:
    """
    Returns a list of primes up to 'n'
    :param n: upper limit
    :return: list
    """
    # Boolean array of potential primes
    prime = [True for _ in range(n + 1)]
    primes = []

    # The sieve
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Create array of primes
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)

    return primes


def get_prime_factors(n: int) -> list:
    """
    Returns a list of the prime factors of 'n'
    :param n: the integer to get prime factors for.
    :return: list.
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors