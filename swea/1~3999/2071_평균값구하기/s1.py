import sys
sys.stdin = open('input.txt')

N = int(input())

for _ in range(N):
    print('#{} {}'.format(_+1, round(sum(map(int, input().split()))/10)))