# https://www.acmicpc.net/problem/2887
# union find

import sys
import heapq

def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[a] = b
    else:
        parents[b] = a

def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]

N = int(input())
nodes = []
xEdges = []
yEdges = []
zEdges = []
edges = []
parents = list(range(N))

for i in range(N):
    x, y, z = map(int, sys.stdin.readline().rstrip().split(' '))
    xEdges.append((x, i))
    yEdges.append((y, i))
    zEdges.append((z, i))
    
xEdges = sorted(xEdges)
yEdges = sorted(yEdges)
zEdges = sorted(zEdges)

for i in range(1, N):
    x1, xNode1 = xEdges[i-1]
    x2, xNode2 = xEdges[i]
    dx = x2 - x1
    if dx < 0:
        dx *= -1
        
    y1, yNode1 = yEdges[i-1]
    y2, yNode2 = yEdges[i]
    dy = y2 - y1
    if dy < 0:
        dy *= -1
        
    z1, zNode1 = zEdges[i-1]
    z2, zNode2 = zEdges[i]
    dz = z2 - z1
    if dz < 0:
        dz *= -1
    
    heapq.heappush(edges, (dx, xNode1, xNode2))
    heapq.heappush(edges, (dy, yNode1, yNode2))
    heapq.heappush(edges, (dz, zNode1, zNode2))

ans = 0
cnt = 0
while edges:
    cost, x, y = heapq.heappop(edges)
    if find(parents, x) != find(parents, y):
        ans += cost
        cnt += 1
        union(parents, x, y)
        if cnt == N-1:
            break
    
print(ans)