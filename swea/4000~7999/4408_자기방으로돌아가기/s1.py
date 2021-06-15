import sys
sys.stdin = open("input.txt", 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    IN = [list(map(int, input().split())) for _ in range(N)]
    # 큰 방에서 작은 방으로 갈 때. 인덱스 바꿔줌 => 작은 방에서 큰 방으로 갈 때로.
    for i in range(len(IN)):
        if IN[i][0] > IN[i][1]:
            IN[i][0], IN[i][1] = IN[i][1], IN[i][0]

    # 인덱스 0 기준으로 정렬하기 IN.sort()
    IN.sort(key=lambda x: x[0])

    stack = [[IN[0][1]]]            # IN[0] = (10, 20)
    for i in range(1, len(IN)):
        for j in range(len(stack)):
            # 이동한 방이 홀수번째 방이면 +1 해서 짝수까지 커버
            if stack[j][-1] % 2:
                # 어떤 경로에서, 큰 방으로 이동한 값보다 / 현재 경로에서 출발하는 작은 방이 크면 추가 가능
                if stack[j][-1] + 1 < IN[i][0]:
                    stack[j].append(IN[i][1])
                    break
            # 이동한 방이 짝수번째 방
            else:
                # 어떤 경로에서, 큰 방으로 이동한 값보다 / 현재 경로에서 출발하는 작은 방이 크면 추가 가능
                if stack[j][-1] < IN[i][0]:
                    stack[j].append(IN[i][1])
                    break
        # for문이 다 돌때까지 제 위치를 찾아가지 못하면 stack에 새 경로로 추가해줌
        else:
            stack.append([IN[i][1]])

    print("#{} {}".format(tc, len(stack)))