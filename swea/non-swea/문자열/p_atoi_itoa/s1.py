# atoi (ASCII to Integer)
# 문자 -> 숫자 / Python의 int()

def atoi(my_str):
    """
    인자로 받은 정수 my_num을 문자로 반환 ord(), chr()사용
    """
    result = 0
    for i in range(len(my_str)):
        result *= 10
        result += ord(my_str[i]) - ord('0')
    return result

my_str = '123'
print(my_str, type(my_str))

my_int1 = atoi(my_str)
print(my_int1, type(my_int1))

my_int2 = int(my_str)
print(my_int2, type(my_int2))