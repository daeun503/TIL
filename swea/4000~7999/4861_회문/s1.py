import sys
sys.stdin = open("input.txt", "r")

# NxN 크기의 글자판에서 길이가 M인 회문
for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split())
    answer = ''
    matrix = [list(input()) for _ in range(N)]

    # matrix 회전시켜주기
    rotate = []
    for r in range(len(matrix[0])):
        tmp = []
        for c in range(len(matrix)):
            tmp += matrix[c][r]
        rotate.append(tmp)

    # 행 검사
    for row in matrix:
        for i in range(N-M+1):
            if M % 2:
                if row[i:i+(M//2)-1] == row[i+M:i+(M//2)+1:-1]:
                    answer = row[i:i + M]
            else:
                if row[i:i+(M//2)-1] == row[i+M:i+(M//2):-1]:
                    answer = row[i:i + M]

    # 열 검사
    for row in rotate:
        for i in range(N-M+1):
            if M % 2:
                if row[i:i+(M//2)-1] == row[i+M:i+(M//2)+1:-1]:
                    answer = row[i:i + M]
            else:
                if row[i:i+(M//2)-1] == row[i+M:i+(M//2):-1]:
                    answer = row[i:i + M]

    print("#{} {}".format(tc, ''.join(answer)))