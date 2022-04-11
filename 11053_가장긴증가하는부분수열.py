# https://www.acmicpc.net/problem/11053
# DP

# 가장 긴 증가하는 부분 수열(LIS)
# dp[i] = i번째 수를 마지막으로 할때 가장 긴 수열의 길이
# dp[i] = if arr[i] > arr[j]: max(dp[i], dp[j] + 1)  단, 0 <= j < i
N = int(input())
A = list(map(int, input().split(' ')))

dp = [1]*1000

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))