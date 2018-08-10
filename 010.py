import math


def is_prime(a):
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            return False;
    return True;


ans = 0
for i in range(2, 2000000):
    if is_prime(i):
        ans += i

print(ans)
