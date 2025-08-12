# 10 001st Prime

from eutilties import get_primes

# Arbitrary guess to start with - we assume
# the 10,000th prime will be less than 1M
ordered_primes = get_primes(1_000_000)
print(ordered_primes[10_000])
