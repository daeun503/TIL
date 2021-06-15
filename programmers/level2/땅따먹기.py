def solution(land):
    N = len(land)

    # 하향식
    m = [land[0]] + [[0]*4 for i in range(N-1)]    # [N-1][4] 배열
    for i in range(1, N):
        m[i][0] = land[i][0] + max(m[i-1][1], m[i-1][2], m[i-1][3])
        m[i][1] = land[i][1] + max(m[i-1][0], m[i-1][2], m[i-1][3])
        m[i][2] = land[i][2] + max(m[i-1][0], m[i-1][1], m[i-1][3])
        m[i][3] = land[i][3] + max(m[i-1][0], m[i-1][1], m[i-1][2])
    return max(m[N-1])

    '''# 상향식 (이 더 빠름)
    m = [[0]*4 for i in range(N-1)] + [land[N-1]]   # [N-1][4] 배열
    for i in range(N-2, -1, -1):
        m[i][0] = land[i][0] + max(m[i+1][1], m[i+1][2], m[i+1][3])
        m[i][1] = land[i][1] + max(m[i+1][0], m[i+1][2], m[i+1][3])
        m[i][2] = land[i][2] + max(m[i+1][0], m[i+1][1], m[i+1][3])
        m[i][3] = land[i][3] + max(m[i+1][0], m[i+1][1], m[i+1][2])
    return max(m[0])'''