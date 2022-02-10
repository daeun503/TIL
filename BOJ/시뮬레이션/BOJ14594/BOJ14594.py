import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

N = int(input())
M = int(input())

rooms = list(range(N+1))

for _ in range(M):
    x, y = map(int, input().split())

    # 첫 번째 방, 마지막 방 값 체크
    first_room = rooms[x]
    final_room = rooms[y]

    # x ~ y 방을 첫 번째 방 번호로 갱신
    for i in range(x, y+1):
        rooms[i] = first_room

    # y+1 방 부터 앞에 방이랑 이어져있는지 확인하고 번호 갱신
    for j in range(y+1, N+1):
        # y+1 번 방이 y번 방 (final_room)과 이어져 있었으면 갱신
        if rooms[j] == final_room:
            rooms[j] = first_room
        # 아니면 볼 필요 없으니까 break
        else:
            break

print(len(set(rooms)) - 1)

