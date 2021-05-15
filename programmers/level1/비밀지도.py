# arr1, arr2 zip으로 묶어서 binary or 연산
# 결과가 0b 형식이라 [2:]로 뒷 값만 슬라이싱
# 2진 표현을 #와 ' '으로 표현해주기

# 2회차 풀이
def solution(n, arr1, arr2):
    # arr1, arr2 zip으로 묶어서 binary or 연산
    arr = [ bin(int(bin(a),2) | int(bin(b),2))[2:] for a, b in zip(arr1, arr2)]
    # 2진 표현을 #와 ' '으로 표현해주기
    for i in range(n):
        arr[i] = arr[i].replace('1', '#')
        arr[i] = arr[i].replace('0', ' ')
        # 앞에 0있어서 자릿수 부족하면 채워주기
        if len(arr[i]) != n:
            arr[i] = ' ' * (n-len(arr[i])) + arr[i]
    return arr