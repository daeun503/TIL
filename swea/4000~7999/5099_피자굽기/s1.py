import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    IN = list(map(int, input().split()))
    # 값이랑 인덱스 묶어주기. 큐에는 화덕에 있는 피자, IN에는 바깥에 있는 피자
    queue = [(value, idx) for idx, value in enumerate(IN[:N], start= 1)]
    IN = [(value, idx) for idx, value in enumerate(IN[N:], start= N+1)]

    while len(queue) != 1:           # 큐에 피자 하나 남을때까지 while문 반복
        value, idx = queue.pop(0)    # value값이 1이든 0이든 일단 버리기
        value //= 2
        if value:                    # value 값이 1이상이면 뒤에 붙여줌
            queue += [(value, idx)]
        elif IN:                     # 0이면 안붙이고(버리고) IN에 값 있으면 IN에서 새로 뽑아오기
            queue += [IN.pop(0)]

    print("#{} {}".format(tc, queue[0][1]))