import sys, itertools

# n, m 입력
n, m = map(int, sys.stdin.readline().split())

# words : 각 단어의 비트마스킹한 정수를 저장
words = [0] * n
ans = 0
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    # word 배열에 각 문자의 비트마스킹 저장
    for x in temp:
        words[i] |= (1 << (ord(x) - ord('a')))

# 만일 m이 5미만이면 필수 글자를 다 배울 수 없기 때문에 한 단어도 읽지 못한다
if m < 5:
    print(0)
else:
    # candidiate : 필수 글자를 제외한 알파벳
    # need : 필수 알파벳
    candidiate = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
    need = ['a', 'c', 't', 'i', 'n']
    for i in list(itertools.combinations(candidiate, m - 5)):
        each = 0
        res = 0
        # 각 조합에 대한 비트마스킹
        for j in need:
            each |= (1 << (ord(j) - ord('a')))
        for j in i:
            each |= (1 << (ord(j) - ord('a')))

        # 단어와 각 조합의 비교
        for j in words:
            if each & j == j:
                res += 1

        # 최대값 갱신
        if ans < res:
            ans = res
    print(ans)
