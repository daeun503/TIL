def solution(m, n, puddles):
    # 이거 그냥 경우의 수 최단거리 구하기 
    matrix = [[0]*(n+1) for _ in range(m+1)]
    # 침수지역 표시
    for x, y in puddles:
        matrix[x][y] = 'x'
    # 집의 위치
    matrix[1][1] = 1
    
    for r in range(m+1):
        for c in range(n+1):
            if r >= 1 and c >= 1 and matrix[r][c] == 0:
                if matrix[r-1][c] == 'x':
                    matrix[r][c] = matrix[r][c-1]
                elif matrix[r][c-1] == 'x':
                    matrix[r][c] = matrix[r-1][c]
                else:
                    matrix[r][c] = (matrix[r-1][c] + matrix[r][c-1]) % 1000000007
    
    return matrix[m][n]