import sys
input = sys.stdin.readline
# sys.stdin = open("input.txt", "r")


def find(x):
    if p[x] == x:
        return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):
    X = find(x)
    Y = find(y)
    if X > Y:
        p[X] = Y
    elif X < Y:
        p[Y] = X


N, M = map(int, input().split())
p = list(range(N+1))

# 진실을 아는 사람의 리스트
IN = list(map(int, input().split()))
count, known_list = IN[0], sorted(IN[1:])
# 진실을 아는 사람이 없으면 파티수 만큼 거짓말
if not count:
    print(M)
    exit()
# 진실을 아는 사람들을 union
for idx in range(count - 1):
    a, b = known_list[idx], known_list[idx + 1]
    union(a, b)

# 로직
party = []
for _ in range(M):
    # 파티에 참여한 사람 리스트
    IN = list(map(int, input().split()))
    count, party_people = IN[0], IN[1:]
    for idx in range(count - 1):
        a, b = party_people[idx], party_people[idx + 1]
        union(a, b)
    party.append(set(party_people))

# 진실을 아는 사람들(known_list와 부모가 같은)을 모두 구함
KNOWN = find(known_list[0])
known_set = {
    idx
    for idx in range(1, N+1)
    if find(idx) == KNOWN
}

# 파티 참여 인원을 보면서 과장할 수 있는 파티 수를 셈
count = 0
for people in party:
    if not (people & known_set):
        count += 1
print(count)


"""
46% 쯤에서 틀렸었는데 이걸로 풀음
5 3
1 3
3 1 2 4
3 1 4 5
1 3 
답: 2
"""
