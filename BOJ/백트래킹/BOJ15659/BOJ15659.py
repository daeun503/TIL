N = int(input())
nums = input().split()
ops = list(map(int, input().split()))

max_value, min_value = -float('inf'), float('inf')

def func(depth, expression, plus, minus, multiply, divide):
    global max_value, min_value

    if depth == N:
        value = eval(expression)
        max_value = max(value, max_value)
        min_value = min(value, min_value)
        return

    if plus:
        func(depth + 1, expression + "+" + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        func(depth + 1, expression + "-" + nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        func(depth + 1, expression + "*" + nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        func(depth + 1, expression + "//" + nums[depth], plus, minus, multiply, divide - 1)


func(1, nums[0], *ops)
print(max_value)
print(min_value)
