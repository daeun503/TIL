# 1회차
def solution(s):
    length = [len(s)]
	
    for i in range(1, int(len(s)/2)+1):
        result = ''         # result 초기화
        word = s[:i]        # 기준
        word_num = 1        # 기준 1부터 시작
        string = s[i:]      # for문 새로 돌 때 리셋 & [:i] 미리 없애고 시작
        
        while len(string):
            if word == string[:i]:                # 기준 문자와 다음 문자가 같을 때
                word_num += 1                     # num +1
            else:                                 # 기준 문자와 다음 문자가 다를 때
                result += str(word_num)+word if word_num != 1 else word
                word = string[:i]                 # 새로운 기준 문자 만들어주기
                word_num = 1                      # 새로운 기준 문자니까 num도 새로 1
            string = string[i:]                   # 기준 문자랑 다음 문자랑 비교한 후엔 맨 앞에 문자 없애주기
        
        # while문 탈출했을 때, 마지막 단어 result에 추가해주기 
        result += str(word_num)+word if word_num != 1 else word
            
        # 길이별로 구한 압축 문장의 길이를 length에 추가
        length.append(len(result))
    
    return min(length)