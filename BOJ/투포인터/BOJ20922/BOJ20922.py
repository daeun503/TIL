import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
IN = list(map(int, input().split()))

s, e = 0, 0
result, length = 0, 0
number_count = [0] * 100001

while e < N:
    e_tmp = IN[e]

    # 만약 end 포인터를 더했을 때 K개 이하이면
    # end 포인터를 이동시키고 길이를 늘린다.
    if number_count[e_tmp] + 1 <= K:
        number_count[e_tmp] += 1
        length += 1
        e += 1
        if length > result:
            result = length
        continue

    # K개 초과하면 start 포인터를 이동하면서
    # 앞에 수열을 제외시켜서 K개 이하로 만든다.
    while number_count[e_tmp] + 1 > K:
        s_tmp = IN[s]
        number_count[s_tmp] -= 1
        length -= 1
        s += 1

print(result)
