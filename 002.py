# Even Fibonacci Numbers

def make_fibs(x: int, y: int, upper_bound: int) -> list:
    fibs = [x, y]
    while fibs[-1] < upper_bound:
        new_y = x + y
        fibs.append(new_y)
        x = y
        y = new_y
    return fibs[:-1]


even_fibs = filter(lambda n: n % 2 == 0, make_fibs(1, 2, 4_000_000))
print(sum(even_fibs))
