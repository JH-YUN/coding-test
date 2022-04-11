# 백준 
# https://www.acmicpc.net/problem/7569
# BFS

import sys
from collections import deque

def bfs(deq):
    global ungrow
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    
    count = 0
    while True:
        temp = deque([])
        while deq:
            x, y, z = deq.popleft()
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if nx < 0 or ny < 0 or nz < 0 or nx >= M or ny >= N or nz >= H:
                    continue
                if graph[nz][ny][nx] == '0':
                    graph[nz][ny][nx] = '1'
                    temp.append((nx, ny, nz))
                    ungrow -= 1
        if not temp:
            break
        deq = temp
        count += 1
        
    return count
                    
M, N, H = map(int, sys.stdin.readline().split(' '))
ungrow = 0

graph = []
deq = deque([])
z = 0
for i in range(H):
    y = 0
    for j in range(N):
        x = 0
        graph.append([])
        line = sys.stdin.readline().rstrip().split(' ')
        graph[z].append(line)
        for k in line:   
            if k == '0':
                ungrow += 1
            elif k == '1':
                deq.append((x, y, z))
            x += 1
        y += 1
    z += 1
    
ans = bfs(deq)
if ungrow > 0:
    print(-1)
else:
    print(ans)
