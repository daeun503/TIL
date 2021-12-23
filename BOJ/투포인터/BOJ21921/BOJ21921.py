import sys
sys.stdin = open("input.txt", "r")

N, X = map(int, input().split())
IN = list(map(int, input().split()))

s, e = 0, X
result = visit_count = sum(IN[:X])
count = 1

for XX in range(X, N):
    # 한 칸씩 옆으로 이동하면서 확인
    visit_count += IN[XX]
    visit_count -= IN[XX-X]

    if visit_count == result:
        count += 1
    elif visit_count > result:
        result = visit_count
        count = 1

if result:
    print(result)
    print(count)
else:
    print("SAD")
