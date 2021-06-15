IN = list(input())

stack = []
Postfix = ''
for i in IN:
    if i.isalpha():
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

print(Postfix)