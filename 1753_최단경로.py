# https://www.acmicpc.net/problem/1753
# 최단경로, 다익스트라

import sys
import math
import heapq

INF = math.inf
V, E = map(int, sys.stdin.readline().rstrip().split(' '))
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
h = []
K = int(input())
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[u].append((v, w))

# 초기값
heapq.heappush(h, (0, K))
distance[K] = 0
while h:
    dist, node = heapq.heappop(h)
    # 이미 최적화가 끝난 노드일 경우 스킵
    if dist > distance[node]:
        continue
    for destination in graph[node]:
        cost = destination[1] + distance[node]
        if cost < distance[destination[0]]:
            distance[destination[0]] = cost
            heapq.heappush(h, (cost, destination[0]))

for dist in distance[1:]:
    if dist == INF:
        print('INF')
    else:
        print(dist)