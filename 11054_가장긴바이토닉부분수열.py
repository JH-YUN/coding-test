# https://www.acmicpc.net/problem/11054
# DP

n = int(input())
arr = list(map(int, input().split(' ')))
arrR = list(reversed(arr))
dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        # 가장 긴 증가하는 부분수열 구하기
        if arr[i] > arr[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        # 가장 긴 감소하는 부분수열 구하기
        if arrR[i] > arrR[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
ans = 0
dp2 = list(reversed(dp2))
for i in range(n):
    ans = max(ans, dp1[i] + dp2[i])

print(ans-1)
    