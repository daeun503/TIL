import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

T = int(input())
for tc in range(1, T + 1):
    text = input()
    stack = []

    for t in text:
        # 여는 괄호면 스택에 쌓아준다.
        if t == '(' or t == '{':
            stack.append(t)
        # 닫는 괄호인데 스택에 여는 괄호가 있으면
        elif (t == ')' or t == '}') and stack:
            # 닫는 괄호가 )이고 스택 맨 위가 (이면 pop (짝 맞음)
            if t == ')' and stack[-1] == '(':
                stack.pop()
            # 닫는 괄호가 } 이고 스택 맨 위가 {이면 pop (짝 맞음)
            elif t == '}' and stack[-1] == '{':
                stack.pop()
            # 닫는 괄호고 스택에 무언가 있는데 짝이 안맞으면 break
            else:
                break
        # 닫는 괄호인데 스택에 아무것도 없으면 스택에 하나 넣어주고 break
        elif t == ')' or t == '}':
            stack.append(t)
            break

    # 스택에 무언가 있으면 0, 스택에 아무것도 없으면 1 출력
    print("#{} {}".format(tc, 0)) if stack else print("#{} {}".format(tc, 1))