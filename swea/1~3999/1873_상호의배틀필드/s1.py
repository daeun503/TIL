import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    GameMap = [list(input()) for _ in range(H)]
    N = int(input())
    IN = input()

    # 초기 방향과 그때의 r, c 위치 찾기
    pic_DIR = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    DIR, r, c = (0, 0), 0, 0
    for i in range(H):
        for j in range(W):
            if GameMap[i][j] in pic_DIR.keys():
                DIR = pic_DIR[GameMap[i][j]]   # DIR = DIR['<']
                r, c = i, j
                break

    str_DIR = {'U': (-1, 0, '^'), 'D': (1, 0, 'v'), 'L': (0, -1, '<'), 'R': (0, 1, '>')}
    for i in IN:
        # S가 들어오면 포탄의 방향은 내 방향. 벽만나거나 out할 때까지 직진시켜주기
        if i == 'S':
            shoot_r = r + DIR[0]
            shoot_c = c + DIR[1]
            # 바깥으로 나갈 때까지 반복. 도중에 벽 만나면 break
            while 0 <= shoot_r < H and 0 <= shoot_c < W:
                if GameMap[shoot_r][shoot_c] == '*':
                    GameMap[shoot_r][shoot_c] = '.'
                    break
                elif GameMap[shoot_r][shoot_c] == '#':
                    break
                # 물이거나 평지면 포탄의 위치 이동시켜준다.
                else:
                    shoot_r += DIR[0]
                    shoot_c += DIR[1]

        # U, D, L, R 이 들어오면, 내 방향은 새로운 방향으로 업데이트
        else:
            DIR = str_DIR[i]
            # 이동할 위치가 out하지 않으면서 평지라면 이동한다. 기존에 있던 자리는 .로 바꿔주기.
            if (0 <= r + DIR[0] < H and 0 <= c + DIR[1] < W) and GameMap[r + DIR[0]][c + DIR[1]] == '.':
                GameMap[r][c] = '.'
                r = r + DIR[0]
                c = c + DIR[1]
            # 새로 위치하는 곳 전차 방향 써주기
            GameMap[r][c] = DIR[2]

    print("#{} ".format(tc), end='')
    for i in GameMap:
        print(''.join(i))
