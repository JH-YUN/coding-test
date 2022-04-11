# https://www.acmicpc.net/problem/1932
# DP
import sys
dp = []
n = int(input())
for i in range(n):
    ls = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    dp.append(ls)

for i in range(1,n):
    for j in range(len(dp[i])):
        if j == 0:
            dp[i][j] = dp[i-1][j]+dp[i][j]
        elif j == len(dp[i])-1:
            dp[i][j] = dp[i-1][j-1]+dp[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1]+dp[i][j], dp[i-1][j]+dp[i][j])
print(max(dp[n-1]))
