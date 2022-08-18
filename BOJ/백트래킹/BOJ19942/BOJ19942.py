# import sys
# sys.stdin = open("input.txt", "r")
# from pandas import DataFrame

def func(pick, p, f, s, v, price):
    global result, result_pick

    # 가지치기: 가격이 이미 찾은 값보다 크면 볼 필요 X
    if price >= result:
        return

    # 종료 조건: 최소 영양 성분 이상이면 답 갱신
    if p >= mp and f >= mf and s >= ms and v >= mv:
        result = price
        result_pick = pick
        return

    # 재귀: 마지막 선택한 숫자 이후로 고른다. (1, 3, 5)와 (1, 5, 3)이 같기 때문.
    for i in range(pick[-1] + 1, N):
        # i 번째를 선택하지 않았으면 선택
        if i not in pick:
            pp, pf, ps, pv, pprice = IN[i]
            func(pick + [i], p + pp, f + pf, s + ps, v + pv, price + pprice)


N = int(input())
mp, mf, ms, mv = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

# 초기값 세팅 후 함수 실행
result = 999999999999999999999999999999
result_pick = []
for i in range(N):
    func([i], *IN[i])

# 출력: 인덱스가 1부터 시작이라 result_pick 에 1씩 더해줌
if result_pick:
    print(result)
    print(*map(lambda x: x+1, result_pick))
else:
    print(-1)