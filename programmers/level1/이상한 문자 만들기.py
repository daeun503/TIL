# tilte()로 공백 다음을 대문자로 바꿔주고, 뮤터블하게 리스트로 바꿔주기
# 대문자 인덱스로부터 2n만큼 떨어져있으면 해당 문자도 대문자로 바꿔주기

def solution(s):
    s_list = list(s.title())        # 공백 다음을 대문자로. 뮤터블하게 리스트로
    tmp = -1                        # 홀/짝 판별 임시 변수
    for i in range(len(s_list)):    
        if s_list[i].isupper():     # 만약 문자가 대문자면 (공백 다음)
            tmp = i                 # 임시 변수에 해당 idx 저장
        elif not (i-tmp) % 2:         # 임시 변수(대문자)로부터 2n으로 떨어져있으면 
            s_list[i] = s[i].upper()  # 해당 문자를 대문자로 바꿔주기
    return ''.join(s_list)