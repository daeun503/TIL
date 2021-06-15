import sys
sys.stdin = open("input.txt")


# pick의 길이는 행의 인덱스,
# pick의 벨류는 열의 인덱스를 의미한다.
def my_func( pick, my_sum):
    global result
    r = len(pick)

    # IN에서 한줄에 하나씩 다 뽑았으면 끝냄
    # 지금 계산하고 있는 값이 기존에 저장한 result보다 작으면 새로 갱신
    if r == len(IN):
        if result >= my_sum:
            result = my_sum
        return

    # 유망하지 않으면 리턴하고 끝냄
    # (지금 계산하고 있는 값이 이미 구한 result보다 크면 유망X)
    if my_sum >= result:
        return

    # 유명하면 계속 진행
    # pick(뽑은 열들) 안에 c가 없으면 해당 c를 pick에 추가해서 재귀
    for c in range(len(IN)):
        if c not in pick:
            my_func(pick + [c], my_sum + IN[r][c])
            # line 27는 이렇게도 풀어 쓸 수 있다.
            # pick.append(c)
            # my_func(IN, pick, my_sum + IN[r][c])
            # pick.pop()

    # 결과 리턴
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    result = 999999999
    print("#{} {}".format(tc, my_func([], 0)))