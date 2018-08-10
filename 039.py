d = [0 for x in range(1002)]

for p in range(1, 1001):
    for a in range(1, p):
        for b in range(1, p - a):
            # print(b)
            c = p - a - b

            if a * a == b * b + c * c and c < b < a < b + c:
                d[p] += 1

ind = 0
for i in range(len(d)):
    if d[ind] < d[i]:
        ind = i

print(ind)
