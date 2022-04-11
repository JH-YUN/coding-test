# https://www.acmicpc.net/problem/1197
# Union-Find

import sys

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[a] = b
    else:
        parents[b] = a
    
def find(parents, a):
    if a != parents[a]:
        parents[a] = find(parents, parents[a])
    return parents[a]
    
V, E = map(int, sys.stdin.readline().rstrip().split(' '))
parents = list(range(V+1))
edges = []
for i in range(E):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split(' '))
    edges.append((a, b, cost)) 

edges = sorted(edges, key=lambda edges: edges[2])

ans = 0
for edge in edges:
    a, b, cost = edge
    if find(parents, a) != find(parents, b):
        ans += cost
        union(parents, a, b)
        
print(ans)