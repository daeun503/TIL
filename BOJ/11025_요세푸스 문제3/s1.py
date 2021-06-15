import sys
sys.stdin = open('input.txt')



N, K = map(int, input().split())
gn = 0
for i in range(2, N+1):
    gn = (gn + K) % i
print(gn+1)