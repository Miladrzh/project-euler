def fifth_power_sum(num):
    ret = 0
    while num > 0:
        ret += ((num % 10) ** 5)
        num //= 10
    return ret


ans = 0
for i in range(10, 10 ** 7):
    if i == fifth_power_sum(i):
        ans += i

print(ans)
