import sys
sys.stdin = open("input.txt")
from pandas import DataFrame

def win(A):
    A.sort()
    if A[0][0] == 1 and A[1][0] == 2:
        return A[1]
    elif A[0][0] == 2 and A[1][0] == 3:
        return A[1]
    elif A[0][0] == 1 and A[1][0] == 3:
        return A[0]
    # 숫자 동일할 때
    else:
        return A[0]

# 리턴할 때 튜플인지 리스트인지 잘 확인해야한다
def my_func(IN):
    # 2이하 일 때
    if len(IN) == 1:
        return (IN[0][0], IN[0][1])
    elif len(IN) == 2:
        return win(IN)
    else:
        # 3이상 일 때
        mid = (1+len(IN)) // 2
        A = my_func(IN[:mid])
        B = my_func(IN[mid:])
        return win([A, B])

for tc in range(1, int(input())+1):
    N = int(input())
    IN = list(map(int, input().split()))
    for i in range(len(IN)):
        IN[i] = (IN[i], i+1)
    print("#{} {}".format(tc, my_func(IN)[1]))

'''
토너먼트 카드게임
- 이전에는 set을 통해 가위바위보 남은 종류의 수를 판단해서 풀었었다.
- 이번에는 list를 통해 리스트 길이로 (종류 말고) 판단해서 풀었다.
- 둘 다 튜플로 인덱스 번호 써준 것은 똑같다

- 1111 같은 경우에 set으로 푸는 게 재귀 안 돌아서 더 좋지 않을까.. 싶긴 하다. 
  이번에도 풀면서 set할까 싶었는데 그럼 복잡해질까봐 그냥 list로만 풀었다.  
- 저번에는 시간이 많이 들었었다. 이번에는 저번보단 덜 들었었고. 빨리 풀어야 해!! 해서.
- 코드 변수 명이 좀 간결해진듯?? 전에는 SetIN_len, A_idx... 이렇게 썼었는데 지금은 A..B.....
  변수 명을 대충 작성하지만 보기에는 더 나아진 것 같다. 전에 작성한 건 길어서 지저분해 보인다;;
  전에 쓴 게 지저분해 보여서 읽기 싫은데 막상 읽으면 변수 명 때문에 좀 편한 것 같기도 하고 
  오늘 작성한게 짧아서 읽기 괜찮아 보이지만 막상 읽기 어려울 수 있으니까 트레이드 오프가 확실한 듯...

- 이번에 풀면서 재귀 리턴 타입이 섞여서 에러가 발생했었다. 그래서 삽질을 좀 했음(line21)
- 지금까지 별 생각 없었는데 타입 힌팅 쓰는 버릇을 들여야겠다.
'''