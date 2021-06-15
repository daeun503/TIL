import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def merge(left, right):
    global cnt
    if left[-1] > right[-1]: cnt += 1

    Lp, Rp = 0, 0
    # left + right 길이만큼 고정 배열 만들기
    result = [0] * (len(left) + len(right))
    for p in range(len(result)):
        # 둘 다 리스트 인덱스 안쪽에 있으면
        if Lp < len(left) and Rp < len(right):
            if left[Lp] < right[Rp]:
                result[p] = left[Lp]
                Lp += 1
            else:
                result[p] = right[Rp]
                Rp += 1

        # 한 쪽이 리스트 인덱스 바깥에 있으면
        elif Lp < len(left):
            result[p] = left[Lp]
            Lp += 1
        else:
            result[p] = right[Rp]
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


