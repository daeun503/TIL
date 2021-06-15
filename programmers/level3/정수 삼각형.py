def solution(triangle):
    # 이게 왜 백트래킹이 아니라 DP일까? 제한이 없어서, 작은 부분을 큰 부분으로 확장할 수 있기 때문?
    # 일단 그림으로 그려보니까 어떤 느낌인 지 알겠다!
    ttt = triangle
    N = len(ttt)
    
    # [][][0]에는 숫자, [][][1]에는 내가 될 수 있는 값들 모두 저장한 리스트. 이 값중에서 최대를 고른다.
    for r in range(N):
        for c in range(r + 1):
            ttt[r][c] = [ttt[r][c], []]
    ttt[0][0][1] = [ttt[0][0][0]]

    # 현재 [r][c]일 때 [r][c][1] 리스트에서 최댓값 찾아서 [r][c][0]으로 만들고(내가 될 수 있는 최댓값)
    # [r][c][0]이랑 자기 아래, 아래 대각선 값이랑 합해서 합한 쪽 [-][-][1] 리스트에 값 추가
    for r in range(N-1):
        for c in range(r + 1):
            ttt[r][c][0] = max(ttt[r][c][1])
            ttt[r + 1][c][1].append(ttt[r][c][0] + ttt[r + 1][c][0])  # 아래
            ttt[r + 1][c + 1][1].append(ttt[r][c][0] + ttt[r + 1][c + 1][0])  # 대각선

    # 삼각형 바닥 라인에서 최댓값 추출하기
    result = []
    for i in range(N):
        ttt[N - 1][i][0] = max(ttt[N - 1][i][1])
        result.append(ttt[N - 1][i][0])

    return max(result)