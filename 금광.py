# https://youtu.be/5Lu34WIx2Us?t=3156
# DP
# 입력예시
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split(' '))
    dp = [[0 for _ in range(m)] for _ in range(n)]
    lines = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    for i in range(n):
        for j in range(m):
            dp[i][j] = lines.pop(0)
    for j in range(1, m):
        for i in range(n):
            maxValue = 0
            if i - 1 >= 0:
                maxValue = max(maxValue, dp[i-1][j-1] + dp[i][j])
            if i + 1 < n:
                maxValue = max(maxValue, dp[i+1][j-1] + dp[i][j])
            maxValue = max(maxValue, dp[i][j-1] + dp[i][j])
            dp[i][j] = maxValue
    print(dp)
    
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][m-1])
    print(ans)