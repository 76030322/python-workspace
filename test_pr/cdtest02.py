import os

# # 첫날 10원을 입금하고 그 다음날 부터 2배씩 30일동안 저축을한다면 저축된 금액은 얼마인가?
# a = 10
# b = 0
# for i in range(30):
#     b += a # 총 저축금액
#     a *= 2 # 그 다음날 넣을 금액
# print(f'30일날 저축된 금액은 {b:,}원이다.')

# # N을 입력 받은뒤, 구구단 N단을 출력하는 프로그램을 만드시오. 단, 음수를 입력할 시 프로그램을 강제 종료 시키세요
# n = int(input('수 입력: '))
# if n < 0 :
#     print('잘못 입력했습니다.')
#     os.system('pause')
#     os._exit(1)
# for i in range(1,10): # 세로
#     for j in range(2,n+1):
#         print(f'{j} X {i} = {i*j}',end="\t")
#     print()
# print("="*15*n)
# for i in range(2,n+1): # 가로
#     for j in range(1,10):
#         print(f'{i} X {j} = {i*j}',end="\t")
#     print()

# print(); print()

# # 별찍기! 줄수에 맞춰 별의 개수 증가 시키기
# n = int(input('줄 수 입력: '))
# for i in range(1,n+1):
#     for j in range(i):
#         print('*',end="")
#     print()

# # a, b, n은 무조건 양수이고 아닐시 시스템을 종료시킨다.
# # b > a 
# a = int(input('수 입력: ')); b = int(input('수 입력: ')); n = int(input('수 입력: '))
# sumN = 0;
# if a < 0 or b < 0 or n < 0:
#     os._exit(1)
# else:
#     for i in range(a,b+1):
#         sumN += i
#         if sumN == n:
#             print(f'입력하신 {n}은 {i}번째 합과 같습니다.')
#             break
#         elif sumN > n:
#             print(f'입력하신 {n}과 {i}번째 합인 {sumN}과의 차는 {sumN-n}입니다.')
#             break
#     if n > sumN :
#         print(f'입력하신 {n}은 범위값을 벗어났습니다.')

# # 임의의 정수 n을 입력 받을 때 각자리의 수를 비교해서 짝수의 합과 홀수의 합을 구하시오.
# # 단, n은 양의 정수
# n = int(input('수 입력: '))
# d_sum = 0; o_sum = 0;
# if n < 0 :
#     print('잘못입력했습니다.')
#     os._exit(1)
# else:
#     for i in str(n):
#         if int(i) % 2 == 0:
#             d_sum += int(i)
#         else:
#             o_sum += int(i)
# print(f'짝수의 합: {d_sum}\n홀수의 합: {o_sum}')

# # 매주 화요일은 분리수거의 날, 1일이 목요일일때 이번달 분리수거의 날짜와 횟수를 구하시오. 이번달은 31일까지 있다.
# cnt = 0
# for i in range(1,32):
#     if i % 7 == 6:
#         cnt += 1
#         if i != 27:
#             print(f'{i}일',end=", ")
#         else:
#             print(f'{i}일',end=" | ")
#     if i == 31:
#         print(f'총 : {cnt}번 있다')
    
# # 맥주 1캔: 3,000원이고 현재 3+1행사 중이다. 맥주의 개수를 입력받고 할인금액과 총금액을 출력하시오
# canB = int(input('구입할 맥주 캔 : '))
# to_m = canB * 3000; cnt = 0;
# if canB < 0:
#     print('잘못입력했습니다')
#     os.exit(1)
# else:
#     for i in range(1,canB+1):
#         if i % 4 == 0:
#             cnt += 1
# mo_d = cnt * 3000;
# print(f'전체 금액 - 할임 금액 : {to_m} - {mo_d}\n총 금액: {to_m - mo_d}')

# # 1 부터 N까지 이어적는 프로그램을 만들고 출력값과 총 길이를 구하시오.
# n = int(input('수 입력: ')); cnt = 0
# for i in range(1,n+1):
#     for j in range(i):
#         cnt += 1
#         print(f'{i}',end="")
# print(f'\t총 길이: {cnt}')

# # 1~10까지의 수의 곱을 구하시오
# n = 1
# for i in range(1,11):
#     n *= i
# print(f'1부터 10까지 곱한 값: {n:,}')

# # 공백을 제외한 나머지 문자들의 갯수를 구하시오
# st = 'It is a fun python class'; cnt = 0
# for i in st:
#     cnt += 1
#     if i == ' ':
#         cnt -= 1
# print(cnt)

# # 입력받은 수를 조합해서 가장 큰수가 나오게 하시오.
# num = int(input('수 입력: ')); n_sum = 1
# if num < 0:
#     num *= -1
# for i in str(num):
#     if i == '0':
#         n_sum += int(i)
#     else:
#         n_sum *= int(i)
# print(n_sum)

# # 숫자 5개를 받아 합계, 평균을 구하시오
# print('수를 입력하세요!'); n_sum = 0;
# for i in range(5):
#     num = float(input('수 입력: '))
#     n_sum += num
# print(f'총 합: {round(n_sum,2)}\n평균: {round(n_sum/5,2)}')


