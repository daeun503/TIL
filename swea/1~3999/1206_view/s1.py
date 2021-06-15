import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    # 양 옆 (0)은 제외 
    for i in range(2, N-2):
        # 내 주위의 건물들 중 가장 높은 건물의 높이(around_max)
        # around_max = max([arr[i-2], arr[i-1], arr[i+1], arr[i+2]])
        around_max = 0
        for height in [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]:
            if height > around_max:
                around_max = height

        # 만약 내가(arr[i]) 가장 높은 주위 건물보다도 더 높다면 그 높이 차이만큼 조망권+
        if around_max < arr[i]:
            result += arr[i] - around_max

    print('#{} {}'.format(tc, result))
