import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def merge(left, right):
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크면 +1
    global cnt
    if left[-1] > right[-1] : cnt += 1

    # merge
    result = []
    Lp, Rp = 0, 0  # L pointer, R pointer

    # Lp, Rp가 두 리스트의 인덱스 바깥으로 나갈때까지
    while Lp < len(left) or Rp < len(right):
        # 둘 다 리스트 인덱스 안쪽에 있으면
        if Lp < len(left) and Rp < len(right):
            if left[Lp] < right[Rp]:
                result.append(left[Lp])
                Lp += 1
            else:
                result.append(right[Rp])
                Rp += 1
        # 한 쪽이 리스트 인덱스 바깥에 있으면
        elif Lp < len(left):
            result.append(left[Lp])
            Lp += 1
        else:
            result.append(right[Rp])
            Rp += 1

    return result


def merge_sort(IN):
    # 길이가 1이면 그냥 리턴
    if len(IN) <= 1:
        return IN
    # 길이가 2이상이면 반으로 가르기
    mid = len(IN) // 2
    left = merge_sort(IN[:mid])
    right = merge_sort(IN[mid:])
    return merge(left, right)


for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    cnt = 0
    sort_IN = merge_sort(IN)
    print("#{} {} {}".format(tc, sort_IN[N//2], cnt))


