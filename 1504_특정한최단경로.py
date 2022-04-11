# https://www.acmicpc.net/problem/1504
# 최단경로, 다익스트라
import sys
import heapq
import math

INF = math.inf
N, E = map(int, sys.stdin.readline().rstrip().split(' '))
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append((b, c))
    graph[b].append((a, c))

v, w = map(int, sys.stdin.readline().rstrip().split(' '))

def dijkstra(start):
    h = []
    distance = [INF] * (N+1)
    distance[start] = 0
    heapq.heappush(h, (0, start))
    
    while h:
        dist, node = heapq.heappop(h)
        # 이미 최적화가 완료된 노드 스킵
        if dist > distance[node]:
            continue
        for dest in graph[node]:
            cost = distance[node] + dest[1]
            if cost < distance[dest[0]]:
                distance[dest[0]] = cost
                heapq.heappush(h, (cost, dest[0]))
    return distance

def ansDikstra():
    distFromStart = dijkstra(1)
    distFromEnd = dijkstra(N)
    distBetween = dijkstra(v)[w]
    ans = min(distFromStart[v]+distFromEnd[w]+distBetween, distFromStart[w]+distFromEnd[v]+distBetween)
    if ans < INF:
        print(ans)
    else:
        print(-1)
        
# 플루이드-워셜 메모리 초과
def floyd():
    distance = [[INF for _ in range(E+1)] for _ in range(E+1)]
    
    for i in range(1, N+1):
        distance[i][i] = 0
        for node,dist in graph[i]:
            distance[i][node] = dist
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    ans = min(distance[1][v]+distance[v][w]+distance[w][N], distance[1][w]+distance[w][v]+distance[v][N])
    if ans < INF:
        print(ans)
    else:
        print(-1)
        
ansDikstra()