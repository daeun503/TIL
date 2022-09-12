def func(member, idx):
    # K 명의 멤버를 모두 뽑았으면 종료
    if len(member) >= K:
        check = set(range(1, N+1))
        for m in member:
            check &= G[m]
        if len(check) >= K:
            for m in member:
                print(m)
            exit()
        return

    # K 명의 멤버를 뽑지 못했으면 더 뽑기
    for i in range(idx, len(check_member)):
        next_member = check_member[i]
        if next_member not in member:
            func(member + [next_member], i)


# N 명의 학생, K 명 뽑기
K, N, F = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(F)]

# 친구 관계 표시
G = [{me} for me in range(N + 1)]
for a, b in IN:
    G[a].add(b)
    G[b].add(a)

# 친구가 K 명 이상 (본인 포함) 인 사람만 체크
check_member = []
for i in range(1, N + 1):
    if len(G[i]) >= K:
        check_member.append(i)

func([], 0)
print(-1)