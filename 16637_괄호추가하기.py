# https://www.acmicpc.net/problem/16637

N = int(input())
cal = input()

opNum = N / 2 # 연산자의 갯수




def DFS(idx, result):
    

def calculate(a, op, b):
    a = int(a)
    b = int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    