import sys
import heapq
import math
INF = math.inf
N, M, C = map(int, sys.stdin.readline().rstrip().split(' '))
graph = [[] for _ in range(N+1)] 
dis = [INF] * (N+1)
h = []
for i in range(1, M+1):
    X, Y, Z = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[X].append((Z, Y)) # (distance, destination)
    
# 초기 값 설정
dis[C] = 0
heapq.heappush(h, (0, C))

while h:
    distance, now = heapq.heappop(h)
    # 이미 최소거리가 확정된 경우 스킵
    if distance > dis[now]:
        continue
    for i in graph[now]:
        cost = distance + i[0]
        if cost < dis[i[1]]:
            dis[i[1]] = cost
            heapq.heappush(h, (cost, i[1]))

ansCnt = 0
ansMax = 0
for i in dis:
    # 도달할수 있는 노드 체크, 시작 노드 제외
    if i != INF and i != 0:
        ansCnt += 1
        ansMax = max(ansMax, i)
print(ansCnt, ansMax, sep = ' ')

# test input
# 3 2 1
# 1 2 4
# 1 3 2

# test output
# 2 4
                    
         
    
    