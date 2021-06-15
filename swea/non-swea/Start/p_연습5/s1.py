"""
연습 문제 5.

16진수 문자로 이루어진 1차원 배열이 주어질 때 앞에서부터 7bit씩 묶어 십진수로 변환하여 출력하기

입력 예시)
0F97A3

출력 예시)
7 101 116 3

참고 사항) 16진수 & 2진수
1. 0xff -> 256
    15      15
 1 1 1 1  1 1 1 1

2. 0xfa -> 250
    15      10
 1 1 1 1  1 0 1 0

3. 0xfe -> 254
   15       14
 1 1 1 1  1 1 1 0
"""

#1. 16진수 -> 2진수
asc = {
    '0': 0, '1': 1, '2': 2, '3': 3,
    '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11,
    'C': 12, 'D': 13, 'E': 14, 'F': 15,
}


def ascii_to_hex(c):
    return asc[c]

def hex_to_binary(x):
    output = ''
    while x:
        output += str(x % 2)
        x = x // 2
    output = '0'*(4-len(output)) + output  # 자릿수 맞춰주기
    return output


t = []
arr = '0F97A3'

for i in range(len(arr)):
    htb = hex_to_binary(ascii_to_hex(arr[i]))
    t.extend(map(int, htb))

#2. 7bit씩 묶어서 2진수 -> 10진수 변환
"""
print(t)
[0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]

앞에서부터 7 bit씩 끊고 10진수 변환

1. 0, 0, 0, 0, 1, 1, 1 -> 7
2. 1, 1, 0, 0, 1, 0, 1 -> 101
3. 1, 1, 1, 0, 1, 0, 0 -> 116
4. 0, 1, 1 -> 3
"""
n = 6
result = 0
for i in range(len(t)):
    result += t[i] * (2**n)
    # n이 0이 되면(=7bit) 초기화
    if n == 0:
        print(result, end=' ')
        n = 6
        result = 0
    else:
        n -= 1