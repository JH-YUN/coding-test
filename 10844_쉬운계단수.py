# https://www.acmicpc.net/problem/10844
# DP

# dp[i][j] (j로 끝나는 i길이의 계단수 갯수)
#  = dp[i-1][j-1] + dp[i-1][j+1] (단 j가 0이나 9가 아닐 경우)
#  (j가 0이나 9일경우 이전수가 1이나 8 둘중 하나씩밖에 안된다)

N = int(input())
mod = 1000000000
dp = [[1 for n in range(10)]for n in range(100)]
dp[0][0] = 0
for i in range(1, N):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1] % mod
        elif j == 9:
             dp[i][j] = dp[i-1][j-1] % mod
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % mod
res = 0    
for n in dp[N-1]:
    res = (res + n) % mod
    
print(res)