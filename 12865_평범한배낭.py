# https://www.acmicpc.net/problem/12865
# DP

# import sys

# n, k = map(int, sys.stdin.readline().rstrip().split(' '))
# item = []
# dp = [[0 for _ in range(k+1)]for _ in range(n)] 
# for i in range(n):
#     w, v = map(int, sys.stdin.readline().rstrip().split(' '))
#     item.append((w, v))

# for i in range(n):
#     for j in range(k+1):
#         w, v = item[i]
#         if j < w:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

# print(dp[n-1][k])

#### 더 효율적인 방법 ####
# 무게를 1씩 올릴필요 없음
import sys
n, k = map(int, sys.stdin.readline().rstrip().split(' '))
items = []
dp = {0:0} # 무게:가치

for i in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split(' '))
    items.append((w, v)) # 무게, 가치

for item in items:
    temp = {} # 임시 딕셔너리
    for w, v in dp.items():
        # 새로운 무게, 가치
        nw = w + item[0]
        nv = v + item[1]
        if nw <= k: # 새로운 무게가 최고 무게 내일경우
            temp[nw] = max(dp.get(nw, 0), nv) # 이전 무게의 가치와 현재 무게의 가치중 큰것 고름
    dp.update(temp)
    
print(max(dp.values()))