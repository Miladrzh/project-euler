# in the name of God

my_file = open("inp.txt", 'r')

numbers = my_file.readlines()

dp = [[0 for x in range(len(numbers))] for y in range(len(numbers))]

dp[0][0] = int(numbers[0])

for i in range(1, len(numbers)):
    cur_line = numbers[i].split(' ')
    for j in range(len(cur_line)):
        if dp[i][j] < (dp[i - 1][j] + int(cur_line[j])) and j < i:
            dp[i][j] = (dp[i - 1][j] + int(cur_line[j]))
        if dp[i][j] < (dp[i - 1][j - 1] + int(cur_line[j])) and j > 0:
            dp[i][j] = dp[i - 1][j - 1] + int(cur_line[j])

ans = 0
for i in range(len(numbers)):
    ans = max(ans, dp[len(numbers) - 1][i])

print(ans)
