import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())

# txt에서 target이 몇번 나오는지 세는 함수
def search(txt, target):
    cnt = 0
    for i in range(len(txt)):
        if txt[i] == target[0]:
            if txt[i:i + len(target)] == target:
                cnt += 1
    return cnt

for tc in range(1, T+1):
    N, K = map(int, input().split())

    # 상하좌우에 0 넣어준 매트릭스 만들기 (1차원 리스트임)
    matrix = ['0'*(N+2)]+['0'+input().replace(' ','')+'0' for _ in range(N)]+['0'*(N+2)]
    target = '0' + '1' * K + '0'  # 찾아야하는 target
    cnt = 0

    # rotated_box = [''.join(char) for char in list(zip(*box))]
    # 열 우선순회로 회전한 매트릭스 만들기
    rotate = []
    for r in range(len(matrix[0])):
        tmp = ''
        for c in range(len(matrix)):
            tmp += matrix[c][r]
        rotate.append(tmp)

    # 정방향 매트릭스 row에서 target이 몇번 나오는지?
    for row in matrix:
        cnt += search(row, target)

    # 회전한 매트릭스 row에서 (정방향에선 column) target이 몇번 나오는지?
    for column in rotate:
        cnt += search(column, target)

    print("#{} {}".format(tc, cnt))

