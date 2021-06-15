# itoa (Integer to ASCII)
# 숫자 -> 문자 / Python의 str()

def itoa(my_num):
    """
    인자로 받은 정수 my_num을 문자로 반환
    """
    result = ""
    while my_num:
        tmp = my_num % 10
        result = chr(tmp + 48) + result
        my_num = my_num // 10
    return result


my_num = 123
print(my_num, type(my_num))

my_str1 = itoa(my_num)
print(my_str1, type(my_str1))

my_str2 = str(my_num)
print(my_str2, type(my_str2))