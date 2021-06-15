def func2():
    print('함수 2 시작')
    print('함수 2 종료')

def func1():
    print('함수 1 시작')
    func2()
    print('함수 1 종료')

print('메인시작')
func1()
print('메인끝')

"""
메인시작
함수 1 시작
함수 2 시작
함수 2 종료
함수 1 종료
메인끝
"""
