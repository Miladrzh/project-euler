# be name khoda

def letter(n):
    ret = ''
    if n // 1000 > 0:
        ret += l1[n // 1000] + 'thousand'
        n %= 1000

    andFlag = False
    if n // 100 > 0:
        ret += l1[n // 100] + 'hundred' + 'and'
        andFlag = True
        n %= 100

    if n // 10 > 1:
        ret += l10[n // 10]
        n %= 10
        andFlag = False

    if n // 10 == 1:
        ret += ex[n % 10]
        n = 0
        andFlag = False

    if n % 10 != 0:
        ret += l1[n]
        andFlag = False

    if andFlag:
        ret = ret[:len(ret) - 3]

    return ret


l1 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
l10 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
ex = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ans = 0

for i in range(1, 1001):
    ans += len(letter(i))

print(ans)
