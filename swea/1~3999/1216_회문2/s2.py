import sys
sys.stdin = open("input.txt", "r")

def palindrome(string, length):
    for i in range(len(string) - length + 1):
        a = string[i:i + length]
        if a[::] == a[::-1]:
            return True
    else:
        return False


for _ in range(1, 2):
    test = int(input())
    max_length = 0
    for length in range(100, -1, -1):
        if palindrome('ABAABA', length):
            if max_length < length:
                max_length = length
                break

    print('#{} {}'.format(test, max_length))
