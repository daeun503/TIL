# 문자열 s의 길이가 4나 6이면 True 아니면 False
# try except로 s를 int로 바꿀 수 있으면 True 아니면 False

def solution(s):
    # 문자열 s의 길이가 4나 6이면 True
    result = True if len(s) == 4 or len(s) == 6 else False
    # 문자열 s가 숫자로만 구성되어 int로 바꿀 수 있으면 True 아니면 False
    try:
        int(s)
        return result
    except:
        return False