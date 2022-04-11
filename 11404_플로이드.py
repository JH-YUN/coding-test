# https://www.acmicpc.net/problem/11404
# 최단거리, 플로이드 워셜

import sys
import math

INF = math.inf
n = int(input())
m = int(input())
distance = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split(' '))
    distance[a][b] = min(distance[a][b], c)

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] < INF:
            print(distance[i][j], end = ' ')
        else:
            print(0, end = ' ')
    print('')
