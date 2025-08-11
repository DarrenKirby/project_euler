# Smallest Multiple

n = 20
while True:
    truth = []
    for i in range(3, 21):
        truth.append(n % i == 0)

    if all(truth):
        print(truth)
        print(n)
        break
    n += 20
