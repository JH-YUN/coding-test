# https://youtu.be/5Lu34WIx2Us?t=3614
# DP
# 가장 긴 증가하는 부분수열 (LIS)
# 입력예시
# 7
# 15 11 4 8 5 2 4

import sys
N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
arr.reverse()
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(N - max(dp))