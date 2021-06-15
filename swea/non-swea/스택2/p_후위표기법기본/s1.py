"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여
수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

예시 입력)
2+3*4/5

예시 출력)
2345/*+
"""

import sys
sys.stdin = open('input.txt')

IN = input()
number = "0123456789"
stack = []
result = ''

for t in IN:
    if t in number:
        result += t
    else:
        stack.append(t)
while stack:
    result += stack.pop()

print(result)


# for t in IN:
#     if t in number:
#         result += t
#
#     # 들어오는 글자가 + 혹은 - 이면
#     elif t in "+-":
#         # 스택 맨 위 글자가 * 혹은 /이면
#         if stack[-1:] == ['*'] or stack[-1:] == ['/'] :
#             result += stack.pop()
#             stack.append(t)
#         # 스택 맨 위 글자가 + 혹은 - 이거나, 비어있으면
#         else:
#             stack.append(t)
#     # 들어오는 글자가 * 혹은 / 이면
#     else:
#         # 스택 맨 위 글자가 * 혹은 / 이면
#         if stack[-1:] == ['*'] or stack[-1:] == ['/'] :
#             result += stack.pop()
#             stack.append(t)
#         # 스택 맨 위 글자가 + 혹은 - 이거나, 비어있으면
#         else:
#             stack.append(t)
#
# while stack:
#     result += stack.pop()

