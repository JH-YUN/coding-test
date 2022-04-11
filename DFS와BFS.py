# 백준 
# https://www.acmicpc.net/problem/1260
# DFS, BFS

# 깊이우선탐색
def dfs(adj, isVisit, start):
    isVisit[start] = True
    dfsRes.append(str(start))
    for i in adj[start]: # 인접리스트 확인
        if not isVisit[i]: # 방문여부가 없을경우
            dfs(adj, isVisit, i) # DFS

# 너비우선탐색
def bfs(adj, isVisit, start):
    queue = [] # 큐 생성
    bfsRes.append(str(start))
    isVisit[start] = True
    queue.append(start) # 큐에 시작 노드 방문처리 후 넣기
    
    while queue: # 큐에 노드가 존재하면 계속 반복
        node = queue[0]
        del(queue[0])
        for i in adj[node]: # 노드의 방문하지 않은 인접노드 모두 방문처리 후 큐에 넣기
            if not isVisit[i]:
                bfsRes.append(str(i))
                isVisit[i] = True
                queue.append(i)
            

N, M, V = map(int, input().split(' '))
adj = [[]for _ in range(N+1)]

dfsRes = []
bfsRes = []
# 인접 리스트 생성
for i in range(M):
    edge = list(map(int, input().split(' ')))
    adj[edge[0]].append(edge[1])
    adj[edge[1]].append(edge[0])
    adj[edge[0]].sort()
    adj[edge[1]].sort()

# 방문 여부 체크배열
isVisit = [False] * (N + 1)
dfs(adj, isVisit, V)

isVisit = [False] * (N + 1)
bfs(adj, isVisit, V)

print(' '.join(dfsRes))
print(' '.join(bfsRes))

    
        
        
        

