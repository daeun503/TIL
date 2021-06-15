import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    input()                                # #기호, 테스트 케이스의 번호 안씀
    input_planet = list(input().split())   # input은 split 해서 list에 넣음

    planet_num = {"ZRO": 0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    planet_num_list = ["ZRO ", "ONE ", "TWO ", "THR ", "FOR ", "FIV ", "SIX ", "SVN ", "EGT ", "NIN "]
    result = [0] * 10

    # input에서 for문 돌아서, i는 ZRO 같은 값. planet_num[i] 하면 0~9까지 숫자가 나온다.
    # 따라서 ZRO, ONE, TWO ... 나온 횟수를 result에 저장하는 것 input_planet.count() 랑 동일
    for i in input_planet:
        result[planet_num[i]] += 1

    # 출력. planet_num_list[i]은 ZRO, ONE.. 같은 str, result[i]는 해당 str 나온 횟수
    print("#{}".format(tc))
    for i in range(10):
        print(planet_num_list[i] * result[i], end = '')
    print()