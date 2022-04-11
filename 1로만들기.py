# # https://youtu.be/vRFXpqWDbRU?t=3646

# # BFS
# from collections import deque
# X = int(input())
# isVisit = [False] * (X+1)
# isVisit[X] = True
# deq = deque([])
# count = 0
# deq.append(X)

# while deq:
#     for _ in range(len(deq)):    
#         n = deq.popleft()
#         if n == 1:
#             print(count)
#             deq = deque([])
#             break
#         # if n % 5 == 0 and not isVisit[int(n/5)]:
#         #     deq.append(int(n/5))
#         #     isVisit[int(n/5)] = True
#         if n % 3 == 0 and not isVisit[int(n/3)]:
#             deq.append(int(n/3))
#             isVisit[int(n/3)] = True
#         if n % 2 == 0 and not isVisit[int(n/2)]:
#             deq.append(int(n/2))
#             isVisit[int(n/2)] = True
#         if  not isVisit[n-1]:
#             deq.append(n-1)
#             isVisit[n-1] = True
#     count += 1
    
# BP

X = int(input())

d = [0] * (X+1)

for i in range(2, X+1):
    d[i] = d[i-1]+1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # if i % 5 == 0:
    #     d[i] = min(d[i], d[i//5]+1)
        
print(d[X])