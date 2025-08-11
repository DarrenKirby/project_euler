# Largest Palindrome Product

candidates = []

for x in range(100, 1000):
    for y in range(100, 1000):
        p = x * y
        if str(p) == str(p)[::-1]:
            candidates.append(p)

print(max(candidates))
