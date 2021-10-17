
import sys
sys.stdin = open('input.txt')


# for tc in range(int(input())):

from collections import deque

N, K = map(int, input().split())

if N == K:
    print(0)
else:
    visited = [[]]
    KK = K

    dq = deque([(N, 0)])
    while dq:
        v, n = dq.popleft()

        tmp = []
        if 0 <= v - 1 <= 500000: tmp.append((v - 1, n + 1))
        if 0 <= v + 1 <= 500000: tmp.append((v + 1, n + 1))
        if 0 <= v * 2 <= 500000: tmp.append((v * 2, n + 1))

        KK = K + (n+1)*(n+2)//2
        if not (0 <= KK <= 500000):
            print(-1)
            break
        if (KK, n+1) in tmp:
            print(n+1)
            break

        if len(visited) != n+2:
            visited.append([])

        for w, m in tmp:
            if w not in visited[m]:
                visited[m].append(w)
                dq.append((w, m))