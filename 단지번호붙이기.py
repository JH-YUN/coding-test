# 백준 
# https://www.acmicpc.net/problem/2667
# DFS, BFS

# ---- dfs 풀이 ------
# def dfs(x, y, res):
#     if x < 0 or y < 0 or x >= N or y >= N:
#         return False
#     if graph[x][y] == 0:
#         return False
    
#     graph[x][y] = 0 # 방문표시
#     num[res] += 1 # 단지별 아파트수 추가
#     dfs(x + 1, y, res)
#     dfs(x - 1, y, res)
#     dfs(x, y + 1, res)
#     dfs(x, y - 1, res)
        
# N = int(input())
# graph = []
# for i in range(N):
#     graph.append(list(map(int, input())))

# # 모든 점에 관하여 탐색 수행
# res = 0
# num = []
# for x in range(N):
#     for y in range(N):
#         if graph[x][y] != 0:
#             num.append(0) # 새로운 단지 추가 
#             dfs(x, y, res)
#             res += 1 # 총 단지 갯수++
           
# print(res) 
# for i in sorted(num):
#     print(i)


# ---- bfs 풀이 ------
def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = 1 # 아파트 갯수
    queue = []
    queue.append((x, y))
    graph[x][y] = 0
    while queue:
        x, y = queue[0]
        del(queue[0])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            graph[nx][ny] = 0
            n += 1
    return n
    
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
    
# 모든 점에 관하여 탐색 수행
res = 0 # 단지 갯수
num = [] # 단지별 아파트 갯수
for x in range(N):
    for y in range(N):
        if graph[x][y] != 0:
            num.append(bfs(x, y))
            res += 1

print(res) 
for i in sorted(num):
    print(i)