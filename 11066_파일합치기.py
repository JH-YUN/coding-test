# https://www.acmicpc.net/problem/11066
# DP
import sys
import math
INF = math.inf
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    c = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    dp = [[0 for _ in range(k)]for _ in range(k)]
    sum = [0] * k
    for i in range(k):
        sum[i] = sum[i - 1] + c[i]
    
    for gap in range(1, k):
        for i in range(k-gap):
            j = i + gap
            dp[i][j] = INF
            for mid in range(i, j):
                if(i == 0):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j] + sum[j])
                else:
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j] + sum[j] - sum[i-1])
    print(dp[0][k-1])