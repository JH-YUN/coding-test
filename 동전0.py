# 백준 
# https://www.acmicpc.net/problem/11047
# 그리디 
param = input()
param1 = param[0].split(' ')
N = int(param1[0])
K = param1[1]
A = []
for i in range(0,N):
    a = input()
    A.append(a)
    
res = 0
total = int(K)
for coin in reversed(A):
    coin = int(coin)
    if(total >= coin):
        res += int(total / coin)
        total = total % coin

print(res)

