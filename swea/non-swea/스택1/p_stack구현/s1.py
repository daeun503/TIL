# 크기를 정하지 않은 가변 리스트

stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

push(1)
push(2)
push(3)
print(stack)

print('------')

# 가장 뒤(위)부터 pop
print(pop())
print(pop())
print(pop())
