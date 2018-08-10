from math import gcd

cur = 1
for i in range(2, 21):
    ans = cur * i
    ans //= gcd(cur, i)
    cur = ans

print(ans)
