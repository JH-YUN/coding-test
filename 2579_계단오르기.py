# https://www.acmicpc.net/problem/2579
# DP

# dp[i] 는 i번째 계단을 밟았을 때 점수의 최대 값, arr[i]는 i번째 계단의 점수
# i번째 계단을 밟는다고 할때 i-1계단도 밟을 경우 3연속 계단을 밟지는 못하므로 dp[i-3]+arr[i-1]+arr[i]
# i-1번째 계단을 밟지 않을 경우 3연속에 위배되지 않으므로 dp[i-2]+arr[i]
# dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

import sys

n = int(sys.stdin.readline().rstrip())
arr = [0]*300
dp = [0]*10000

for i in range(n):
    arr[i] = int(sys.stdin.readline().rstrip())
dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(dp[1], dp[0] + arr[2])

for i in range(2, n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    
print(dp[n-1])