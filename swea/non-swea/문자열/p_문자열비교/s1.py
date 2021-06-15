
def str_comparision(str1, str2):
    """
    문자열이 같은지 비교해서
    같으면 True 반환
    같지 않으면 False 반환
    """
    # 길이 같은데 문자열 비교중에 다르면 False
    if len(str1) == len(str2):
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
    # 길이 다르면 False
    else:
        return False
    # if문 다 마치면 True
    return True

str1 = 'abccd'
str2 = 'abcd'

print(str_comparision(str1, str2))