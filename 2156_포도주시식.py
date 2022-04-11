# https://www.acmicpc.net/problem/2156
# DP

# 2칸 전까지 생각해야함
# dp[i] 는 i번째까지 가장 많이 마실수 있는 포도주의 양
# arr[i] 는 i번째 포도주의 양
# 1. i번째 포도주를 고를 경우, 
#   1) i-1번째 포도주를 고른다 -> i-2번째 포도주는 고르지 못함 => dp[i] = dp[i-3] + arr[i] + arr[i-1]
#   2) i-1번째 포도주를 고르지 않는다 -> i-2번째 포도주를 고를 수 있음 => dp[i] = dp[i-2] + arr[i]
# 2. i번째 포도주를 고르지 않을 경우
#   => dp[i] = dp[i-1]
# 즉, dp[i] = max(dp[i-3] + arr[i] + arr[i-1], dp[i-2] + arr[i], dp[i-1])

n = int(input())
arr = [0]*10000
dp = [0]*10000

for i in range(n):
    arr[i] = int(input())

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[1]+arr[2], arr[0]+arr[1], arr[0]+arr[2])
    
for i in range(3, n):
    dp[i] = max(arr[i-1] + arr[i] + dp[i-3], dp[i-2] + arr[i])
    dp[i] = max(dp[i], dp[i-1])

print(dp[n-1])
    