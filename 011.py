myfile = open('inp.txt')
l = myfile.readlines()

a = []
for i in l:
    a.append(i.strip('\n').split(' '))

ans = 0
for i in range(20):
    for j in range(20):
        if j - 3 >= 0:
            ans = max(ans, int(a[i][j]) * int(a[i][j - 1]) * int(a[i][j - 2]) * int(a[i][j - 3]))
        if i - 3 >= 0 and j - 3 >= 0:
            ans = max(ans, int(a[i][j]) * int(a[i - 1][j - 1]) * int(a[i - 2][j - 2]) * int(a[i - 3][j - 3]))
        if i - 3 >= 0:
            ans = max(ans, int(a[i][j]) * int(a[i - 1][j]) * int(a[i - 2][j]) * int(a[i - 3][j]))
        if i + 3 < 20 and j - 3 >= 0:
            ans = max(ans, int(a[i][j]) * int(a[i + 1][j - 1]) * int(a[i + 2][j - 2]) * int(a[i + 3][j - 3]))

print(ans)
