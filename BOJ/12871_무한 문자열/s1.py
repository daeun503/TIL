import sys
sys.stdin = open('input.txt')

s = input()
t = input()

# 문자열 길이 제한이 작아서 그냥 곱해도 될듯
n, m = len(s), len(t)
s, t = s * m, t * n
print(1) if s == t else print(0)