# class AAA:
#     def test1(self):
#         print('test1')
#         print(self.num)

# a = AAA()
# a.num =12345
# a.test1()

# class BBB:
#     aaa = '안녕하세요'
#     def test1(self):
#         print('test1')
#         print(self.aaa)
#         print(BBB.aaa)

# # b = BBB()
# # b.test1()

# print(BBB.aaa)
# BBB.num = '넘입니다.'
# print(BBB.num)

# b = BBB()
# b.bbb = 'bbb입니다.'
# print(b.num)
# print(b.bbb)

# def test():
#     b = BBB()
#     b.test1()

# test()

# class CCC:

#     a = 'aaaa'

#     def test():
#         print('test입니다.')

#     def test1(self):
#         print('self입니다.')

# CCC.test()

# # CCC.test1() # self는 객체가 만들어졌을때 실행이 된다.

# c = CCC()
# c.test1()
# # c.test()

'''
생성자
 - 객체가 만들어질때 자동으로 호출되는 메소드
 - __int__(self)이름을 사용한다
 - 일반적으로 변수 초기화 목적으로 사용한다.
'''

# class TestClass:
#     def __init__(self):
#         print('생성자 실행')

# t = TestClass()

# class TestClass02:
#     def __init__(self, name):
#         self.name = name

#     def printName(self):
#         print('당신의 이름은: ',self.name)
# n = input('이름 입력: ')
# t = TestClass02(n)
# t.printName()

# class TestClass03:
#     def __init__(self,version,memory):
#         self.version = version
#         self.memory = memory

#     def setVersion(self,version):
#         self.version = version

#     def printM(self):
#         print('버전: ',self.version)
#         print('메모리: ',self.memory)

#     def __str__(self):
#         # return '원하는 값 표현'
#         return f'{self.version},{self.memory}'

# t = TestClass03('win11','16GB')
# t.setVersion('버전 정보')
# t.printM()

# print('t: ', t)

import os

class Computer:

    def __init__(self,cpu,memory,tech1,tech2):
        self.cpu = cpu
        self.memory = memory
        self.tech1 = tech1
        self.tech2 = tech2

    def comStatus(self):
        print('cpu:',self.cpu)
        print('memory:',self.memory)
    
    def comTech(self):
        print('계산기:',self.tech1)
        print('메모장:',self.tech2)

c = Computer('R9','32GB','calc','notepad')


cho = None
while True:
    os.system('cls')
    print('1.version확인');print('2.기능확인');print('3.종료');cho=input('>>> ')

    if cho == '1':
        print('사양을 보여 줍니다.')
        c.comStatus()
        os.system('pause')

    elif cho == '2':
        choice = None
        print('기능을 보여 줍니다.')
        c.comTech()

        choice = input('사용할 기능 입력: ')
        if choice == '계산기' or choice == 'calc':
            os.system('calc')
        elif choice == '메모장' or choice == 'notepad':
            os.system('notepad')
        else:
            print('구현되지 않은 기능입니다.')

    elif cho == '3': break
    else: continue