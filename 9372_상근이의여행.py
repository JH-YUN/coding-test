# https://www.acmicpc.net/problem/9372

import sys
import collections

T = int(input())
for _ in range(T):
    # adj = [[] for _ in range(N+1)]
    # isVisit = [False for _ in range(N+1)]
    # dq = collections.deque([])
    N, M = map(int, sys.stdin.readline().rstrip().split(' '))
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    #     adj[a].append(b)
    #     adj[b].append(a)
    print(N-1)
    
    
    
        
