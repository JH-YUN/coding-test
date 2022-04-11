# https://youtu.be/5Lu34WIx2Us?t=2667
# DP

import sys

INF = 10001
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
moneys = []
dp = [INF] * INF
dp[0] = 0

for _ in range(N):
    money = int(sys.stdin.readline().rstrip())
    moneys.append(money)

# for i in range(M+1):
#     for money in moneys:
#         if i - money < 0:
#             continue
#         dp[i] = min(dp[i], dp[i - money] + 1)

for money in moneys:
    for i in range(money, M+1):
        dp[i] = min(dp[i], dp[i - money] + 1)

print(dp[M] if dp[M] != INF else -1)
