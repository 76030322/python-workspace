class Bignum:
        
    def bigNum(a,b):
        if a > b :
            print(a)
        elif b > a:
            print(b)
        else:
            print('두 수는 같습니다.')

class EvenorOdd:
    
    def evenOrodd(a):
        if a%2==0: print(f'{a}은(는) 짝수입니다.')
        else: print(f'{a}은(는) 홀수입니다.')

class ThreeMul:

    def threeMul(a):
        if a%3==0: print(f'{a}은(는) 3의배수 입니다.')
        else: print(f'{a}은(는) 3의 배수가 아닙니다..')

class Decimalpoint:

    def decimalPoint(a):
        cnt = 0;
        for i in range(2,a+1):
            if a%i==0: cnt+=1
        if cnt == 1: print(f'{a}는 소수입니다.')
        else: print(f'{a}는 소수가 아닙니다.')

class Absolutevalue:

    def absoluteValue(a):
        if a < 0 : print(f'입력한 {a}의 절대값 : {-a}')
        else: print(f'입력한 {a}의 절대값 : {a}')

def inNum():
    n = int(input('수 입력: '))
    return n

n1 = inNum()
n2 = inNum()
a = inNum()

Bignum.bigNum(n1,n2)
EvenorOdd.evenOrodd(a)
ThreeMul.threeMul(a)
Decimalpoint.decimalPoint(a)
Absolutevalue.absoluteValue(a)