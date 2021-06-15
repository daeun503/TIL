import sys
sys.stdin = open('input.txt')

"""
괄호 매칭
1. 괄호의 종류 - [], {}, ()
2. 괄호 매칭의 조건 
- 왼쪽 괄호의 개수와 오른쪽 괄호의 '개수'가 같아야 한다.
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 '먼저' 나와야 한다.
 - 괄호 사이에는 포함 관계만 존재한다.
3. 잘못된 사용의 예시
(a(b) -> 괄호 개수
a(b)c) -> 괄호 개수
a{b(c[d]e}) -> 괄호가 올바르게 매칭되지 않음
"""

# 소괄호만
stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in data:
        if i == ')':
            if is_empty():
                return '괄호 개수가 다르다.'
            pop()
        else:
            push(i)
    if is_empty():
        return '괄호가 올바르다.'
    else:
        return '괄호 개수가 다르다.'


# 첫 번째 괄호쌍
data = input()

# 두 번째 괄호쌍
data2 = input()

print(check_matching(data))
print(check_matching(data2))
