import sys
sys.stdin = open("input.txt")


# def my_func(n):
#     global cnt
#     if cnt > N: return
#     # 왼쪽 자식 노드가 비었으면 왼쪽을 기준으로
#     if tree[2*n] == 0: my_func(2*n)
#     # 왼쪽 처리 다 했으면 자신에 값 써넣기
#     tree[n] = cnt
#     cnt += 1
#     # 오른쪽 자식 노드가 비었으면 오른쪽을 기준으로
#     if tree[2*n+1] == 0: my_func(2*n+1)
#
#
# for tc in range(1, int(input())+1):
#     N = int(input())
#     tree = [0] * (N+1) + ['-'] * 1000  # 제한이 별로 안 크니까..
#     cnt = 1
#     my_func(1)
#     print('#{} {} {}'.format(tc, tree[1], tree[N//2]))


# 두호님 걸 보고 고쳤다..
def my_func(n):
    global cnt
    if n <= N:
        my_func(2*n)
        tree[n] = cnt; cnt += 1
        my_func(2*n+1)

for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 1
    my_func(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))