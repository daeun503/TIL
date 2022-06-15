from collections import defaultdict
import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")

# 모기가 들어오면 +1, 나가면 -1
T = int(input())
IO = defaultdict(int)
for _ in range(T):
    s, e = map(int, input().split())
    IO[s] += 1
    IO[e] -= 1
IO_time = sorted(IO.keys())

max_range = [0, 0]
max_count = -1
end_edit_flag = 0

# 모기의 입출력을 보면서 들어오면 +1, 나가면 -1
current = 0
for time in IO_time:
    current += IO[time]
    
    # 만약 모기가 들어와서 최고값을 갱신하면 새로운 범위로 체크
    if current > max_count:
        max_count = current
        max_range[0] = time
        end_edit_flag = 1

    # 모기가 나갔고 아직 end 범위를 못 정했으면 해당 범위로 체크
    elif end_edit_flag and IO[time] < 0:
        max_range[1] = time
        end_edit_flag = 0

print(max_count)
print(*max_range)
