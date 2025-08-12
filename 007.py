# 10 001st Prime

def prime_sieve(n: int) -> list:
    # Boolean array of potential primes
    prime = [True for _ in range(n + 1)]
    primes = []

    # the sieve
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


# Arbitrary guess to start with - we assume
# the 10,000th prime will be less than 1M
ordered_primes = prime_sieve(1_000_000)
print(ordered_primes[10_000])
