# swea 5250
import heapq
import sys
sys.stdin = open("input_77.txt")
from pandas import DataFrame

# 다익스트라 알고리즘
import heapq
def dijkstra():
    heap = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dist[0][0] = 0  # 시작 지점
    heapq.heappush(heap, (dist[0][0], 0, 0))

    while heap:
        cur_w, cur_r, cur_c = heapq.heappop(heap)

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                tmp = 1
                if H[nr][nc] > H[cur_r][cur_c]:
                    tmp += H[nr][nc] - H[cur_r][cur_c]

                if dist[cur_r][cur_c] + tmp < dist[nr][nc]:
                    dist[nr][nc] = dist[cur_r][cur_c] + tmp  # 최소 비용 갱신
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))    # heap에 추가
    return dist

# import heap 사용 X 버전
def dijkstra2():
    heap = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dist[0][0] = 0
    heap.append((dist[0][0], 0, 0))        # heappush 대신 append로 추가

    while heap:
        cur_w, cur_r, cur_c = heap.pop(0)  # heappop 대신 pop(0)으로 맨 앞의 값을 빼옴

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                tmp = 1
                if H[nr][nc] > H[cur_r][cur_c]:
                    tmp += H[nr][nc] - H[cur_r][cur_c]

                if dist[cur_r][cur_c] + tmp < dist[nr][nc]:
                    dist[nr][nc] = dist[cur_r][cur_c] + tmp
                    heap.append((dist[nr][nc], nr, nc))    # heappush 대신 append로 추가
    return dist


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    dist = [[999999] * N for _ in range(N)]
    dijkstra()
    print('#{} {}'.format(tc, dist[-1][-1]))