import sys
sys.stdin = open("input.txt")

def my_func(n, IN, IN_idx):
    SetIN = set(IN)
    SetIN_len = len(SetIN)

    # 1종류 일 때 이긴 쪽 값과 인덱스 리턴
    if SetIN_len == 1: return IN_idx[0]

    # 2종류 일 때 이긴 쪽 값과 인덱스 리턴
    elif SetIN_len == 2:
        # 가위(1), 보(3) 이면 가위가 이기니까, IN_idx 확인하면서 i가 1일때를 리턴
        if SetIN == {1, 3}:
            for i, j in IN_idx:
                if i == 1: return (i, j)
        # 가위(1), 바위(2) 이면 바위가 이기니까, IN_idx 확인하면서 i가 2일때 리턴
        elif SetIN == {1, 2}:
            for i, j in IN_idx:
                if i == 2: return (i, j)
        # 바위(2), 보(3) 이면 보가 이기니까, IN_idx 확인하면서 i가 3일때 리턴
        elif SetIN == {2, 3}:
            for i, j in IN_idx:
                if i == 3: return (i, j)

    # 3종류 일 때는 카드 양 쪽으로 나눠주기. 결과값 A_idx(값+인덱스), a(값), a_idx(인덱스) 로 나눔
    else:
        A_idx = my_func(len(IN[:(len(IN)-1)//2+1]), IN[:(len(IN)-1)//2+1], IN_idx[:(len(IN)-1)//2+1])
        B_idx = my_func(len(IN[(len(IN)-1)//2+1:]), IN[(len(IN)-1)//2+1:], IN_idx[(len(IN)-1)//2+1:])
        return my_func(2, [A_idx[0], B_idx[0]], [A_idx, B_idx])

for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    # 값과 인덱스 쌍을 만들기
    IN_idx = [(i, idx) for idx, i in enumerate(IN, start=1)]
    result = my_func(N, IN, IN_idx)
    print("#{} {}".format(tc, result[1]))