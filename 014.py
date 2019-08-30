memo = {1: 1}


def f(a):
    if a in memo:
        return memo[a]
    if a % 2 == 0:
        memo[a] = 1 + f(a / 2)
    else:
        memo[a] = 1 + f(3 * a + 1)
    return memo[a]


mx = 0
ans = -1
for i in range(1, 1000000):
    if f(i) > mx:
        mx = f(i)
        ans = i

print(ans)
