import sys
from pandas import DataFrame
sys.stdin = open("input.txt", "r")

# sort가 시간초과라면 x,y값 으로 인덱싱하기
n, m = map(int, input().split())
X, Y = [], []
for i in range(n):
    x, y, v = map(int, input().split())
    X.append((x, y, v))
    Y.append((y, x, v))
X.sort()
Y.sort(reverse=True)

ans = cnt = tmp = 0
x = y = 0
while x < n:
    xx = X[x][0]
    while x < n and X[x][0] == xx:
        if y < n and X[x][1] <= Y[y][0]:
            tmp += X[x][2]
            cnt += 1
        x += 1

    while cnt > m:
        yy = Y[y][0]
        while y < n and Y[y][0] == yy:
            if x >= n or Y[y][1] < X[x][0]:
                tmp -= Y[y][2]
                cnt -= 1
            # 윗줄에서 <=가 아니라 <인 이유: 이전의 while에서 x+=1된 형태이기 때문
            y += 1

    ans = max(ans, tmp)
print(ans)
