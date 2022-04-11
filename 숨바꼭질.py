# 백준 
# https://www.acmicpc.net/problem/1697
# BFS
import sys
from collections import deque

LIMIT = 100001
N, K = map(int, sys.stdin.readline().rstrip().split(' '))
deq = deque([])
isVisit = [False] * LIMIT

deq.append(N)
isVisit[N] = True
second = 0
while True:
    temp = deque([])
    while deq:
        node = deq.popleft()
        if node == K:
            temp = False
            break
        if node + 1 < LIMIT and node + 1 >= 0 and not isVisit[node+1]:
            temp.append(node+1)
            isVisit[node+1] = True
        if node - 1 < LIMIT and node - 1 >= 0 and not isVisit[node-1]:
            temp.append(node-1)
            isVisit[node-1] = True
        if node * 2 < LIMIT and node * 2 >= 0 and not isVisit[node*2]:
            temp.append(node*2)
            isVisit[node*2] = True
    if not temp:
        break        
    deq = temp
    second += 1
        
print(second)

