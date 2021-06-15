import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, str(input())))

    # 0~9 까지의 인덱스에 해당 숫자 나온 횟수
    count = [0] * 10
    for num in num_list:
        count[num] += 1

    # count의 최대값 구하기
    max_count = max(count)

    # 동일 횟수 나왔으면 큰 값이 출력되므로 뒤집어주고 인덱스 찾기.
    count.reverse()
    max_num = 9 - count.index(max_count)

    print('#{} {} {}'.format(tc, max_num, max_count))