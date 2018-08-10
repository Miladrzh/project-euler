l = []

for i in range(2, 101):
    for j in range(2, 101):
        if i ** j not in l:
            l.append(i ** j)

print(len(l))
