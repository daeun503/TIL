# https://ddiyeon.tistory.com/62 참고

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# i 번째 수를 포함하면서 j개의 구간을 갖는 배열
dp1 = [[0] + [-float('inf')] * M for _ in range(N + 1)]
# i 번째 수를 포함하지 않으면서 j개의 구간을 갖는 배열
dp2 = [[0] + [-float('inf')] * M for _ in range(N + 1)]

for i in range(1, N + 1):
    num = int(input())
    for j in range(1, min(M, (i+1)//2) + 1):
        # i-1 번째를 포함하면서 j개의 구간을 갖거나,
        # i-1 번째를 포함하지 않으면서 j-1개의 구간을 갖는다.
        # 그리고 i 번째를 포함시켜서 최종적으로 j개의 구간을 만든다.
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j-1]) + num

        # i-1 번째를 포함하면서 j개의 구간을 갖거나,
        # i-1 번째를 포함하지 않으면서 j개의 구간을 갖는다.
        dp2[i][j] = max(dp1[i-1][j], dp2[i-1][j])

print(max(dp1[N][M], dp2[N][M]))
