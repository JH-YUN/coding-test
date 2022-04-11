# 백준 
# https://www.acmicpc.net/problem/7576
# BFS
import sys
from collections import deque
def bfs(deq):
    global notGrowCount
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    while True:
        temp = deque([])
        while deq:
            x, y = deq.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 1 or ny < 1 or nx > N or ny > M:
                    continue
                if graph[nx][ny] == 0:
                    temp.appendleft((nx, ny))
                    graph[nx][ny] = 1
                    notGrowCount -= 1
        if not temp:
            break
        deq = temp
        count += 1
    return count

M, N = map(int, sys.stdin.readline().split(' '))
graph = []
deq = deque([])
notGrowCount = 0 # 익지 않은 토마토 갯수
graph.append([-1] * (M+1))
for x in range(1, N+1):
    line = [-1]+list(map(int, sys.stdin.readline().split(' ')))
    y = 0
    for i in line:
        if i == 0:
            notGrowCount += 1
        elif i == 1:
            deq.appendleft((x, y))
        y += 1
    graph.append(line)
            
ans = bfs(deq)

if notGrowCount > 0:
   print(-1)
else: 
    print(ans)

