# # 이상한 계산기
# # 빼기는 더하기, 더하기는 빼기, 곱하기는 나누기, 나누기는 곱하기로 계산하도록 만드시오.
# # 단, 연산자 3회 입력 실패시 프로그램 종료
# # 입력 받는 값은 전부 전역변수로 받고 함수로 결과값을 출력하세요.

# # 1번 풀이
# def numC():
#     # global n1, n2, m
#     numP(n1,n2,m)

# def numP(a,b,c):
#     global cnt; global button; 
#     if m == '+':
#         print(f'{a} {c} {b} = {a-b}')
#     elif m == '-':
#         print(f'{a} {c} {b} = {a+b}')
#     elif m == '*':
#         print(f'{a} {c} {b} = {a/b}')
#     elif m == '/':
#         print(f'{a} {c} {b} = {a*b}')
#     else:
#         cnt += 1
#         if cnt == 3:
#             print('종료!')
#             button = False
#         else:
#             print('이상한거 집어넣지 마세요!')

# # 2번 풀이
# def numC():
#     global cnt,button
#     if m == '+':
#         print(f'{n1} {m} {n2} = {n1-n2}')
#     elif m == '-':
#         print(f'{n1} {m} {n2} = {n1+n2}')
#     elif m == '*':
#         print(f'{n1} {m} {n2} = {n1/n2}')
#     elif m == '/':
#         print(f'{n1} {m} {n2} = {n1*n2}')
#     else:
#         cnt += 1
#         if cnt == 3:
#             print('종료!')
#             button = False
#         else:
#             print('이상한거 집어넣지 마세요!')

# button = True; cnt = 0; 
# while button:
#     n1 = int(input('수 입력: ')); n2 = int(input('수 입력: ')); m = input('연산자 입력: '); 
#     numC()


# # 어떤 양의 정수 n의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# # 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. n이 주어졌을 때,
# # 1보다 크거나 같고, n보다 작거나 같은 한수의 개수를 구하는 함수를 작성하시오. 
# # 단, n < 1,000

# def hansu(n) :
#     cnt = 0
#     if n < 100 :
#         return n
#     else :
#         for i in range(1, n+1) :
#             if i < 100 :
#                 cnt += 1
#             else :
#                 ls = []
#                 for j in str(i) :
#                     ls.append(int(j))
#                 if ls[0] - ls[1] == ls[1] - ls[2] :
#                     cnt += 1
#         return cnt

# n =int(input('수 입력: '))
# a = hansu(n)
# print(a)

# # 10만원짜리 마우스는 매일 가격 8퍼센트씩오른다 20만원이 넘어가면 그 시점에 반값이되고 되풀이된다 n일 후 가격을 계산하시오.(소수점 2자리까지만 표시)

# def inP():
#     global gMouse;  
#     for i in range(n):
#         gMouse += gMouse*0.08
#         if gMouse > 200000:
#             gMouse /= 2

# def pdD():
#     inP()
#     print(f'{n}일 후 마우스가격 : {round(gMouse,2)}')        

# gMouse = 100000
# n = int(input('날짜 입력: '))
# pdD()

# 문제
# 6명의 학생의 점수를 입력받고 리스트로 저장
# 입력받은 6명의 학생의 점수 중 제일 높은 점수 출력

# def max(li):
#     max_num = 0
#     for i in li:
#         if max_num < i:
#             max_num = i
#     return max_num

# def ip():
#     for i in range(1,6+1):
#         score = int(input(f'{i}번째 학생 점수 입력: '))
#         li.append(score)
#     return li
# li = []
# a = ip()
# print('제일 높은 점수:', max(li))
