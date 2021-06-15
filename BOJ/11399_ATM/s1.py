import sys
sys.stdin = open('input.txt')


N = int(input())
Times = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(N):
    result += (i+1) * Times[i]
print(result)

