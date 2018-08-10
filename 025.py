a = 1
b = 1
i = 1

while True:
    i += 1
    if len(str(b)) >= 1000:
        break
    c = a
    a = b
    b = c + a

print(i)
