# https://www.acmicpc.net/problem/1774
# union-find

import sys

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b
    
def find(parents, a):
    if a != parents[a]:
        parents[a] = find(parents, parents[a])
    return parents[a]
    
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
nodes = []
edges = []
parents = list(range(N))
for _ in range(N):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    nodes.append((x, y))

for i in range(N):
    x1, y1 = nodes[i]
    for j in range(i+1, N):
        x2, y2 = nodes[j]
        cost = ((x2-x1)**2 + (y2-y1)**2)**0.5
        edges.append((cost, i, j))

ans = 0
cnt = 0
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    a -= 1
    b -= 1
    x1, y1 = nodes[a]
    x2, y2 = nodes[b]
    cost = ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    union(parents, a, b)
    cnt += 1

edges = sorted(edges)
for edge in edges:
    cost, a, b = edge
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
        ans += cost
        cnt+=1
        if cnt == N-1:
            break
print(format(ans, ".2f"))
    
    