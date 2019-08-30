from utils.prime import is_prime

primes = []
for i in range(2, 10 ** 6):
    if is_prime(i):
        primes.append(i)

# calculate partial sum for consecutive primes
partial_sum = [primes[0]]
for i in range(1, len(primes)):
    partial_sum.append(partial_sum[i - 1] + primes[i])

maxi = 0
ans = -1
for i in range(len(primes)):
    for j in range(i + 1, min(i + 1000, len(primes))):  # do you know why i + 1000? ask if u cant get the meaning
        primes_sum = partial_sum[j] - (partial_sum[i - 1] if i > 0 else 0)
        if primes_sum < 10 ** 6 and j - i + 1 > maxi and is_prime(primes_sum):
            maxi = j - i + 1
            ans = primes_sum
print(maxi, ans)
