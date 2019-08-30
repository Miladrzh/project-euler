l = []
prime = []
for i in range(0, 10 ** 7):
    l.append(False)

for i in range(2, 10 ** 7):
    if l[i]:
        continue
    for j in range(2 * i, 10 ** 7, i):
        l[j] = True
    prime.append(i)

print(len(prime), prime[0], prime[10000])
