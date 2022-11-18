'''
class
 - 틀, 틀안에 모든 기능과 변수가 존재한다.
 - 하나의 자료형

객체
 - 클래스 자료혀응로 변수를 만들면 객체라고 표현한다.

메소드
 - 클래스안에 함수를 만들면 메소드라 한다.

절차지향 >> 각각의 함수를 만듬어 사용 틀(x) // 대표: c
객체지향 >> 객체(class)안에 함수와 변수를 집어넣어 하나의 틀로 움직임 // 대표: python, java

'.' >> 멤버접근연산자
'''

st = 'aaa'

class Info:
    name = None
    addr = None
    age = None
    stNum = None
    phNum = None

s = Info()
s.name = '홍길동'; s.age = 20; s.addr = '산골짜기'

print(s.name, s.addr, s.age)

import os, time

# for i in range(1000):
#     print("ε="*i, end="")
#     if i % 2 == 0:
#         print("┌( ﾟДﾟ)┘")
#     else:
#         print("└( ﾟДﾟ)┐")
#     time.sleep(0.1)
#     os.system("cls")

def test():
    info  = Info()
    info.name = 'test'
    print(info.name)

def test1():
    info  = Info
    info.name = '연습중'
    print(info.name)

test()
test1()

class Myclass:
    name = None
    def test(self):
        print('test 메소드 입니다')
        print(self)
        print('=='*30)

c = Myclass()
c.test()
print(c)

class MethodTest01:
    def sumFunc(self):
        n1 = int(input('수 입력: '))
        n2 = int(input('수 입력: '))
        s = n1 + n2
        print('합: ',s)

    def myInput(self):
        n1 = int(input('수 입력: '))
        n2 = int(input('수 입력: '))
        return n1, n2
    
    def sumN(self,n1,n2):
        return n1 + n2

    def myPrint(self, *t):
        print(f'{t[0]} + {t[1]} = {t[2]}')
        print()
obj = MethodTest01()
# obj.sumFunc()
# tul = obj.myInput()
a,b = obj.myInput()
c = obj.sumN(a,b)
obj.myPrint(a,b,c)
