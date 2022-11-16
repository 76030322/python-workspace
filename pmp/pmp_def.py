import os,random

def nDis(x):
    if x == False: print('잘못된 입력값입니다'); os.system('pause'); os.system('cls')
    else: print(x); os.system('pause'); os.system('cls')

def nCalc(x,y,z):
    if z == '+': return x+y
    elif z == '-': return x-y
    elif z == '/': return x/y
    elif z == '//': return x//y
    elif z == '%': return x%y
    elif z == '*': return x*y
    else: return False

def nRandom(x,y):
    rNum = random.randrange(x,y+1); return rNum

def mDict(x):
    
    button = True; choice = None; count = 0; 
    
    while button:

        if count == 0:

            print('value의 형태를 지정하시오')
            print('1.default 2.list 3.dictionary'); choice = input('>>> ')

            if choice == '1':
                a = input('key값 입력 : ')
                b = input('value값 입력: ')

            elif choice == '2':
                b = []
                a = input('key값 입력 : ')
                cnt = input('list_count 입력: ')
                for i in range(int(cnt)):
                    c = input("value's list값 입력: ")
                    b.append(c)

            elif choice == '3':
                b = {}
                a = input('key값 입력 : ')
                cnt = input('dictonary_count 입력: ')
                for i in range(int(cnt)):
                    c = input("value's key값 입력: ")
                    d = input("value's value값 입력: ")
                    b[c] = d

            else:
                a = input('key값 입력 : ')
                b = input('value값 입력: ')

            x[a] = b
            count += 1

        else:
            print('1: 추가\t 2. 종료'); choice = input('>>> ')
            if choice == '1': count = 0
            elif choice == '2': button = False
            else: button = False

if __name__=='__main__':
    os.system('cls')
    test = {}
    mDict(test)
    print(test)
    pass

