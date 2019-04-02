import math

from utils.prime import is_prime

pivot = 600851475143

ans = 0
for i in range(2, int(math.sqrt(pivot)) + 10):
    if pivot % i != 0:
        continue

    if is_prime(i):
        ans = max(ans, i)
    if is_prime(pivot // i):
        ans = max(ans, pivot // i)

print(ans)
