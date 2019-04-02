from utils.prime import is_prime

ans = 0
for i in range(2, 2000000):
    if is_prime(i):
        ans += i

print(ans)
