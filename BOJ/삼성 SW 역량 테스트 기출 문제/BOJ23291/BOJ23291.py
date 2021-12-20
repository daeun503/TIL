import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame


# 어항 공중 부양
def stack_fishbowls(height, stack_width, total_width, fishbowls):
    # 공중 부양 시키는 것이 불가능하면 return
    if height > total_width - stack_width:
        return fishbowls

    # 다음 단계 공중 부양은 높이 stack_width + 1 x 너비 total_width - stack_width
    h, w = stack_width + 1, total_width - stack_width
    next_fishbowls = [[-1]*w for _ in range(h)]
    for stack_h in range(height):
        for stack_w in range(stack_width):
            next_fishbowls[stack_w][stack_h] = fishbowls[(height-1) - stack_h][stack_w]
    for non_stack_w in range(w):
        next_fishbowls[-1][non_stack_w] = fishbowls[-1][stack_width + non_stack_w]

    # 다음 단계로
    fishbowls = stack_fishbowls(stack_width + 1, height, total_width - stack_width, next_fishbowls)
    return fishbowls


# 어항 공중 부양 2
def stack_fishbowls2(fishbowls):
    top = fishbowls[:N//2][::-1]
    down = fishbowls[N//2:]
    fishbowls = [top, down]

    half = len(top) // 2
    next_fishbowls = [[0] * half for _ in range(4)]
    # 왼쪽 절반은 공중부양
    for r in range(2):
        for c in range(half):
            next_fishbowls[r][c] = fishbowls[1-r][half-1-c]

    # 오른쪽 절반은 그대로
    for r in range(2):
        for c in range(half, len(top)):
            next_fishbowls[r+2][c-half] = fishbowls[r][c]

    return next_fishbowls


# 어항에 있는 물고기 수 조절
def fish_count(fishbowls):
    R, C = len(fishbowls), len(fishbowls[0])
    next_fishbowls = [i[:] for i in fishbowls]

    for r in range(R):
        for c in range(C):
            # 비어있으면 패스
            if fishbowls[r][c] == -1:
                continue

            for dr, dc in [(0, 1), (1, 0)]:
                nr = r + dr
                nc = c + dc
                # 범위 내이고, 물고기가 있는 어항이면
                if 0 <= nr < R and 0 <= nc < C and fishbowls[nr][nc] != -1:
                    fish_diff = fishbowls[r][c] - fishbowls[nr][nc]
                    # 5로 나눈 몫이 1 이상이면
                    d = abs(fish_diff) // 5
                    if d > 0:
                        # 양수이면, r,c 에 있는 물고기가 많다.
                        if fish_diff > 0:
                            next_fishbowls[r][c] -= d
                            next_fishbowls[nr][nc] += d
                        else:
                            next_fishbowls[r][c] += d
                            next_fishbowls[nr][nc] -= d

    # 일렬로 놓기
    result = []
    for c in range(C):
        for r in range(R-1, -1, -1):
            if next_fishbowls[r][c] != -1:
                result.append(next_fishbowls[r][c])

    return result


N, K = map(int, input().split())
fishbowls = list(map(int, input().split()))

result = 0
fish_diff = float('inf')
while K < fish_diff:

    # 1. 물고기 수가 가장 적은 어항에 한 마리 넣는다.
    fish_min = min(fishbowls)
    for idx in range(len(fishbowls)):
        if fishbowls[idx] == fish_min:
            fishbowls[idx] += 1

    # 2. 어항을 쌓는다.
    top = [fishbowls.pop(0)] + [0] * (len(fishbowls) - 1)
    next_fishbowls = [top, fishbowls]
    fishbowls = stack_fishbowls(2, 1, len(fishbowls), next_fishbowls)

    # 3. 물고기 수 조절
    fishbowls = fish_count(fishbowls)

    # 4. 두 번째 방법으로 어항을 쌓는다.
    fishbowls = stack_fishbowls2(fishbowls)

    # 5. 물고기 수 조절
    fishbowls = fish_count(fishbowls)

    # 6. 물고기 가장 많은 어항, 적은 어항 차이 확인
    fish_diff = max(fishbowls) - min(fishbowls)

    # 어항 정리 횟수
    result += 1

print(result)
