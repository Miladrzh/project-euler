import math


def div_count(a):
    cnt = 0
    for i in range(1, int(math.sqrt(a)) + 1):
        if a % i == 0:
            cnt += 1
            if a // i != i:
                cnt += 1
    return cnt


sum = 1

for i in range(2, 10000000):
    sum += i
    if div_count(sum) > 500:
        print(sum)
        break
