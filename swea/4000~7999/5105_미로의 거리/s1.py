import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


# 참고 : p_Queue - p_bfs구현 - s4.py (거리에 대한 정보)
# => 시작 위치(큐 초기값)로부터 임의의 위치 사이의 거리 구하기
for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input())) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result, cnt = 0, 0

    for r in range(N):
        for c in range(N):
            if IN[r][c] == 2: s = (r, c)  # 2이면 출발
            if IN[r][c] == 3: e = (r, c)  # 3이면 도착

    queue = [s]         # 시작지점 큐에 넣기
    IN[s[0]][s[1]] = 1  # 시작지점 방문 표시

    while queue:
        r, c = queue.pop(0)
        # 큐에서 꺼낸걸로 사방탐색
        for i in range(4):
            check_r = r + dr[i]
            check_c = c + dc[i]
            # 범위 내 일때
            if 0 <= check_r < N and 0 <= check_c < N:
                # 갈 수 있으면 큐에 넣고 거리+1 (=방문 표시)
                if IN[check_r][check_c] == 0:
                    queue.append((check_r, check_c))
                    IN[check_r][check_c] = IN[r][c] + 1

                # 도착지면 한칸 더 가면 되므로 +1 (시작/종료 위치 포함이므로 -2)
                if (check_r, check_c) == e:
                    result = IN[r][c] + 1 - 2
                    break

        if result : break  # 이중 반복문 종료용
    print("#{} {}".format(tc, result))
