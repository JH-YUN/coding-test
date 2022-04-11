# https://www.acmicpc.net/problem/1976

import sys
sys.setrecursionlimit(10**8)

def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if (a < b):
        parents[b] = a
    else:
        parents[a] = b
    
N = int(input())
M = int(input())
parents = list(range(N+1))

for i in range(1, N+1):
    routes = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    for j in range(N):
        if routes[j] == 1:
            union(parents, i, j+1)
        
plans = list(map(int, sys.stdin.readline().rstrip().split(' ')))

flag = True
for i in range(len(plans)-1):
    if find(parents, plans[i]) != find(parents, plans[i+1]):
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
    
    
    