# https://www.acmicpc.net/problem/1149
# DP
import sys
N = int(sys.stdin.readline().rstrip())
dp = []
for _ in range(N):
    color = list(map(int, (sys.stdin.readline().rstrip().split(' '))))
    dp.append(color)
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1]+dp[i][0], dp[i-1][2]+dp[i][0])
    dp[i][1] = min(dp[i-1][0]+dp[i][1], dp[i-1][2]+dp[i][1])
    dp[i][2] = min(dp[i-1][0]+dp[i][2], dp[i-1][1]+dp[i][2])
    
print(min(dp[N-1]))
    