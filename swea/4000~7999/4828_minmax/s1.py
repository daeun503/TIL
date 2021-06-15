import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    a_min, a_max = arr[0], arr[0]

    for a in arr:
       if a_min > a:
           a_min = a
       if a_max < a:
           a_max = a

    print('#{} {}'.format(tc, a_max - a_min))