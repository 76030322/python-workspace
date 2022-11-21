'''
클래스 변수 : 클래스가 실행될때 생성
 - 프로그램 내에서 접근 가능
인스턴스(객체) 변수 : 객체가 생성될때 생성
 - 객체를 이용해서만 접근 가능
지역변수 : 특정 지역이 실행될때 생성
 - 특정 지역에서만 접근 가능
'''

# class Variable01:

#     def var(self):
#         v = 100
#         print('var v: ',v)

#     def var02(self):
#         print('20 v :  ',v )


# vv = Variable01()
# v = vv.var()
# vv.var02()

# print('-'*10)

# class var02:
#     def var(self):
#         self.v = 100    # 인스턴스(객체) 변수 >> class내부에서 사용가능한 변수
#         print('var : ',self.v)

#     def var02(self):
#         print('20 v : ',self.v)

# vv = var02()
# vv.var()
# vv.var02()

# print('-'*10)

# class Student:
#     def inputST(self):
#         self.name = input('이름 입력: ')
#         self.age = input('나이 입력: ')
#         i = 5
#         while i < 10:
#             print()
#             i += 5

#     def printST(self):
#         print(self.name,'님')
#         print(self.age,'살')

# s = Student()
# s.inputST()
# s.printST()


print('='*50)

class StudentInfo:

    def inputST(self):
        self.name = input('이름 입력: ')
        self.kor = int(input('국어 점수: '))
        self.eng = int(input('영어 점수: '))
        self.math = int(input('수학 점수: '))

    def sumST(self):
        self.sum = self.kor + self.eng + self.math

    def gradeST(self):
        self.avg = round(self.sum/3,2)
        grade = self.avg
        
        if grade >= 90: return 'A'
        elif grade >= 80: return 'B' 
        elif grade >= 70: return 'C' 
        else: return 'F'

    def prInfoST(self,grade):
        print(f'이름: {self.name}')
        print(f'총합: {self.sum}')
        print(f'평균: {self.avg}')
        print(f'등급 : {grade}')

stu = StudentInfo()
stu.inputST(); stu.sumST(); stGrade = stu.gradeST(); stu.prInfoST(stGrade)
