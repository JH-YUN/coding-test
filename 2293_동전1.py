# https://www.acmicpc.net/problem/2293
# DP
# dp[i][k] 는 i번째 동전까지 사용할 때, k원을 만드는 경우의 수
# dp[i][k] = dp[i-1][k] + dp[i][k-k(i)] 단, k >= k(i) 일때  
# dp[i][k] = dp[i-1][k] 단, k < k(i) 일때  
# 이 문제의 경우 메모리 제한이 빡빡하므로 dp[i-1][k]를 dp[i][k]가 덮어쓰는 방식으로 처리
n, k = map(int, input().split(' '))
dp = [0] * (k+1)
dp[0] = 1
for i in range(n):
    coin = int(input())
    for j in range(1, k+1):
        if j >= coin:
            dp[j] = dp[j] + dp[j-coin]

print(dp[k])