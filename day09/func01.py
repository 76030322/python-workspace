def sum_func(x1=1,x2=22,x3=100): # default값을 설정해줄 수 있으며 해당하는 값을 받으면 그 값을 우선 처리한다.
    re = x1 + x2 + x3
    return re

print(sum_func(10,20))
print(sum_func(10,20,30))

print(sum_func(x3 = 200)) # 해당하는 변수에 직접 입력은 가능하나, 값만 입력시 변수의 등록순으로 나아간다.

# 요금 구하는 프로그램 만들기

def trM(cho='1'):
    price = 500;
    if cho == '1':
        print(f'{price}원')
    elif cho == '2':
        b = int(input('환승 횟수: '))
        add_p = 500
        for i in range(b-1):
            add_p *= 2
        price += add_p
        print(f'{price}원')
    elif cho == '3':
        print(f'{2*price}원')
    else:
        print('잘못입력했습니다.')
        return

print('1.환승 안함 2.환승 함 3.장거리')
a = input('선택: '); trM(a); trM()


# 아르바이트 계산기
# 1. 기본급 2.일한 시간설정 3.시급 설정 4.시간&시급 설정

def albaChoice():
    print('1. 기본금 2.일한 시간설정 3.시금 설정 4.시간&시급 설정')
    cho = input('선택: ')
    if cho == '1':
        albCalc()
    elif cho == '2':
        a = int(input('시간 입력(시간단위): '))
        albCalc(x1=a)
    elif cho == '3':
        b = int(input('시급 설정: '))
        albCalc(x2=b)
    elif cho == '4':
        a = int(input('시간 입력(시간단위): '))
        b = int(input('시급 설정: '))
        albCalc(x1=a,x2=b)
    else:
        print('잘못입력했습니다.')
        return

def albCalc(x1=240,x2=12000):
    print(f'금액: {x1*x2:,}원')
    return

albaChoice()