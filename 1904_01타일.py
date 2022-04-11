# https://www.acmicpc.net/problem/1904
# DP

# 큐 사용

from collections import deque
DIV = 15746
n = int(input())
dp = deque([])
dp.append(1)
dp.append(1)

for i in range(2, n+1):
    a = dp.popleft()
    b = dp[0]
    dp.append((a+b) % DIV)

print(dp[1])

# 배열 사용 

# DIV = 15746
# n = int(input())
# dp = [0] * (n+1)
# dp[0] = 1
# dp[1] = 1

# for i in range(2, n+1):
#     dp[i] = (dp[i-1] + dp[i-2]) % DIV

# print(dp[n])