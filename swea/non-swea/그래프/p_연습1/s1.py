"""
연습 문제1. Stack 구현
 - 사이즈가 5인 고정 배열 Stack을 구현하시오.
"""

SIZE = 5
stack = [0]*SIZE
top = -1

def push(num):
    global top

    if top+1 < SIZE:
        top += 1
        stack[top] = num
    else:
        print('stack pull')

def pop():
    global top

    if top > -1:
        top -= 1
        return stack[top+1]
    else:
        print('stack empty')
        return None

push(1)
push(2)
push(3)
push(4)
push(5)
push(6)

item = pop() # 5
print('Pop item {}'.format(item))
item = pop() # 4
print('Pop item {}'.format(item))
item = pop() # 3
print('Pop item {}'.format(item))
item = pop() # 2
print('Pop item {}'.format(item))
item = pop() # 1
print('Pop item {}'.format(item))

item = pop() # None
print('Pop item {}'.format(item))