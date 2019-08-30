my_file = open('inp.txt', 'r')

inp = str(my_file.read())

tok = ''

for i in inp:
    if i != '\n':
        tok += i

ans = 0

for i in range(0, len(tok) - 12):
    cur = 1
    for j in range(i, i + 13):
        cur *= int(tok[j])
    ans = max(ans, cur)

print(ans)
