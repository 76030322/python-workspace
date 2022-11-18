# [문항1] 1.아래의 내용을 보고 문제를 해결하시오(풀이 코드 올려주세요)

# 1).입력한 데이터가 3의 배수인 경우 출력 하시오.
# 2).수를 입력 받아 짝,홀수를 구분하여 출력 하시오.
# 3).두수를 입력 받아 큰 수를 출력 하시오.
# 4).수를 입력받아 절대값을 구하는 프로그램을 작성 하시오.

# # 1-1
# n = int(input('수 입력: '))
# if n != 0:
#     if n%3 == 0:
#         print(f'{n}은 3의 배수입니다.')
#     else:
#         print(f'{n}은 3의 배수가 아닙니다.')
# else:
#     print('0을 제외한 수 입력')

# # 1-2
# n = int(input('수 입력: '))
# if n%2 == 0:
#     print(f'{n}은 짝수입니다')
# else:
#     print(f'{n}은 홀수입니다.')

# # 1-3
# n1 = int(input('수 입력: '))
# n2 = int(input('수 입력: '))
# if n1 > n2:
#     print(n1)
# elif n2 > n1:
#     print(n2)
# else:
#     print('두수는 같다')

# # 1-4
# n = int(input('수 입력: '))
# if n >= 0:
#     print(n)
# else:
#     print(-n)

# [문항2] 2.아래의 내용을 보고 문제를 해결하시오(풀이 코드 올려주세요)

# 1).날짜를 입력 받아 요일을 구하시오.
# 단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일
# 어떤 값을 입력 받던 요일이 정확히 출력 되게 만드시오.
# 2).세수를 입력 받아 큰 수를 출력 하시오.
# 3).두수를 입력 받아 큰 수가 짝수이면 출력 하시오.
# 4).두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력 하시오.

# # 2-1
# day = int(input('날짜 입력(1~30): '))
# if day<=0 or day>30:
#     print('잘못입력했습니다.')
# else:
#     if day%7 == 1: print('월요일')
#     elif day%7 == 2: print('화요일')
#     elif day%7 == 3: print('수요일')
#     elif day%7 == 4: print('목요일')
#     elif day%7 == 5: print('금요일')
#     elif day%7 == 6: print('토요일')
#     else: print('일요일')

# # 2-2
# a = int(input('수 입력: ')); b = int(input('수 입력: ')); c = int(input('수 입력: '));
# max_ = 0
# if a>c and a>b: max_ = a
# elif b>a and b>c : max_ = b
# else: max_ = c
# print(max_)

# # 2-3
# n1 = int(input('수 입력: ')); n2 = int(input('수 입력: '));
# if n1>n2 and n1%2==0: print(n1)
# elif n2>n1 and n2%2==0: print(n2)
# elif n1==n2 and n1%2==0: print(n1)
# else:
#     print('조건에 부합하지 않습니다.')

# # 2-4
# n1 = int(input('수 입력: ')); n2 = int(input('수 입력: '));
# a = n1+n2
# if a%6 ==0: print(a)
# else: print('조건에 부합하지 않습니다.')

# [문항3] 3.아래의 내용을 보고 문제를 해결하시오(풀이 코드 올려주세요)

# 1).1~100 까지의 총 합을 구한다. 단, 3의 배수는 제외하고 3의 배수이며 5의 배수는 제외하지 않는 조건이다.

# 2).두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오
# 1입력, 10입력 => 55
# 10입력,1입력 => 55

# 3).첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한달(30일) 이 되는 날 입금해야 하는 금액은 얼마인지 구하시오
# (첫날 10, 둘 째날 20 , 셋 째날 40 . . .무조건 2배씩 증가되는 값이다)

# 4) 아래와 같이 출력되게 2중 for문을 이용하여 출력하시오
# 상위포문 0 일 때 하위 포문 : 0 0 0 0 0
# 상위포문 1 일 때 하위 포문 : 0 1 2 3 4
# 상위포문 2 일 때 하위 포문 : 0 2 4 6 8
# 상위포문 3 일 때 하위 포문 : 0 3 6 9 12
# 상위포문 4 일 때 하위 포문 : 0 4 8 12 16

# # 3-1
# to_sum = 0
# for i in range(1,101):
#     to_sum += i
#     if i%15 == 0:
#         to_sum += i
#     if i%3 == 0:
#         to_sum -= i
# print(to_sum)

# # 3-2
# a = int(input('수 입력: ')); b = int(input('수 입력: '));
# x = 0; y = 0; to_sum = 0;
# if a>b: x=b; y=a+1
# else: x=a; y=b+1
# for i in range(x,y):
#     to_sum += i
# print(to_sum)

# # 3-3
# a = 10; b = 0;
# for i in range(1,30):
#     b += a # 총 저축금액
#     a *= 2 # 그 다음날 넣을 금액
# print(f'저축할 금액은 {a:,}원이다')

# # 3-4
# for i in range(5):
#     print(f'상위포문 {i}일 때 하위 포문 : ',end='')
#     for j in range(5):
#         print(i*j,end=' ')
#     print()

# [문항4] 4. 랜덤과 set을 이용하여 로또 프로그램을 만드시오

# # 4
# import random
# lotto = set()
# while True:
#     lotto.add(random.randrange(1,46))
#     if len(lotto) == 6:
#         break
# print(lotto)

# [문항5] 5. 다음 내용을 lambda와 map을 이용하여 아래와 같이 표현하시오
# day = { '날짜' : ['2018.01.01.','2019.02.02','2020.03.03'] }

# 2018년 01월 01일
# 2019년 02월 02일
# 2020년 03월 03일

# # 5
# day = { '날짜' : ['2018.01.01.','2019.02.02','2020.03.03'] }
# a = list(map(lambda x : x.split('.'),day['날짜']))
# for i in a:
#     print(f'{i[0]}년 {i[1]}월 {i[2]}일')