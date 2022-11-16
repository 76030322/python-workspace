from func02_1 import *

def sumFunc():
    sum_ = 0
    num = int(input('수 입력:'))    
    for i in range(num+1):
        sum_+=i
    print(f'1 ~ {num}까지의 합: {sum_}')

def sumFunc1(num):
    sum_ = 0
    for i in range(num+1):
        sum_+=i
    print(f'1 ~ {num}까지의 합: {sum_}')

def sumFunc2(num):
    sum_ = 0
    for i in range(num+1):
        sum_+=i
    return sum_

def sumInput():
    num = int(input('수 입력: '))
    return num

def sumPrint(num,sum_):
    print(f'1 ~ {num}까지의 합 : {sum_}')

def sumT():
    a = sumInput()
    s = sumFunc2(a)
    sumPrint(a,s)

if __name__=='__main__':
    
    # sumFunc()

    # num1 = int(input('수 입력:'))
    # sumFunc1(num1)

    # num2 = int(input('수 입력: '))
    # sum_ = sumFunc2(num2)
    # print(f'1 ~ {num2}까지의 합: {sum_}')
    
    # a = sumInput()
    # sum_ = sumFunc2(a)
    # sumPrint(a,sum_)

    sumT()

    ls = set()
    ls.add(10)
    print('ls : ',ls)
    result = ls.pop()
    print(result)
    print('ls: ',ls)

n1 = int(input('수 입력: '))
n2 = int(input('수 입력: '))
p = input('연산자 입력: ')
toTal(n1,n2,p)
