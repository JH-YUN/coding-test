# https://www.acmicpc.net/problem/11657
# 최단거리, 벨만포드

import sys
import math

INF = math.inf
N, M = map(int, sys.stdin.readline().rstrip().split(' '))
distance = [INF] * (N+1)
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().rstrip().split(' '))
    adj[A].append((B, C)) 

# 초기값 세팅
distance[1] = 0
flag = True
# 다익스트라와 다르게 모든 간선을 체크
for n in range(N+1):
    for i in range(1, N+1):
        for node, dist in adj[i]:
            cost = distance[i] + dist
            if cost < distance[node]:
                # 음의 순환이 일어나는지 체크
                if n == N:
                    flag = False
                    break
                distance[node] = min(distance[i] + dist, distance[node])
                
if flag:
    for dist in distance[2:]:
        if dist < INF:
            print(dist)
        else:
            print(-1)
else:
    print(-1)