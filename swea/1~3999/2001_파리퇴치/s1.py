import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())

for tc in range(1, T+1):
    # N : nxn 배열, M : mxm 파리채
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    # 기준 위치 (r,c) 로부터 mxm 면적 파리채 때릴 것
    for r in range(N-M+1):
        for c in range(N-M+1):
            # 파리채 면적으로 죽인 파리 계산
            num = 0
            for i in range(M):
                for j in range(M):
                    num += matrix[r+i][c+j]
            # 최대값 구하기
            if result < num : result = num

    print("#{} {}".format(tc, result))