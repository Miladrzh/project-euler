from math import sqrt as SQR


def is_prime(a):
    for i in range(2, int(SQR(a)) + 1):
        if a % i == 0:
            return False
    return True


pivot = 600851475143

ans = 0
for i in range(2, int(SQR(pivot)) + 10):
    if pivot % i != 0:
        continue

    if is_prime(i):
        ans = max(ans, i)
    if is_prime(pivot // i):
        ans = max(ans, pivot // i)

print(ans);
