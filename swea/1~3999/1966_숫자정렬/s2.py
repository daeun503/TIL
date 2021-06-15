import sys
sys.stdin = open('input.txt', "r")

T = int(input())


def partition(a, begin, end):
    # 중앙 값으로 피봇을 잡아준다.
    pivot = (begin + end) // 2
    L = begin
    R = end
    # R이 L보다 클 때
    while L < R :
        # 피봇보다 L값이 작으면 +1 해준다. 최종적으로 피봇보다 커진 L을 구한다.
        while a[L] < a[pivot] and L < R:
            L += 1
        # 피봇보다 R값이 작으면 -1 해준다. 최종적으로 피봇보다 작은 R을 구한다.
        while a[pivot] <= a[R] and L < R:
            R -= 1
        # 만약 L < R 이고 L이 피봇이면 피봇을 R로 바꾼다.
        if L < R:
            if L == pivot:
                pivot = R
        # L과 R을 바꾼다.
        a[L], a[R] = a[R], a[L]
    # 피봇과 R을 바꾼다.
    a[pivot], a[R] = a[R], a[pivot]
    return R


def quickSort(a, begin, end):
    if begin < end:
        pivot = partition(a, begin, end)
        quickSort(a, begin, pivot-1)
        quickSort(a, pivot+1, end)
    return a

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    quickSort(numbers, 0, len(numbers)-1)
    print(numbers)
