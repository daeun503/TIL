# import sys
# sys.stdin = open("input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def func(r, c, count):
    global result

    result = max(result, count)

    # 재귀
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 범위 바깥이거나 이미 사용한 알파벳이면 X
        if not (0 <= nr < R and 0 <= nc < C) or IN[nr][nc] in alpa:
            continue
        # 갈 수 있는 곳이면 이동하기
        alpa.add(IN[nr][nc])
        func(nr, nc, count + 1)
        alpa.remove(IN[nr][nc])
        
R, C = map(int, input().split())
IN = [list(input()) for _ in range(R)]

r, c, result = 0, 0, 0
alpa = {IN[r][c]}

func(r, c, 1)
print(result)
