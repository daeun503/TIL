import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

# 해당 value를 기준으로 구간을 나눌 수 있는지
def isValid(value):
    # low, high값, 구간의 수 초기화
    low = high = IN[0]
    cnt = 1

    # 배열을 탐색하면서 최대값이 나오면 high 갱신, 최소값이 나오면 low 갱신
    for i in IN:
        high = max(high, i)
        low = min(low, i)

        # 최대 - 최소 (구간의 점수) 가 value보다 크면 새로운 구간으로 설정
        if high - low > value:
            cnt += 1
            low = high = i

    # 만들 수 있는 구간의 개수보다 cnt가 적으면 가능
    return M >= cnt
    
N, M = map(int, input().split())
IN = list(map(int, input().split()))

end = max(IN)
start = 0

# 이분 탐색
result = end
while start <= end:
    mid = (start + end) // 2

    if isValid(mid):
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)
