import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


def partition(arr, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while arr[L] < arr[pivot] and L < R:
            L += 1
        while arr[pivot] <= arr[R] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
    arr[pivot], arr[R] = arr[R], arr[pivot]
    return R


def quick_sort(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        quick_sort(arr, begin, p-1)
        quick_sort(arr, p+1, end)


for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    quick_sort(IN, 0, N-1)
    print("#{} {}".format(tc, IN[N//2]))
