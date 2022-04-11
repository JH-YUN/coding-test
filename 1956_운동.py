# https://www.acmicpc.net/problem/1956
# 최단거리, 다익스트라
# pypy로 제출, python으로 제출하면 시간초과뜸;

# ---다익스트라---#
import sys
import math
import heapq

INF = math.inf
v, e = map(int, sys.stdin.readline().rstrip().split(' '))
distance = [[INF for _ in range(v+1)] for _ in range(v+1)]
h = []
adj = [[] for _ in range(v+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    adj[a].append((b, c))
    
for i in range(1, v+1):
    distance[i][i] = 0
    heapq.heappush(h, (0, i)) # cost, node
    while h:
        dist, curNode = heapq.heappop(h)
        # 이미 최적화가 완료된 경우 스킵
        if dist > distance[i][curNode]:
            continue
        for destNode, dest in adj[curNode]:
            cost = dest + distance[i][curNode]
            if cost < distance[i][destNode]:
                distance[i][destNode] = cost
                heapq.heappush(h, (cost, destNode))

ans = INF
for i in range(1, v+1):
    for j in range(1, v+1):
        if distance[i][j] < INF and distance[i][j] != 0:
            ans = min(ans, distance[i][j] + distance[j][i])

if ans < INF:
    print(ans)
else:
    print(-1)


# -----플루이드 워셜-----#
# import sys
# import math

# INF = math.inf
# v, e = map(int, sys.stdin.readline().rstrip().split(' '))
# distance = [[INF for _ in range(v+1)] for _ in range(v+1)]

# for _ in range(e):
#     a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
#     distance[a][b] = c

# for i in range(1, v+1):
#     distance[i][i] = 0

# for k in range(1, v+1):
#     for i in range(1, v+1):
#         for j in range(1, v+1):
#             distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])


# ans = INF
# for i in range(1, v+1):
#     for j in range(1, v+1):
#         if distance[i][j] < INF and distance[i][j] != 0:
#             ans = min(ans, distance[i][j] + distance[j][i])

# if ans < INF:
#     print(ans)
# else:
#     print(-1)
    
    