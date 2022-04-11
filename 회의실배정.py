# 백준
# https://www.acmicpc.net/problem/1931
# 그리디, 정렬
# 끝나는 시간을 기준으로 정렬하되 시작하는 시간도 두번째 조건으로 정렬해야한다
# 3 3, 1 3 일 경우 순서에 따라 두번째 회의는 잡히지 않기 때문
def main():
    N = int(input())
    times = []
    for _ in range(N):
        a, b = map(int, input().split(' '))
        time = (a, b)
        times.append(time)
    times = sorted(times, key=lambda time: (time[1], time[0]))

    max = times[0][1]
    del(times[0])

    res = 1
    for time in times:
        if time[0] >= max:
            max = time[1]
            res += 1
    print(res)
    
    main()