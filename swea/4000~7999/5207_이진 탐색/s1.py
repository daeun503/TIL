import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def binary_search(IN: list, target: int, posit: str) -> int:
    Lp = 0
    Rp = len(IN) - 1

    while Lp <= Rp:
        mid = (Lp + Rp) // 2

        # m에 찾는 원소가 있을 경우
        if target == IN[mid]:
            return 1

        # 왼쪽에 대해 검사 & 연속 L이면 중단
        elif target < IN[mid]:
            if posit == 'L':
                return 0
            Rp = mid-1
            posit = 'L'

        # 오른쪽에 대해 검사 & 연속 R이면 중단
        else:
            if posit == 'R':
                return 0
            Lp = mid+1
            posit = 'R'

    # 탐색 실패
    return 0


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0
    for num in B:
        cnt += binary_search(A, num, '')

    print("#{} {}".format(tc, cnt))