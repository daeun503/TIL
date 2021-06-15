import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 상하좌우 // 1 5 7 11
dr = [-1, 1, 0, 0, -1, 1, 1, -1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    IN = [list(map(int, input().split())) for _ in range(M)]

    # 초기화 작업 ///// 1은 흑돌, 2는 백돌 //////
    GameMap = [[0 for _ in range(N)] for _ in range(N)]
    GameMap[N//2][N//2] = 2
    GameMap[N//2 - 1][N//2 - 1] = 2
    GameMap[N//2][N//2 - 1] = 1
    GameMap[N//2 - 1][N//2] = 1

    # 입력 받기 (x, y)로 입력이 들어오면 => (y-1, x-1)로 입력  // IN[i] = [1, 2, 1] (i=0)
    for i in range(M):
        # 돌 두기.
        r = IN[i][1]-1
        c = IN[i][0]-1
        color = IN[i][2]
        GameMap[r][c] = color

        # 상대편 돌 뒤집는 로직
        for j in range(8):
            # check_r/c로 상하좌우대각선 살펴볼건데,
            check_r = r + dr[j]
            check_c = c + dc[j]

            # 일단 범위 내로 들어와야하고, 이동한 곳이 0이면 안되고, 지금 내 색 이어도 안돼. => 즉, 상대방 색만
            if (0 <= check_r < N and 0 <= check_c < N) and GameMap[check_r][check_c] != 0 and GameMap[check_r][check_c] != color:
                while 0 <= check_r < N and 0 <= check_c < N:
                    # 전진해서 마지막 끝이 0 이면 뒤집을 수 없음 (도중에 0을 만나면 x)
                    if GameMap[check_r][check_c] == 0:
                        break
                    # 전진해서 마지막 끝이 내 컬려면 뒤집을 수 있음. 되돌아오면서 뒤집기
                    elif GameMap[check_r][check_c] == color:
                        while check_r != r or check_c != c :
                            GameMap[check_r][check_c] = color
                            check_r -= dr[j]
                            check_c -= dc[j]
                        break
                    # 전진하고 있는 곳이 상대방 컬러면 더 전진할 수 있음.
                    else:
                        check_r += dr[j]
                        check_c += dc[j]

    # 출력용
    result = [0, 0]
    for i in GameMap:
        result[0] += i.count(1)
        result[1] += i.count(2)
    print("#{}".format(tc), *result)
