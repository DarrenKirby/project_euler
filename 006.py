# Sum Square Difference

sum_of_squares = sum([n ** 2 for n in range(1, 101)])
square_of_sums = sum([n for n in range(1, 101)]) ** 2

print(square_of_sums - sum_of_squares)
