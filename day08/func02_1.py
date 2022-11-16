def thrD(n):
    if n % 3 == 0:
        print(f'{n}은 3의 배수입니다.')
    else:
        print(f'{n}은 3의 배수가 아닙니다')

def odN(n):
    cnt = 0
    for i in range(2,n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 1:
        print(f'{n}은 소수 입니다.')
    else:
        print(f'{n}은 소수가 아닙니다')

def revN(n):
    temp = 0
    while True:
        temp = n % 10 
        n //= 10
        print(temp, end="")
        if not n:
            print()
            break

def calcN(n1,n2,a):
    if a == '+':
        print(f'{n1} {a} {n2} = {n1+n2}')
    elif a == '-':
        print(f'{n1} {a} {n2} = {n1-n2}')
    elif a == '*':
        print(f'{n1} {a} {n2} = {n1*n2}')
    elif a == '/':
        print(f'{n1} {a} {n2} = {n1/n2}')
    else:
        print(f'입력한 {a}는 연산자가 아닙니다.')

def toTal(n1,n2,p):
    thrD(n1)
    thrD(n2)
    odN(n1)
    odN(n2)
    revN(n1)
    revN(n2)
    calcN(n1,n2,p)

if __name__=="__main__":
    n1 = int(input('수 입력: '))
    n2 = int(input('수 입력: '))
    p = input('연산자 입력: ')
    toTal(n1,n2,p)
