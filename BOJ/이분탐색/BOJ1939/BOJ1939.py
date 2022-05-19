from collections import defaultdict


def bfs(weight):
    visit[A] = 1
    q = [A]
    while q:
        current = q.pop(0)
        # 다음 위치와 다음 위치로 갈 수 있는 중량
        for next, next_w in matrix[current]:
            # 아직 방문 안 했고 다음 위치로 갈 수 있는 중량 내이면 이동
            if not visit[next] and weight <= next_w:
                q.append(next)
                visit[next] = 1
                # 도착 위치면 true 반환
                if next == B:
                    return True
    return False


N, M = map(int, input().split())
matrix = defaultdict(list)
for _ in range(M):
    i, j, k = map(int, input().split())
    matrix[i].append([j, k])
    matrix[j].append([i, k])
A, B = map(int, input().split())

# 이분탐색
low, high = 1, 1000000000
while low <= high:
    visit = [0] * (N + 1)
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)