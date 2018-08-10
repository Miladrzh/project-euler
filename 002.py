x = 1
y = 2
z = 3
ans = 0

while y <= 4000000:
    if y % 2 == 0:
        ans += y
    z = x + y
    x = y
    y = z

print(ans)
