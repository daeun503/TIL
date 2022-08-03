# import sys
# sys.stdin = open("input.txt", "r")


def check_good(num):
    # -1 부터 -N//2까지 보면 됨 (그 이상은 길이 넘어가서 볼 필요 X) 
    for point in range(-1, -N//2 - 1, -1):
        # pattern이 동일하면 나쁜 수열
        pattern = num[point:]
        if num[point - len(pattern) : point] == pattern:
            return False
    # 끝날 때까지 걸리지 않으면 좋은 수열
    return True


def func(num):
    # 길이 N이면 그만두기
    if len(num) == N:
        print(num)
        exit()

    # 1, 2, 3 을 붙여서 순열 만들기 & 좋은 순열일 때만 재귀
    for i in ['1', '2', '3']:
        next_num = num + i
        if check_good(next_num):
            func(next_num)



N = int(input())
for j in ['1', '2', '3']:
    func(j)