# Special Pythagorean Triplet

from math import isqrt


def find_pythagorean_triplets(n: int) -> list[tuple[int, int, int]]:
    triples = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c_2 = a ** 2 + b ** 2
            c = isqrt(c_2)

            if c * c == c_2:
                triples.append((a, b, c))

    return triples


p_triples = find_pythagorean_triplets(1000)
for a, b, c in p_triples:
    if a + b + c == 1000:
        print(a, b, c)
        print(a * b * c)
