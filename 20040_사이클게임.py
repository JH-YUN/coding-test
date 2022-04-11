# https://www.acmicpc.net/problem/20040
# Union-Find

import sys

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
parents = list(range(n))

ans = 0
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    if find(parents, a) == find(parents, b):
        if ans == 0:
            ans = i
    else:
        union(parents, a, b)

print(ans)
    