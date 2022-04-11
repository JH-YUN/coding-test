import math
INF = math.inf
N, M = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]
distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
for _ in range(1, M+1):
    i, j = map(int, input().split(' '))
    graph[i].append(j)
    graph[j].append(i)
X, K = map(int, input().split(' '))

def floyd():
    for i in range(1, N+1):
        distance[i][i] = 0
        for j in graph[i]:
            distance[i][j] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
                
    ans = distance[1][K] + distance[K][X]
    if ans == INF:
        print(-1)
    else:
        print(ans)
        
def dijkstra(start, destination):
    import heapq
    distance = [INF] * (N+1)
    h = []
    heapq.heappush(h, (0, start)) # distance, node
    distance[start] = 0

    while h:
        dist, node = heapq.heappop(h)
        # 이미 최적화가 끝났을 경우 스킵
        if dist > distance[node]:
            continue
        for i in graph[node]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(h, (cost, i))
                
    return distance[destination]
    
ans = dijkstra(1, K) + dijkstra(K, X)
if ans == INF:
    print(-1)
else:
    print(ans)
        

# # test input
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# # test output
# 3