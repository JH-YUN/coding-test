# 백준 
# https://www.acmicpc.net/problem/2178
# BFS

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = []
    queue.append((x, y))
    while queue:
        x, y = queue[0]
        del(queue[0])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or ny < 1 or nx > N or ny > M:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] += graph[x][y]
            
    return
            
N, M = map(int, input().split(' '))
graph = [[0 for _ in range(M+1)] for _ in range(N+1)]

for x in range(1, N+1):
    line = input()
    for y in range(1, M+1):
        graph[x][y] = int(line[y-1])
bfs(1, 1)

print(graph[N][M])



        
        