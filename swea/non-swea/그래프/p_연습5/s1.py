"""
연습 문제5.
채점 완료 후 해당 화면을 캡처하여 폴더에 첨부하여 업로드 해주세요!

 - BOJ 2606 바이러스
 - 기본적인 그래프 탐색 문제
"""
import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

def bfs(s):
    q = [s]
    visited[s] = 1
    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)
    return sum(visited)


V = int(input())
E = int(input())
G = [set() for _ in range(V+1)]
visited = [0] *(V+1)
for _ in range(E):
    v, w = map(int, input().split())
    G[v].add(w)
    G[w].add(v)

print(bfs(1)-1)