# 백준 
# https://www.acmicpc.net/problem/11399
# 그리디 

N = map(int, input())
P = list(map(int, input().split(' ')))

P.sort()

total = 0
ans = 0
for time in P:
    total += time
    ans += total

print(ans)

