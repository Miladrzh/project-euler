from math import factorial

number = str(factorial(100))

tk = 0
for i in range(len(number)):
    tk += int(number[i])

print(tk)
