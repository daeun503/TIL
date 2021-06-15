# 크기를 정해놓은 배열

SIZE = 5
top = -1
stack = [0] * SIZE

def push(item):
    global top, stack
    if top == SIZE-1:
        return
    top += 1
    stack[top] = item

def pop():
    global top, stack
    if top == -1:
        return
    else:
        top -= 1
        return stack.pop()

push(1)
push(2)
push(3)
push(4)
push(5)
print(top, stack)

print('------------------------')

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
print(top, stack)
