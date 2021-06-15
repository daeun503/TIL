"""
연습 문제3. 2의 거듭제곱

2의 거듭 제곱을 반복과 재귀버전으로 구현하시오.
"""

my_list = [5, 2, 7, 1, 3, 8, 9, 3, 5, 2]

# 반복
def power_of_two_iteration(k):
    result = 1
    for i in range(k):
        result *= 2
    return result

print(power_of_two_iteration(2))
print(power_of_two_iteration(3))
print(power_of_two_iteration(4))


# 재귀
def power_of_two_recursion(k):
    if k == 0:
        return 1
    else:
        return 2 * power_of_two_recursion(k-1)

print(power_of_two_recursion(2))
print(power_of_two_recursion(3))
print(power_of_two_recursion(4))