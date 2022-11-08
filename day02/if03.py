'''
제어문
 - 프로그램의 흐름을 제어한다.
 - if, for, while, break, continue

 if 조건식:
    종속문장
 다음문장
'''
'''
print('1.쉬운 게임')
print('2.어려운 게임')
print('3.종료')
num = int(input(">>>>> : "))
if num == 1:
    print('쉬운게임 실행!!!')
if num == 2:
    print('어려운게임 실행!!!')
if num == 3:
    print('게임을 종료합니다!!!')
'''

'''
n1 = 5; n2 = 10;
if n1 > n2 :
    print('n1이 n2보다 크다')
if n1 < n2 :
    print('n2가 n1보다 크다')
'''

'''
print('==== 짝수판단 ====')
n1 = int(input('수 입력: '))
if n1 % 2 == 0:
    print(f'{n1}은(는) 짝수다')
    print('n1은 2의 배수이다')
    print('종속문장들 실행')
print('다음문장 실행')
print('다음문장 실행')
'''

'''
# 절대값을 구하는 프로그램 만들기
u_num = input('수 입력: ')
if float(u_num) >= 0:
    print(f'입력한 {u_num}의 절대값은 {u_num}입니다.')
if float(u_num) < 0:
    print(f'입력한 {u_num}의 절대값은 {-float(u_num)}입니다.')
'''

# 세 수를 입력받아 가장 큰 수 출력
n1 = int(input('수 입력: ')); n2 = int(input('수 입력: ')); n3 = int(input('수 입력: '))
n_max = 0
if n1 >= n2 and n1 >= n3:
    n_max = n1
if n3 >= n1 and n3 >= n2:
    n_max = n3
if n2 >= n_max:
    n_max = n2
print(n_max)