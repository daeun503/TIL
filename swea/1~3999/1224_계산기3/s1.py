import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

for tc in range(1, 11):
    N = int(input())
    IN = list(input())

    # 중위 -> 후위
    stack = []
    Postfix = ''
    for i in IN:
        if i.isdigit():
            Postfix += i
        else:
            # 여는 괄호면 무조건 스택에 넣기
            if i == '(':
                stack += [i]
            # 닫는 괄호면 무조건 여는 괄호 만날때까지 pop.
            elif i == ')':
                while stack[-1] != '(':
                    Postfix += stack.pop()
                stack.pop() # 스택 내의 여는 괄호 필요 없으니까 제거
            # +, - 일 때 : stack이 비거나 ( 만날 때 까지 pop 하고 push
            elif i == '+' or i == '-':
                while stack and stack[-1] != '(':
                    Postfix += stack.pop()
                stack.append(i)
            # *, / 일 때 : stack에 *, / 있으면 pop하고 push
            else:
                while stack[-1:] == ['*'] or stack[-1:] == ['/']:
                    Postfix += stack.pop()
                stack.append(i)
    # 스택에 남아 있는 것들 모두 꺼내서 더해주기
    while stack:
        Postfix += stack.pop()

    # 후위 -> 계산
    stack = []
    for i in Postfix:
        # 만약 숫자면 stack에 쌓기
        if i.isdigit():
            stack.append(i)
        # 연산자면 피연산자 2개 뽑아서 계산
        else:
            B = int(stack.pop())
            A = int(stack.pop())
            cal = {'+': A + B, '-': A - B, '*': A * B, '/': A // B}
            stack.append(cal[i])

    print("#{} {}".format(tc, stack.pop()))