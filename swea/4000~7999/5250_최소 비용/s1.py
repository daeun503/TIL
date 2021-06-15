import sys
import heapq
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

import heapq
def dijkstra():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    heap = []
    dist[0][0] = 0                            # 시작점 초기화 -> (0, 0)은 0이라는 비용을 지불하여 갈 수 있는 곳
    heapq.heappush(heap, (dist[0][0], 0, 0))  # (가중치, (행, 열))

    # heap이 비어있음이 의미하는 것은?
    # 경로 자체를 어떻게 갔는지는 모르지만 (0, 0)에서 시작하여 어떤 지점까지 가는데 필요한 최소 비용은 모두 구해졌다는 것
    while heap:
        # 어차피 기본 min_heap이기 때문에 가중치의 값이 작은 것부터(가중치가 같다면 행 -> 열 순서 동일 적용) pop
        # 가중치, 행, 열 순
        cur_w, cur_r, cur_c = heapq.heappop(heap)
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            # nr, nc가 이동할 수 있는 범위내면 이동 & 거리 확정 안된 곳이면
            if 0 <= nr < N and 0 <= nc < N:
                # 기본적으로 이동할 수 있으니까 1 더해주고
                tmp_dist = dist[cur_r][cur_c] + 1
                # 높이차이가 나면 그 만큼 더해준다
                if IN[cur_r][cur_c] < IN[nr][nc]:
                    tmp_dist += (IN[nr][nc] - IN[cur_r][cur_c])
                # 연료소비량이 더 적으면 갱신
                if dist[nr][nc] > tmp_dist:
                    dist[nr][nc] = tmp_dist
                    heapq.heappush(heap, (dist[nr][nc], nr, nc))


for tc in range(1, int(input())+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    dist = [[987654321] * N for _ in range(N)]  # 비용 초기화
    dijkstra()
    # print(DataFrame(dist))

    print("#{} {}".format(tc, dist[N-1][N-1]))