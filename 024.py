l = []


def generate(pos, curr):
    if len(l) > 1000000:
        return
    if pos == 11:
        l.append(curr)
        return

    for i in range(10):
        if str(i) not in curr:
            generate(pos + 1, curr + str(i))
    return


generate(1, '')
print(l[999999])
