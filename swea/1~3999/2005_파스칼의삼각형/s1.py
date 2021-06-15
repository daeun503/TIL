import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    print("#{}".format(tc))

    # 맨 처음 1 출력, old_result에 저장
    print(1)
    old_result = [1]

    for i in range(N-1):     # 그 밑에 N-1행 출력할 예정
        result = [1]         # 각 행의 맨 처음 1 추가
        # old_result 값의 j + (j+1) 을 더해서 현재 값에 추가해준다.
        for j in range(i):
            result.append(old_result[j]+old_result[j+1])
        result += [1]        # 각 행의 마지막 1 추가
        old_result = result  # old_result에 현재 result 저장
        print(*result)