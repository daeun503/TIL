"""
연습 문제 3.

5 ~ -5를 2진수로 표현

출력 예시)
-5  11111011
-4  11111100
-3  11111101
-2  11111110
-1  11111111
0   00000000
1   00000001
2   00000010
3   00000011
4   00000100
5   00000101

참고 1) i의 j번 비트가 1인지 여부를 검사

0
| b7 | b6 | b5 | b4 | b3 | b2 | b1 | b0 |
  0    0    0    0    0    0    0    0 -> i

  1    0    0    0    0    0    0    0 -> j번째 비트(7번째)
  0    1    0    0    0    0    0    0 -> j번째 비트(6번째)
  ....
  0    0    0    0    0    0    1    0 -> j번째 비트(1번째)
  0    0    0    0    0    0    0    1 -> j번째 비트(0번째)
  -------------------------------------
  0    0    0    0    0    0    0    0

1
| b7 | b6 | b5 | b4 | b3 | b2 | b1 | b0 |
  0    0    0    0    0    0    0    1 -> i

  1    0    0    0    0    0    0    0 -> j번째 비트(7번째)
  0    1    0    0    0    0    0    0 -> j번째 비트(6번째)
  ....
  0    0    0    0    0    0    1    0 -> j번째 비트(1번째)
  0    0    0    0    0    0    0    1 -> j번째 비트(0번째)
  -------------------------------------
  0    0    0    0    0    0    0    1
"""

def Bbit_print(i):
    output = ''
    # -5~5까지는 8bit로 표현되니까, 0 ~ 7 번째 비트를 확인
    # 왼쪽부터 비교해서 ouput에 밀어넣을 거니까, range(7, -1, -1)
    for j in range(7, -1, -1):
        output += '1' if i & (1 << j) else '0'
    print(output)

for i in range(-5, 6):
    print ('{}  '.format(i), end='')
    Bbit_print(i)