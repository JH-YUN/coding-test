# https://www.acmicpc.net/problem/17472
# 크루스칼 , BFS

import sys
import collections

def BFS(start, graph, cnt):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = collections.deque([])
    q.append(start)
    graph[start[0]][start[1]] += cnt # 한칸짜리 섬도 섬으로 취급
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += cnt
                q.append((nx, ny))    

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

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
graph = []
edges = []
parents = []

for _ in range(N):
    l = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(l)

# BFS 이용하여 각 섬 이름지어주기
cnt = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            cnt += 1
            BFS((i, j), graph, cnt)

parents = list(range(cnt+1)) # 부모 테이블 생성

# 섬 사이의 다리 구하기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    for j in range(M):
        if graph[i][j] > 1:
            node = graph[i][j]
            for k in range(4):
                dist = 0
                nx = i
                ny = j
                while True:
                    nx = nx + dx[k]
                    ny = ny + dy[k]
                    if nx < 0 or ny < 0 or nx >= N or ny >= M or graph[nx][ny] == node:
                        break
                    elif graph[nx][ny] == 0:
                        dist += 1
                    else:
                        if dist >= 2:
                            edges.append((dist, node - 1, graph[nx][ny] - 1))
                        break

# 크루스칼 알고리즘으로 최소신장트리 구하기
edges = sorted(edges)
ans = 0
cnt = 0
for edge in edges:
    dist, a, b = edge
    if find(parents, a) != find(parents, b):
        ans += dist
        union(parents, a, b)
        cnt += 1
    if cnt == len(parents) - 2:
        break

if cnt < len(parents) - 2:
    print(-1)
else:
    print(ans)

# 10 6
# 0 0 0 1 0 0
# 0 0 0 1 0 0
# 0 1 0 0 0 1
# 0 0 0 0 0 0
# 1 1 0 1 1 0
# 1 0 0 0 1 0
# 1 1 0 0 1 0
# 0 0 0 0 1 1
# 0 0 0 0 0 0
# 0 1 0 0 0 0
# output: -1
# correct answer: 13

# 10 10
# 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 1 0 1 0 1 0 1 0 1 0
# output: -1
# answer: 40