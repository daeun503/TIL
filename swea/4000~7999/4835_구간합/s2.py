import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):

    N, M = list(map(int, input().split()))
    IN = list(map(int, input().split()))

    a = []
    for i in range(N-M+1):
        a += [sum(IN[i:i+M])]

    print("#{} {}".format(tc, max(a)-min(a)))
