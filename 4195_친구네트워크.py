# https://www.acmicpc.net/problem/4195
# Union-Find
import sys

def union(friends, a, b):
    a = friends[a]
    b = friends[b]
    # 부모를 합쳐주고 네트워크 수는 더해줌
    network = friends[a[0]][1] + friends[b[0]][1]
    friends[a[0]][1] = network 
    friends[b[0]][1] = network
    friends[a[0]][0] = friends[b[0]][0]
    
def find(friends, a):
    if a not in friends:
        friends[a] = [a, 1] # 본인이 네트워크에 연결되어있음
    if a != friends[a][0]:
        friends[a] = find(friends, friends[a][0])
    return friends[a]

T = int(input())
for _ in range(T):
    friends = {} # 친구의 이름을 key, value[0] 는 부모, value[1]은 연결된 네트워크 수
    F = int(input())
    for i in range(F):
        a, b = sys.stdin.readline().rstrip().split(' ')
        if find(friends, a)[0] != find(friends, b)[0]:
            union(friends, a, b)
        print(find(friends, a)[1])
    
            