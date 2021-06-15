import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

for tc in range(1, 11):
    input()
    IN = [list(map(int, input())) for _ in range(16)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0

    r, c = 1, 1       # 시작 지점(고정)
    queue = [(r, c)]  # 큐 초기값
    IN[r][c] = 1      # 미로에 방문표시

    # 큐가 빌 때까지 반복해서 못 찾으면 0, 중간에 찾으면 1
    while queue:
        r, c = queue.pop(0)      # 큐에서 꺼내서
        for i in range(4):       # 그 기준으로 4방 탐색
            check_r = r + dr[i]
            check_c = c + dc[i]
            if IN[check_r][check_c] == 0:         # 해당 경로가 갈 수 있으면
                queue.append((check_r, check_c))  # 큐에 넣고
                IN[check_r][check_c] = 1          # 방문 표시
            elif IN[check_r][check_c] == 3:       # 종료 지점이면
                result = 1                        # 결과에 1 넣고 끝내기
                break
        if result == 1 : break      # 결과 나왔는데 괜히 while문 도는 것 방지

    print("#{} {}".format(tc, result))