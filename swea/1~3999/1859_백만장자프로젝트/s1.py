import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    IN = list(map(int, input().split()))

    result = 0
    while IN:
        # 가격이 max인 곳과 그 곳의 idx를 찾는다.
        # max_price = max(IN)
        # max_idx = IN.index(max_price)
        max_price = IN[0]
        max_idx = 0
        for idx, value in enumerate(IN):
            if max_price <= value:
                max_price = value
                max_idx = idx

        # max 가격과 매매가 가격의 차이를 빼서 더한다.
        for i in range(max_idx):
            result += max_price - IN[i]

        # max인 날 다음날부터로 IN을 재정의해서 반복한다.
        IN = IN[max_idx+1:]

    print("#{} {}".format(tc, result))