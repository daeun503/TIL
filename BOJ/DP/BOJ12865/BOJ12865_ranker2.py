import sys
from pandas import DataFrame
sys.stdin = open('input.txt')

# top-down
N, K = map(int, input().split())

# (1, 1) 부터 시작하기 위해 [0, 0] 삽입
IN = [[0, 0]]
for _ in range(N):
    IN.append(list(map(int, input().split())))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = IN[i][0]
        value = IN[i][1]

        # weight(선택한 물건의 무게) 보다 j(가용 무게)가 작으면 위의 값을 그대로 가져온다
        if j < weight:
            dp[i][j] = dp[i - 1][j]

        # weight 보다 j가 크면 화살표는 왼쪽에서도 올 수 있으니, 큰 값으로 갱신한다.
        # 왼쪽 화살표 => 이전 행 & 가용무게 - 선택 물건 무게 & 가치 더하기 => dp[i-1][j-weight] + value
        else:
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])

print(dp[N][K])
