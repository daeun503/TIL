import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

for tc in range(1, 11):
    input() # tc 버리기
    IN = list(map(int, input().split()))

    # tmp가 양수면 i 빼서 뒤에 붙여주기
    i, tmp = 1, 1
    while tmp > 0 :
        tmp = IN.pop(0) - i
        IN += [0] if tmp <= 0 else [tmp]
        i = 1 if i == 5 else i+1

    print("#{}".format(tc), *IN)