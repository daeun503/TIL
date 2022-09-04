# import sys
# sys.stdin = open('input.txt')


# 위 왼 아래 오
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]


def go_or_back(start, d, flag, end=None):
    nr, nc = start
    next_start = (0, 0)

    # 범위 안에 있으면
    while 0 <= nr < R and 0 <= nc < C:
        # flag = 1 (go): 이동할 수 있으면 방문 체크
        if flag and (IN[nr][nc] == '.'):
            IN[nr][nc] = 'O'
            next_start = (nr, nc)
        # flag = 0 (back): 이미 방문 체크 되어있으면 방문 풀기
        elif (not flag) and (IN[nr][nc] == 'O'):
            IN[nr][nc] = '.'
        else:
            break
        
        # end 지점에 도달했다면 종료
        if (nr, nc) == end:
            break

        # 다음 위치
        nr += dr[d]
        nc += dc[d]

    return next_start


def func(start, count):
    global result

    # 재귀
    r, c = start
    can_go = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 해당 방향으로 갈 수 있으면 쭉 이동하기
        if 0 <= nr < R and 0 <= nc < C and IN[nr][nc] == '.':
            can_go = 1
            # (nr, nc) 부터 쭉 이동하면서 방문체크 => next_start: 다음 시작점
            next_start = go_or_back((nr, nc), d, 1)
            func(next_start, count + 1)
            # 재귀 나온 후 next_start 부터 (nr, nc)까지 방문 해제 (방향은 반대 방향)
            go_or_back(next_start, (d + 2) % 4, 0, (nr, nc))
    
    # 종료 조건 => 갈 수 있는 곳이 없는 상태
    if not can_go:

        # 모든 칸을 방문했는지 확인
        board_count = 0
        for i in range(R):
            for j in range(C):
                board_count += 1 if IN[i][j] == 'O' else 0

        # board 칸을 모두 방문했다면 result 갱신
        if board_count == total_board_count:
            result = min(result, count)


count = 0
while 1:
    count += 1

    try:
        R, C = map(int, input().split())
        IN = [list(input()) for _ in range(R)]

        # board 칸의 개수 구하기
        total_board_count = 0
        for r in range(R):
            for c in range(C):
                total_board_count += 1 if IN[r][c] == '.' else 0
                       
        # 함수 시작 => 모든 위치에서 함수 실행하여 확인하기
        result = 99999999999999999
        for r in range(R):
            for c in range(C):
                if IN[r][c] == '.':
                    IN[r][c] = 'O'
                    func((r, c), 0)
                    IN[r][c] = '.'
            
        # 모든 빈 칸을 방문할 수 있는 경우가 없다면 -1
        if result == 99999999999999999:
            result = -1
        print(f'Case {count}: {result}')

    except:
        break
