import sys
sys.stdin = open('input.txt')

N = int(input())
IN = list(map(int, input().split()))

# 카운팅
ANS = [0] * 41
for i in IN:
    ANS[i] += 1

# 경우의 수 구하기
animal_min = ANS.count(2)
animal_max = animal_min + ANS.count(1)
result = 2**animal_min*2 if animal_min != animal_max else 2**animal_min

# 예외 처리 ~min는 모두 2, min~max는 1, max~는 0 이어야함
for i in ANS[:animal_min]:
    if i != 2: result = 0
for j in ANS[animal_min:animal_max]:
    if j != 1 : result = 0
for z in ANS[animal_max:]:
    if z != 0 : result = 0
if animal_min + animal_max != N:
    result = 0

print(result)

