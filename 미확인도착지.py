# https://www.acmicpc.net/problem/9370
# 최단거리

import sys
import math
import heapq

def dijkstra(start, adj):
    distance = [INF for _ in range(n+1)]
    h = []
    distance[start] = 0
    heapq.heappush(h, (0, start))
    
    while h:
        curDist, curNode = heapq.heappop(h)
        if curDist > distance[curNode]:
            continue
        for destNode, destDist in adj[curNode]:
            cost = destDist + curDist
            if cost < distance[destNode]:
                distance[destNode] = cost
                heapq.heappush(h, (cost, destNode))
    return distance

INF = math.inf
T = int(input())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().rstrip().split(' '))
    s, g, h = map(int, sys.stdin.readline().rstrip().split(' '))
    destination = []
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().rstrip().split(' '))
        adj[a].append((b, d))
        adj[b].append((a, d))
    for _ in range(t):
        destination.append(int(input()))
    
    sDist = dijkstra(s, adj)
    gDist = dijkstra(g, adj)
    hDist = dijkstra(h, adj)
    
    ans = []
    # 목적지 걸러내기
    for dest in destination:
        # # 출발지에서 목적지로 가지 못하는경우
        # if sDist[dest] == INF:
        #     continue
        # # 경유지에서 목적지로 가지 못하는경우
        # if gDist[dest] == INF or hDist[dest] == INF:
        #     continue
        
        dist = min(sDist[g] + gDist[h] + hDist[dest], sDist[h] + hDist[g] + gDist[dest])
        # 경유지를 거쳐가는 비용이 최적비용이 아닌경우
        if dist == INF or dist != sDist[dest]:
            continue
        ans.append(dest)
    
    for dest in sorted(ans):
        print(dest, end = ' ')

# 플루이드 워셜 - 시간초과
# import sys
# import math
# INF = math.inf
# T = int(input())
# for _ in range(T):
#     n, m, t = map(int, sys.stdin.readline().rstrip().split(' '))
#     s, g, h = map(int, sys.stdin.readline().rstrip().split(' '))
#     distance = [[INF for _ in range(n+1)] for _ in range(n+1)]
#     destination = []

#     for _ in range(m):
#         a, b, d = map(int, sys.stdin.readline().rstrip().split(' '))
#         distance[a][b] = d
#         distance[b][a] = d

#     for _ in range(t):
#         destination.append(int(input()))

#     for i in range(n):
#         distance[i][i] = 0
        
#     # 플루이드 - 워셜
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             for j in range(1, n+1):
#                 distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])
#     ans = []
#     for dest in destination:
#         # 목적지까지 가지 못할 경우
#         if distance[s][dest] == INF:
#             continue
#         # 경유지에서 목적지로 가지 못할경우
#         if distance[g][dest] == INF or distance[h][dest] == INF:
#             continue
#         # 경유지를 통해 가는 경우가 최적의 수가 아닐 경우
#         if min(distance[s][g] + distance[g][h] + distance[h][dest], distance[s][h]+distance[h][g]+distance[g][dest]) != distance[s][dest]:
#             continue
#         ans.append(dest)
        
#     for dest in sorted(ans):
#         print(dest, end = ' ')