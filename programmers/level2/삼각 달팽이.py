# 1회차
def solution(n):
    # 아래 오른쪽 대각선
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    
    # 빈 리스트 틀 만들어주기
    result = []
    for i in range(1, n+1):
        result.append([0]*i)
    
    j, r, c = 0, 0, 0
    for i in range(1, n*(n+1)//2 + 1):   # 1 ~ 마지막 수까지 for문
        result[r][c] = i             # 현재 있는 인덱스에 순서대로 i값 넣어주기
        nr = r + dr[j]               # 이동한 row 인덱스
        nc = c + dc[j]               # 이동한 column 인덱스
        
        # 만약에 이동한 인덱스가 범위를 초과하면 j를 이동시켜서 방향 바꿔주고 다시 이동시켜주기
        if not (0 <= nr < n and 0 <= nc < n) or result[nr][nc] != 0 :
            j = 0 if j == 2 else j+1
            nr = r + dr[j]
            nc = c + dc[j]
        # 이제 이동한 위치가 정상 위치니까 r, c에 제대로 넣어주기 
        r = nr
        c = nc
        
    answer = []
    for i in result:
        for j in i:
            answer.append(j)
    return answer