input_file = open('inp.txt')

l = input_file.readlines()

sum = 0
for i in l:
    sum += (int(i))

print(sum // (10 ** (len(str(sum)) - 10)))
