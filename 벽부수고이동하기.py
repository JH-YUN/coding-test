# 백준 
# https://www.acmicpc.net/problem/2206
# BFS
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
isVisit = []
for x in range(N):
    line = list(sys.stdin.readline().rstrip())
    graph.append(line)
    # isVisit.append([[False, False]*len(line)])
    isVisit.append([[False, False] for _ in range(len(line))])

deq = deque([])
deq.append((0, 0, 0))
isVisit[0][0][0] = True
# print(isVisit)
count = 0
answer = -1
while deq:
    count += 1
    for _ in range(len(deq)):
        x, y, isDestroy = deq.popleft()
        if x == N-1 and y == M-1:
            answer = count
            deq = deque([])
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if isVisit[nx][ny][isDestroy]:
                continue
            if graph[nx][ny] == '0':
                deq.append((nx, ny, isDestroy))
                isVisit[nx][ny][isDestroy] = True
            if graph[nx][ny] == '1' and isDestroy == 0: # 아직 벽을 부순적이 없을 경우 벽 부수는 경우 추가
                deq.append((nx, ny, 1))
                isVisit[nx][ny][1] = True

print(answer)
                
        
    
    
    
# 5 5
# 00000
# 11101
# 00001
# 01111
# 00010
    
