# https://www.acmicpc.net/problem/10217
# 최단거리, 다익스트라, DP

# 다익스트라로 풀시 시간내로 풀기힘듬 DP로 푼다
# DP[dest][cost] = dist 일때 (dest = 목적지, cost = 비용, dist = 거리)
# DP[nextDest][cost + nextCost] = min (DP[nextDest][cost+nextCost], DP[dest][cost] + nextDist) 단 cost + nextCost < 최대 비용 

import sys
import heapq
import math

INF = math.inf
NUM = int(input())
for _ in range(NUM): 
    N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))
    distance = [[INF for _ in range(M+1) ] for _ in range(N+1)] # distance[dest][cost] = time
    adj = [[] for _ in range(N+1)] 
    h = []

    for i in range(K):
        u, v, c, d = map(int, sys.stdin.readline().rstrip().split(' '))
        adj[u].append((v, c, d)) 

    distance[1][0] = 0
    
    for j in range(M+1):
        for i in range(1, N+1):
            if distance[i][j] == INF:
                continue
            for dest, destCost, destDist in adj[i]:
                if destCost+j > M:
                    continue
                distance[dest][j+destCost] = min(distance[dest][j+destCost], distance[i][j] + destDist)
    ans = min(distance[N])
    
    if ans < INF:
        print(ans)
    else:
        print('Poor KCM')