"""
연습 문제 4.

0과 1로 이루어진 1차원 배열에서 Byte 단위로 묶어 10진수로 출력하기
- arr는 편의상 분리한 것이기 때문에 연속된 수로 간주할 것

입력 예시)
0 0 0 0 0 0 1 0 0 0 1 1 0 1

0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 1 1 0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 1 1 0 0 1 1 1 1 0 0 1 1 1 1 1 1 0 0 1 1 0 0 1 1 1

출력 예시)
1 13

0 120 12 7 76 24 60 121 124 103
"""

arr = [
       0,0,0,0,0,0,0, 1,1,1,1,0,0,0, 0,0,0,1,1,0,0, 0,0,0,0,1,1,1, 1,0,0,1,1,0,0,
       0,0,1,1,0,0,0, 0,1,1,1,1,0,0, 1,1,1,1,0,0,1, 1,1,1,1,1,0,0, 1,1,0,0,1,1,1
      ]

# 위 arr 대로 할거면 이 부분 주석처리. 입력받을거면 살려두기
arr = list(map(int, input().split()))

# 7자리씩 끊어서 10진수로 변환해준다.
b = ''
for i in arr:
    b += '1' if i else '0'
    # b의 길이가 7이 됐으면 출력하고 b를 초기화
    if len(b) % 7 == 0:
        print(int('0b'+b, 2), end=' ')
        b = ''