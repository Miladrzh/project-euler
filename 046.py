# in the name of God
import math

from utils.prime import is_prime


def check(num):
    x = int(math.sqrt(num // 2))  # x is the bound for square number
    for i in range(1, x + 1):
        if is_prime(num - 2 * i * i):
            return True
    return False


for i in range(3, 10000000, 2):
    if not is_prime(i) and not check(i):
        print(i)
        break
