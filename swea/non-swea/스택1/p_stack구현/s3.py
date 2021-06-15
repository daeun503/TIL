# class로 stack 구현하기

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return
        else:
            return self.stack.pop()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack)
print(s.pop())
print(s.stack)
print(s.is_empty())