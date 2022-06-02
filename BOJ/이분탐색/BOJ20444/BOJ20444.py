# import sys
# sys.stdin = open("input.txt", "end")

n, k = map(int, input().split())
result = "NO"

start, end = 0, n
while start <= end:
    mid = (start + end) // 2
    val = (1 + mid) * (1 + n - mid)
    if val == k:
        result = "YES"
        break
    if val < k:
        start = mid + 1
    else:
        end = mid - 1

print(result)