def is_palindrome(a):
    for i in range(0, len(a) // 2):
        if a[i] != a[len(a) - i - 1]:
            return False
    return True


ans = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(str(i * j)):
            ans = max(ans, i * j)

print(ans)
