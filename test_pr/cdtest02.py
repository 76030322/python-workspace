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
