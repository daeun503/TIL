import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame
from collections import defaultdict


# 폴더 만들기
N, M = map(int, input().split())
my_folder = defaultdict(set)
for i in range(N + M):
    P, F, C = input().split()
    my_folder[P].add((F, int(C)))


# 폴더 옮기기 
K = int(input())
for _ in range(K):
    from_dir_str, to_dir_str = input().split()
    from_dir = from_dir_str.split("/")
    to_dir = to_dir_str.split("/")

    # from 폴더에서 to 폴더로 파일 이동
    for f in my_folder[from_dir[-1]]:
        my_folder[to_dir[-1]].add(f)

    # from 폴더 자체 삭제
    del my_folder[from_dir[-1]]

    # from 폴더의 부모에서 from "폴더" 삭제
    if len(from_dir) > 1:
        my_folder[from_dir[-2]].remove((from_dir[-1], 1))


# 쿼리 순서대로 답 내기
Q = int(input())
for _ in range(Q):
    q_dir = input().split("/")

    q = [q_dir[-1]]
    file_list = set()
    file_count = 0
    # q는 탐색할 폴더 => 다 탐색할때까지 반복
    while q:
        current = q.pop(0)
        for f, c in my_folder[current]:
            # 폴더면 q에 넣기
            if c:
                q.append(f)
                continue
            # 파일이면 개수 세기
            file_list.add(f)
            file_count += 1
    print(len(file_list), file_count)
