# https://www.acmicpc.net/problem/4386
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
        parents[a] = find(parents,parents[a])
    return parents[a]
        

n = int(input())
stars = []
edges = []
parents = list(range(n))
for i in range(n):
    x, y = map(float, sys.stdin.readline().rstrip().split(' '))
    stars.append((x, y))

for i in range(len(stars)):
    for j in range(i+1, len(stars)):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        cost = ((x2-x1)**2 + (y2-y1)**2)**0.5
        edges.append((i, j, cost))

edges = sorted(edges, key = lambda edge: edge[2])

ans = 0
for edge in edges:
    a, b, cost = edge
    if find(parents, a) != find(parents, b):
        union(parents, a, b)
        ans += cost

print(ans)
    
    
        
