# case1. 테케 2~6, 13, 15~17 실패: 서로수? 일 때 동작 X 테케 5, 7, 24로 확인해보세요. 저도 첨에 이 로직으로 했었는데 로직 자체에 문제가 있는 것 같네요. 이 로직은 버리는 게 좋을 것 같지만 성공하는 분이 있다면 궁금합니다
# case2. 테케 4, 6, 17 실패 : 실수형의 오차 때문. k = h/w같이 기울기를 구하고 있다면, y = h * x / w 처럼 연산의 순서를 바꿔보세요.
# case3. 시간 초과 : w == h일 때, w, h가 1일 때를 따로 계산해보세요.

# ver1 : for문으로 풀기 (gcd로 푸는게 좋음. 장점은 math를 안 쓰는거?)
# 각 x 좌표마다 y좌표를 구해서, 사용할 수 없는 직사각형의 수를 구한다.
def solution(w,h):
    if w == h: return w*h - w
    if w > h: w, h = h, w
        
    old_y = 0
    no = 0
    
    for x in range(w+1):
        y = h * x / w
        no += int(y) - old_y
        if y % 1: no += 1
        old_y = int(y)
        
    return w*h - no

# ver2 : gcd로 풀기
# import math
# def solution(w,h):
#     return w*h - (w+h-math.gcd(w,h))

# case1 : 서로수?일 때 동작 x // 2~6, 13, 15~17 테케 실패 // 5, 7, 24 넣어서 확인
# import math
# def solution(w,h):    
#     if w > h:
#         w, h = h, w
#     number = math.ceil(h/w)
#     return w*h - number*w

# case 2 : 소수 제대로 동작 x // 테케 4, 6, 17 실패
# import math
# def solution(w,h):
#     if w == h: return w*h - w
#     if w > h: w, h = h, w
#     k = h/w  # floot형 오차 존재
#     old_y, result = 0, 0
#     for x in range(w+1):
#         y = k * x
#         result += math.floor(y) - old_y
#         if y % 1:
#             result += 1
#         old_y = math.floor(y)
#     return w*h - result