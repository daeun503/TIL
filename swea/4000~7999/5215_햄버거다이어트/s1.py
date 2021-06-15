import sys
sys.stdin = open("input.txt", "r")


def my_func(IN, pick, my_T, my_K):
    global result # 맛 점수

    # 종료조건 & 유망성 검사

    # 칼로리가 넘쳤을 때
    if my_K > L:
        my_K -= IN[pick[-1]][1]
        my_T -= IN[pick[-1]][0]
        pick.pop()
        if my_T > result:
            result = my_T
        return
    # 칼로리가 넘치지 않았을 때
    else:
        if len(pick) == N:
            if my_T > result:
                result = my_T
                return
        else:
            if my_T > result:
                result = my_T


    for r in range(N):
        if r not in pick:
            my_func(IN, pick + [r], my_T + IN[r][0], my_K + IN[r][1])

    # 결과 리턴
    return result



# N: 재료의 수, L: 제한 칼로리 //// T: 맛 점수 K: 칼로리 /// (T, K)
for tc in range(1, int(input())+1):
    global N, L
    N, L = map(int, input().split())
    IN = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    print("#{} {}".format(tc, my_func(IN, [], 0, 0)))