# https://www.acmicpc.net/problem/9461
# DP
import sys
T = int(sys.stdin.readline().rstrip())
dp = [1]*100
maxN = 0
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    if maxN >= N:
        print(dp[N-1])
    else:
        maxN = N
        for i in range(N):
            if i-3 < 0:
                dp[i] = 1
            else:
                dp[i] = dp[i-2] + dp[i-3]
        print(dp[N-1])
