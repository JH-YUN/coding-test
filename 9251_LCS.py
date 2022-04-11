# https://www.acmicpc.net/problem/9251
# DP
# 두개의 배열 A, B가 있을 때,
# dp[i][j] 는 A[0:i], B[0:j] 를 비교했을때 최장 공통 부분 수열의 길이이다
# A[i] == B[j] 일때 dp[i][j] = dp[i-1][j-1] + 1
# A[i] != B[j] 일때 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

import sys
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
dp = [[0 for _ in range(1001)]for _ in range(1001)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(a)][len(b)])
        