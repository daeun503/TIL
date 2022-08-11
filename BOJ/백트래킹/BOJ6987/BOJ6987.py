import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

def func(idx, visited):
    global flag

    # 점수 끝까지 다 확인하면 종료
    if idx == 6 or flag:
        flag = 1
        return

    # win, draw, lose가 0, 0, 0이면 다음 나라(idx + 1)보기
    win, draw, lose = score[idx]
    if win == draw == lose == 0:
        func(idx + 1, [idx + 1])
        return

    # win이 있으면 다른 나라 패랑 함께 삭제하기
    if win:
        for i in range(6):
            if i != idx and score[i][2] and (i not in visited):
                score[idx][0] -= 1
                score[i][2] -= 1
                func(idx, visited + [i])
                score[idx][0] += 1
                score[i][2] += 1

    # draw가 있으면 위와 동일 (그냥 if로 하면 84%에서 시간초과)
    elif draw:
        for i in range(6):
            if i != idx and score[i][1] and (i not in visited):
                score[idx][1] -= 1
                score[i][1] -= 1
                func(idx, visited + [i])
                score[idx][1] += 1
                score[i][1] += 1

    # lose가 있으면 위와 동일 (그냥 if로 하면 84%에서 시간초과)
    elif lose:
        for i in range(6):
            if i != idx and score[i][0] and (i not in visited):
                score[idx][2] -= 1
                score[i][0] -= 1
                func(idx, visited + [i])
                score[idx][2] += 1
                score[i][0] += 1


ret = []
for _ in range(4):
    IN = list(map(int, input().split()))
    score = [[IN[3*i], IN[3*i + 1], IN[3*i + 2]] for i in range(6)]
    flag, start = 0, 1
    # 모든 국가의 win, draw, lose의 합이 5이 아니면 불가능 => 이거 없으면 61%에서 실패
    for i in range(6):
        if sum(score[i]) != 5:
            start = 0
            break
    # 위에서 불가능하면, func을 돌릴 필요 없음 => 이거 없으면 84%에서 시간초과
    if start:
        func(0, [0])
    ret.append(flag)
print(*ret)

