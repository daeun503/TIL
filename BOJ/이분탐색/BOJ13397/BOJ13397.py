import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

def isValid(midValue):
    low = high = IN[0]
    cnt = 1

    for i in IN:
        high = max(high, i)
        low = min(low, i)

        if high - low > midValue:
            cnt += 1
            low = high = i

    return M >= cnt
    
N, M = map(int, input().split())
IN = list(map(int, input().split()))

r = max(IN)
l = 0

# 이분 탐색
result = r
while l <= r:
    mid = (l + r) // 2

    if isValid(mid):
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1

print(result)