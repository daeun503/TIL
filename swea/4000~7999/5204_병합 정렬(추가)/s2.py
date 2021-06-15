import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

# https://nanarin.tistory.com/m/111
# 이거랑 근일님 내용 보고 했다 하지만 모르겠다..
# 이것도 재귀로 들어가는데 기존 내용보다 메리트가 있나?

def merge_sort(IN, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(IN, left, mid)
        merge_sort(IN, mid+1, right)

        p = j = 0
        k = i = left

        while i <= mid:
            buff[p] = IN[i]
            p += 1
            i += 1

        while i <= right and j < p:
            if buff[j] <= IN[i]:
                IN[k] = buff[j]
                j += 1
            else:
                IN[k] = IN[i]
                i += 1
            k += 1

        while j < p:
            IN[k] = buff[j]
            k += 1
            j += 1


for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    buff = [0] * len(IN)
    cnt = 0
    merge_sort(IN, 0, len(IN)-1)
    print(IN)


###################################################

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