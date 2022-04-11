# https://www.acmicpc.net/problem/2565
# DP

import sys

n = int(sys.stdin.readline().rstrip())
line = []
dp = [1]*100
for _ in range(n):
    a, b = (map(int, sys.stdin.readline().rstrip().split(' ')))
    line.append((a,b))

line = sorted(line, key = lambda k: k[0])

for i in range(n):
    for j in range(i):
        if line[j][1] < line[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
                
print(n - max(dp))