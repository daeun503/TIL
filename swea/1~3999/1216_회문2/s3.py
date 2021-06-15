import sys
sys.stdin = open("input.txt", "r")

# 회문 / stack을 하려고 했는데 :(
def my_func(box):
    result = 0
    for text in box:
        for i in range(len(text)):
            tmp = list(text[:i])
            palindrome_cnt = 0
            flag = 0

            # 회문 길이가 홀수 / 짝수일 때
            if tmp[-2:-1] == [text[i]]:   # 짝수는 tmp[-2] == (이후) text 첫 요소
                flag = 1                  # 회문확인 하려면 flag
                tmp.pop()                 # 홀수는 pop두번 cnt +3
                tmp.pop()
                palindrome_cnt += 3
            elif tmp[-1:] == [text[i]]:   # 짝수는 tmp[-1] == (이후) text 첫 요소
                flag = 1                  # 회문확인 하려면 flag
                tmp.pop()                 # 짝수는 pop한번 cnt +2
                palindrome_cnt += 2

            j = 1
            while flag and i+j < len(text):  # flag가 1이면 text[i+j] 까지 회문인지 확인
                if tmp[-1:] == [text[i+j]]:  # 자기 짝이 있으면
                    tmp.pop()                # tmp pop해주고 cnt +2
                    palindrome_cnt += 2
                    # 만약 확인하는 요소가 txt의 끝이면 else문으로 안가고 끝나니까 여기서 result확인
                    if i + j == len(text) - 1 and result < palindrome_cnt:
                        result = palindrome_cnt
                else: # 자기 짝이 없으면 회문이 끝난거니까 회문 길이 확인해서 큰 값을 result에 넣어주기
                    if result < palindrome_cnt: result = palindrome_cnt
                    break
                j += 1

    return result

for _ in range(1, 11):
    tc = int(input())
    cnt = 0
    box = [input() for _ in range(100)]                        # 정방향
    rotated_box = [''.join(char) for char in list(zip(*box))]  # 회전

    a = my_func(box)
    b = my_func(rotated_box)

    print("#{} {}".format(tc, max(a, b)))
