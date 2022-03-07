import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)


def postorder(start, end):
    if start >= end:
        return

    # 루트는 전위 순회의 첫 번째 값
    root = preorder[start]

    # 만약에 끝 값이 root보다 작다면 오른쪽 서브 트리가 없다
    if preorder[end - 1] <= root:
        postorder(start + 1, end)
        print(root)
        return

    # root 보다 큰 값이 나오면 그 때부터 오른쪽 자식 => 해당 값이 idx
    for i in range(start + 1, end):
        if preorder[i] > root:
            idx = i
            break

    # start는 root
    # start + 1 ~ idx (오른쪽 자식) 까지 왼쪽 서브트리
    postorder(start + 1, idx)
    # idx ~ end 까지 오른쪽 서브트리
    postorder(idx, end)
    # root 출력
    print(root)


preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break

postorder(0, len(preorder))
