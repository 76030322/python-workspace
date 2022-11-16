'''
함수(메소드)
 - class 안에 함수가 있으면 메소드라 호칭
 - class 없이 함수만 있으면 함수
 - 어떤 기능이 있다면 함수라고 한다.
 - 소괄호가 존재하면 거의 함수다.

사용방법
def '이름'( args ): # args = 매개변수
    종속문장
    return value      
'''

# 디버깅 할시 f10은 그냥 줄만 확인해서 내려가고 f11은 함수까지 포함해서 넘어간다

def reverseCode():
    temp = 0
    result = int(input('수 입력: '))
    while True:
        temp = result % 10 
        result = result // 10
        print(temp, end=", ")
        if not result:
            break
    print('프로그램 종료')

def test():
    print('test')

def test1():
    print('test1')

def test2():
    print('test2')

def test3():
    print('test3')

# if_name__ == "__main__":
#    함수()

if __name__ == '__main__': # 같은 파일에서 실행하면 if내부의 값이 실행이 되고 다른 파일에서 사용하면 if내부의 값이 실행되지 않는다.
    print('시작')
    reverseCode()
    print('종료')