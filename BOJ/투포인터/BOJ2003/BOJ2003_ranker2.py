import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e, total = 0, 0, 0
result = 0

while 1:
    # total과 M이 같으면 result +1
    if total == M:
        result += 1

    # total이 M보다 같거나 크면 start +1
    if total >= M:
        total -= arr[s]
        s += 1
    # end가 끝인데 위 if에서 안걸렸으면 total < M이란 것이므로 break
    elif e == N:
        break
    # 아직 end가 끝이 아니고 total이 M보다 작으므로 end +1
    else:
        total += arr[e]
        e += 1

print(result)
