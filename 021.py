from math import sqrt

d = {}


def div_sum(x):
    ret = 0
    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0 and i != x:
            ret += i
            if x / i != i and x / i != x:
                ret += (x / i)
    return ret


for i in range(1, 10000):
    d[i] = div_sum(i)

ans = 0
for i in range(1, 10000):
    try:
        if i == d[d[i]] and i != d[i]:
            ans += i
    except KeyError:
        continue

print(ans)
