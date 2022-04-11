# https://www.acmicpc.net/problem/1717
# Union-Find

import sys

sys.setrecursionlimit(100000)

def find(table, a):
    if table[a] != a:
        table[a] = find(table, table[a])
    return table[a]
    
def union(table, a, b):
    rootA = find(table, a)
    rootB = find(table, b)
    if rootA != rootB:
        if rootA < rootB:
            table[rootB] = rootA
        else:
            table[rootA] = rootB

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
# table = list(range(n+1))
table = [0] * (n+1)

for i in range(n+1):
    table[i] = i

for _ in range(m):
    op, a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if op == 0:
        union(table, a, b)
    elif op == 1:
        if find(table, a) == find(table, b):
            print('YES')
        else:
            print('NO')