# # 비행기자리 예매 프로그램
# pl_s = 30; hu_ct = 0;
# while True:
#     print('{:=^30}'.format('좌석 예약 프로그램'))
#     hu_s = int(input('일행 수 입력: '))

#     if hu_s == 0:
#         print('다시 입력하세요')
#         continue

#     if pl_s >= hu_s:
#         for i in range(hu_s):
#             pl_s -= 1
#     else:
#         print(f'예약 가능한 좌석이 부족합니다.\n남은 좌석 수: {pl_s}')
#         continue
#     if pl_s == 0:
#         print('예약 가능한 좌석이 없습니다.\n다음에 이용해주세요')
#         break

#     if hu_s == 1 and hu_ct == 0:
#         hu_ct += 1
#         print(f'{hu_ct}번 좌석입니다')
#     elif hu_s == 1 :
#         print(f'{hu_ct}번 좌석입니다')
#     else:
#         if hu_ct == 0:
#             hu_ct += 1
#             print(f'{hu_ct}부터 {hu_ct+hu_s-1}번 좌석입니다')
#         else:
#             print(f'{hu_ct}부터 {hu_ct+hu_s-1}번 좌석입니다')
#     hu_ct += hu_s
#     print(f'예약 가능한 좌석 수: {pl_s}')

# # 문자열 입력 후 검색하고 싶은 문자하나를 입력하고 그 문자가 문자열에 있다면 개수를 출력하시오
# st = input('아무 문자열이나 입력하세요: '); fi_s = input('찾고자 하는 문자를 입려하세요: '); cnt = 0;
# for i in st:
#     if i == fi_s:
#         cnt+=1
# if cnt == 0:
#     print('찾고자하는 문자는 이 문자열에 없습니다.')
# else:
#     print(f'입력한 {fi_s}는 총 {cnt}개 있습니다.')

# # 경우의 수
# mo, mo1, mo2 = 1024, 1024, 1024
# for i in range(4):
#     mo1 *= 2; mo2 //= 2
#     print(f'{mo1:,}원 {mo2:,}원', end=' ')
# print(f'{mo:,}원')

# # 소수구하기
# num = int(input('수입력 [ 1보다 큰 수를 입력하세요 ]: '))
# if num <= 1:
#     print('다시 입력하세요')
#     os._exit(1)
# else:
#     for i in range(2,num+1):
#         cnt = 0
#         for j in range(2,i):
#             if i % j == 0:
#                 cnt += 1
#         if cnt == 0:
#             print(f'{i}', end=' ')

# 사용자가 입력한 정수값까지의 합을 구하는 프로그램을 만드시오

# a = None
# while True:
#     print('='*20); print('1.실행\n2.종료') ;print('='*20); a = input('선택: ')
#     if a == '1':
#         num = 0; n_sum = 0;
#         print('\n1 부터 입력하신 수까지 더한 값을 출력해주는 계산기입니다. 수를 입력해 주세요',end='\t')
#         num = int(input('>>> '))
#         if num == 1:
#             print('1은 의미없습니다\n')
#             continue
#         for i in range(1,num+1):
#             n_sum += i
#         print(f'1 부터 입력하신 {num:,}까지의 합은 {n_sum:,}입니다.\n')
#         continue
#     elif a == '2':
#         print('이용해 주셔서 감사합니다.\n')
#         os._exit(0)
#     else:
#         print('잘못 입력했습니\n다시입력해주세요')
#         continue

# # 4부터 21까지 홀수의 합을 구하시오
# o_sum = 0
# for i in range(4,22):
#     if i % 2 != 0:
#         o_sum += i
# print(f'{o_sum}')


# # 100보다 작은숫자 N을 입력했을때 다음과 같은 과정으로 새로운 수를 만들고 몇번 만에 최초숫자로 돌아오는지 확인하는 프로그램 만들기
# # 조건: 1) 십의 자리수와 일의 자리수를 더한다   2) 처음숫자의 일의 자리수를 십의자리에 1)의 결과값의 십의자리수를 일의자리에 둔다

# num = 0; ch = None; 
# while True:
#     os.system('cls')
#     print('1.실행 2.종료 |', end='\t'); ch = input('>>> ')
#     if ch == '1':
#         num = int(input('100보다 작은 정수값 입력: '));

#         if num < 0 or num > 100:
#             print('설정값을 벗어났습니다.')
#             continue

#         o,t,ot,newN,nO,nT = 0,0,0,0,0,0; b = 1; num1 = num; cnt = 0; 

#         while b:

#             o = num1%10; t = num1//10; ot = o + t; nO = ot%10; nT = ot//10; 

#             if newN == 0:
#                 newN = o*10 + ot%10
#                 print(f'\n입력한 값: {num1}')
#                 print(f"1) {t} + {o} = {ot}\n2) {t}'{o}'\t{nT}'{nO}'\n")
#             elif newN != 0:
#                 newN = o*10 + ot%10
#                 print(f'바뀐 수 = {num1}')
#                 print(f"1) {t} + {o} = {ot}\n2) {t}'{o}'\t{nT}'{nO}'\n")
#             num1 = newN; cnt+=1

#             if num == newN :
#                 b = 0
#                 print(f'총 반복 회수: {cnt}\n')
#                 os.system('pause')

#     elif ch == '2':
#         print('시스템을 종료합니다.\n')
#         os._exit(0)
#     else:
#         continue