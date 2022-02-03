import sys
sys.stdin = open("input.txt", "r")

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a); B.append(b)
    C.append(c); D.append(d)

# A+B의 값을 미리 dict에 세어두기
AB_dict = {}
for a in A:
    for b in B:
        AB_dict[a+b] = AB_dict.get(a+b, 0) + 1

# C+D의 값을 확인하면서, 대응하는 값이 A+B dict에 있는지 확인
count = 0
for c in C:
    for d in D:
        count += AB_dict.get(-(c+d), 0)

print(count)
