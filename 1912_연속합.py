# https://www.acmicpc.net/problem/1912
# DP

import sys

n = int(sys.stdin.readline().rstrip())
dp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

for i in range(1, n):
    dp[i] = max(dp[i-1] + dp[i], dp[i])

print(max(dp))

