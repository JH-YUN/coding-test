# 백준 
# https://www.acmicpc.net/problem/2606
# DFS, BFS
def dfs(adj, node):
    visited.append(node)
    for i in adj[node]:
        if i not in visited:
            dfs(adj, i)
            
computer = int(input())
edgeCnt = int(input())
adj = [ []for _ in range(computer+1) ]
for i in range(edgeCnt):
    edge = list(map(int, input().split(' ')))
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])

visited = []

dfs(adj, 1)

# print(len(visited) - 1)






        
    
    