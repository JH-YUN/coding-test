# 백준 
# https://www.acmicpc.net/problem/1012
# DFS, BFS

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = []
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue[0]
        del(queue[0])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] != 0:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return
                    
T = int(input())
for _ in range(T):
    res = 0
    M, N, K = map(int, input().split(' '))
    graph = [[0 for _1 in range(N)] for _ in range(M)]
    for j in range(K):
        x, y = map(int, input().split(' '))
        graph[x][y] = 1
    for x in range(M):
        for y in range(N):
            if graph[x][y] != 0:
                bfs(x, y)
                res += 1
    print(res)