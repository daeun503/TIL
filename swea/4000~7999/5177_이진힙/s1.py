import sys
sys.stdin = open("input.txt")
from pandas import DataFrame


for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))

    heap = [0]
    for i in range(len(IN)):
        heap.append(IN[i])            # heap 에 원소 추가
        c = len(heap) - 1             # 원소를 추가한 현재 위치
        while heap[c//2] > heap[c]:   # 내 부모가 나보다 크면 교환
            heap[c//2], heap[c] = heap[c], heap[c//2]
            c = c//2                  # 내 부모 인덱스로

    result, N = 0, N//2      # 조상만 더하는 거니까 //2 해주고 시작
    while N:                 # //2 반복 해주면서 조상들 값 더하기
        result += heap[N]
        N //= 2
    print("#{} {}".format(tc, result))

