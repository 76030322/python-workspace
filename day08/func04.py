'''
지역변수(local variable)
 - 특정 지역에서만 사용가능
전역변수(global variable)
 - 코드 전체에서 사용가능
'''

def func01():
    global a
    print('func01 : ',a)

def func02():
    a = 200
    print('func01 : ',a)

a = 1234
func01()
func02()

def func2(a,b):
    a += 5; b *= 10;
    print('func2 : a = {}, b = {}'.format(a,b))

def func1():
    a = 5; b = 10;
    func2(a,b)
    print('func1 : a = {}, b = {}'.format(a,b))

func2(3,40)
func1()

def display():
    sumFunc()
    print('10까지의 합 : ', sum_)

def sumFunc():
    global sum_
    for i in range(num+1):
        sum_ += i

num = 10; sum_ = 0; 
display()
