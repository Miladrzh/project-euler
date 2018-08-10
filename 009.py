for i in range(1, 1000):
    for j in range(1, 1000 - i):
        k = 1000 - i - j
        if i * i == j * j + k * k and k > 0:
            print(i * j * k)
            exit(0)
