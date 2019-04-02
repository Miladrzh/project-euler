import math


def factorial_sum(num):
    ret = 0
    while num > 0:
        ret += math.factorial(num % 10)
        num //= 10
    return ret


ans = 0
for i in range(10, 10 ** 7):
    if i == factorial_sum(i):
        ans += i

print(ans)
