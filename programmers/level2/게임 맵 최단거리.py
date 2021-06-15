def solution(maps):
    N = len(maps)
    M = len(maps[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    # 너비 우선 탐색 시작
    queue = [(0, 0)]
    maps[0][0] = 2
    
    while queue:
        r, c = queue.pop(0)
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if maps[nr][nc] == 1:
                    maps[nr][nc] = maps[r][c] + 1
                    queue.append((nr, nc))
                    
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1] - 1