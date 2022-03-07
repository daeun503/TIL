# 실패 => 시간초과
import sys
sys.stdin = open("input.txt", "r")
from pandas import DataFrame

input = sys.stdin.readline

def make_tree():
    pointer = 1
    for num in IN:
        # 넣으려는 값이 포인터 값보다 작으면 왼쪽 자식
        while tree[pointer] and num < tree[pointer]:
            pointer = 2 * pointer

        # 넣으려는 값이 포인터 보다 크면 오른쪽 자식
        while tree[pointer] and num > tree[pointer]:
            # 내 부모보다 크면 포인터를 부모로 바꿔서 다시
            if tree[pointer // 2] < num:
                pointer = pointer // 2
            # 내 부모보다 작으면 내 형제
            else:
                pointer = 2 * pointer + 1
        tree[pointer] = num


def print_tree(p):
    if tree[2 * p]:
        print_tree(2 * p)
    if tree[2 * p + 1]:
        print_tree(2 * p + 1)
    if tree[p]:
        print(tree[p])


IN = []
while 1:
    try:
        IN.append(int(input()))
    except:
        break
N = len(IN)
tree = [0] * 10001
tree[0] = 10 ** 7

make_tree()
print_tree(1)
