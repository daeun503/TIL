import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    IN = list(map(int, input().split()))
    print("#{} {}".format(tc, IN[M % N]))
