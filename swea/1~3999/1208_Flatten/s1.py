import sys
sys.stdin = open("input.txt", "r")

# N: 덤프 횟수, arr: 초기 상자 높이
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    box_height = [0] * 101

    # h: 상자의 높이 / hox_height[h]: h 높이의 상자가 몇 개
    for h in arr:
        box_height[h] += 1

    # 최소 상자의 높이
    dump, acc, h = 0, 0, 0
    while dump <= N:
        h += 1
        acc += box_height[h]
        dump += acc
    min_h = h

    # 최대 상자의 높이
    dump, acc, h = 0, 0, 101
    while dump <= N:
        h -= 1
        acc += box_height[h]
        dump += acc
    max_h = h

    print('#{} {}'.format(tc, max_h - min_h))
