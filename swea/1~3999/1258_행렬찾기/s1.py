import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# set을 통해 직사각형 왼쪽 모서리를 구하고 시작했는데 굳이?? 이럴 필요 없었던거 같다.
# 그냥 0 나오다가 숫자가 나오면 cnt 하면 될 것 같은데..... 기껏 쓴걸 지우긴 아깝고 그런 느낌..
for tc in range(1, int(input())+1):
    N = int(input())
    IN = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]

    # 0 다음에 숫자가 오는 좌표를 row, col로 세서 교집합을 구하면 직사각형 왼쪽 상단 edge
    R, C = set(), set()
    for r in range(N):
        for c in range(N):
            if IN[r][c-1] == 0 and IN[r][c] != 0: R.add((r, c))
            if IN[c-1][r] == 0 and IN[c][r] != 0: C.add((c, r))
    edge = list(R & C)

    # 보관해둔 모서리를 pop해서 모서리로부터 행, 열을 센다.
    result = []
    while edge:
        r, c = edge.pop()        # 보관한 모서리를 pop
        tmp = [0, 0, 0]          # [행, 열, 크기]
        i, j = 0, 0              # 행 cnt, 열 cnt
        while IN[r+i][c] != 0:   # 모서리에서 시작해서 행에 0이 나올때까지
            tmp[0] += 1          # 행 크기를 +1 한다.
            i += 1
        while IN[r][c+j] != 0:   # 모서리에서 시작해서 열에 0이 나올때까지
            tmp[1] += 1          # 열 크기를 +1 한다.
            j += 1
        tmp[2] = tmp[0] * tmp[1] # 크기
        result.append(tmp)       # 한 부분 행렬 구했으면 더해주기

    # 행을 기준으로 정렬했다가 크기를 기준으로 정렬하기
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[2])

    # 출력용
    answer = []
    for tmp in result:
        tmp.pop()
        answer += tmp
    print("#{} {}".format(tc, len(result)), *answer)
