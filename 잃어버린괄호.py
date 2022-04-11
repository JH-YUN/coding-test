# 백준
# https://www.acmicpc.net/problem/1541
# 문자열 파싱
# 그리디 

P = input()
P = P.split('-')
res = 0
for n in P.pop(0).split('+'):
    res += int(n)

for s in P:
    total = 0
    for n in s.split('+'):
        total += int(n)
    res -= total

print(res)