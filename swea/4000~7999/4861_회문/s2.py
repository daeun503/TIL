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
        cnt = 0
        tmp = []
        for i in row:
            if M % 2:        # 홀수일 때
                pass
            else:                       # 짝수일 때
                if cnt == M :
                    break
                if tmp[-1:] == [i]:     # tmp에 들어있는 마지막 값과 새로 들어오는 값이 같으면
                    tmp.pop()           # 기존에 들어있던 마지막 값을 pop해주고
                    cnt += 2            # cnt를 +2 해준다 (기존 값 + 새로 들어오려던 값)
                else:                   # tmp에 들어있는 마지막 값과 새로 들어오는 값이 다르면
                    tmp += [i]          # tmp에 새로운 값을 넣어준다
        answer = row[len(tmp):len(tmp) + M]  # 그 때의 row값이 answer# for문 결과 cnt값이 M과 같으면


    # 열 검사
    for row in rotate:
        cnt = 0
        tmp = []
        for i in row:
            if M % 2:                  # 홀수일 때
                pass
            else:                      # 짝수일 때
                if tmp[-1:] == [i]:    # tmp에 들어있는 마지막 값과 새로 들어오는 값이 같으면
                    tmp.pop()          # 기존에 들어있던 마지막 값을 pop해주고
                    cnt += 2           # cnt를 +2 해준다 (기존 값 + 새로 들어오려던 값)
                else:                  # tmp에 들어있는 마지막 값과 새로 들어오는 값이 다르면
                    tmp += [i]         # tmp에 새로운 값을 넣어준다
        if cnt == M:                                # for문 결과 cnt값이 M과 같으면
            answer = row[len(tmp):len(tmp)+M]       # 그 때의 row값이 answer

    print("#{} {}".format(tc, ''.join(answer)))