# # A, B, C에 각각 수를 입력 후 최대값과 최소값을 구하고 A * B * C가 3의 배수이면서 짝수일때는 최대값을 출력 3의 배수이면서 홀수일대는 최소값을 출력하시오.
# # 단, A, B, C는 정수만 입력이 가능하고 A * B * C의 값이 양수일때만 출력

# a = int(input('A값 입력: ')); b = int(input('B값 입력: ')); c = int(input('C값 입력: '))
# max_n, min_n = 0, 0; total = a*b*c
# if a >= b and a >= c:
#     if b >= c:
#         min_n = c
#     elif c >= b:
#         min_n = b
#     max_n = a
# elif b >= a and b >= c :
#     if a >= c:
#         min_n = c
#     elif c >= a:
#         min_n = a
#     max_n = b
# else:
#     if a >= b:
#         min_n = b
#     elif b >= a:
#         min_n = a
#     max_n = c
# if total > 0 and total != 0:
#     if total%2 == 0 and total%3  == 0:
#         print(f'최대값: {max_n}')
#     elif total%2 != 0 and total%3 == 0:
#         print(f'최소값: {min_n}')
#     else:
#         print('출력 실패')
# else:
#     print('출력 실패')

# # 생년월일을 정수로 8자리 입력받고 년, 월 일을 나눠서 출력하시오
# birth = int(input('생년월일 8자리를 입력하세요: '))
# year = birth//10000; month = (birth%10000)//100; day=(birth%10000)%100
# print(f'{year}년 {month}월 {day}일')

# # 윤년을 여부를 출력하시오
# # 윤년의 조건은 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때이다.
# year = int(input('년도를 입력하세요: '))
# if year % 400 == 0:
#     print(f'{year}은(는)윤년이다')
# elif year%4 == 0 and year % 100 !=0:
#     print(f'{year}은(는)윤년이다')
# else:
#     print(f'{year}은(는) 윤년이 아니다')

# # 알람 45분 일찍 설정하기 단, 시간은 24를 초과할 수 없고, 분은 60을 초과할 수 없다.
# c_hour = int(input('시간: ')); c_min = int(input('분: '))
# if 0 <= c_hour <= 23 and 0 <= c_min <= 59:
#     c_min -= 45
#     if c_min < 0:
#         c_hour -= 1
#         if c_hour < 0:
#             print(f'알람시간은 23시 {c_min+60}분 입니다.')
#         else:
#             print(f'알람시간은 {c_hour}시 {c_min+60}분 입니다')
#     else:
#         print(f'알람시간은 {c_hour}시 {c_min}분 입니다.')
# else:
#     print('잘못 입력했습니다.')

# # n명의 사람이 최소 한 조각 이상 피자를 먹을려면 피자를 몇 판 시켜야 하는지 출력 하시오. 단, 피자는 2~10조각으로 쪼갤수 있다.
# hu = int(input('사람 수 입력: ')); pi_sl = int(input('피자 한 판을 몇 조각으로 나뉠지 입력: '))
# piza = 0; pi_ad = hu//pi_sl; pi_adsl = hu%pi_sl
# if hu <= 0 or pi_sl < 2 or pi_sl > 10:
#     print('잘못 입력했습니다.')
# elif pi_ad == 0:
#     pi_ad += 1
#     piza += pi_ad
#     print(f'{hu:,}명의 사람들에게 피자 한판을 {pi_sl}조각으로 나눠 준다면 {piza:,}판이 필요합니다.')
# elif pi_ad > 0 and pi_adsl == 0:
#     piza += pi_ad
#     print(f'{hu:,}명의 사람들에게 피자 한판을 {pi_sl}조각으로 나눠 준다면 {piza:,}판이 필요합니다.')
# else:
#     piza += 1
#     piza += pi_ad
#     print(f'{hu:,}명의 사람들에게 피자 한판을 {pi_sl}조각으로 나눠 준다면 {piza:,}판이 필요합니다.')

# # 계산기(+,-,*,/)
# n1 = int(input('수 입력:')); n2 = int(input('수 입력:')); oper = input('연산 기호 입력: ')
# if oper == '+':
#     print(f'{n1} + {n2} = {n1+n2}')
# elif oper == '-':
#     print(f'{n1} - {n2} = {n1-n2}')
# elif oper == '*':
#     print(f'{n1} * {n2} = {n1*n2}')
# elif oper == '/':
#     print(f'{n1} / {n2} = {round(n1/n2)}')
# else:
#     print('잘 못 입력했습니다.')

# # 영화표 : 13,000원, 0~6세 : 구매X, 7~9: 5,000원 할인, 10대: 20% 할인, 20대: 10% 할인, 60대 이상: 40% 할인 이라 할 때 총 지불해야 할 금액은 얼마인가?
# m_ticket = 13000
# hu = int(input('예매할 표 개수: '));
# m_total = m_ticket * hu; hu_ct = 0; cb = 0;
# if hu > 0:
#     m_0 = input('0~6세가 있습니까? Y, N을 눌러 주세요: ')
#     if m_0 == 'y' or m_0 == 'Y':
#         print('영화표를 구매할 수 없습니다.')
#     elif m_0 =='n' or m_0 == 'N':
#         m_7 = int(input('7~9세: '))
#         hu_ct += m_7
#         cb += m_7*5000
#         m_10 = int(input('10대: '))
#         hu_ct += m_10
#         cb += m_10*(m_ticket*0.2)
#         m_20 = int(input('20대: '))
#         hu_ct += m_20
#         cb += m_20*(m_ticket*0.1)
#         m_60 = int(input('60대 이상: '))
#         hu_ct += m_60
#         cb += m_60*(m_ticket*0.4)
#         if hu - hu_ct >= 0:
#             cb = round(cb)
#             print(f'선택된 금액 - 할인금액 : {m_total:,} - {cb:,}\n총 지불액 : {m_total-cb:,}')
#         else:
#             print('잘못 입력했습니다.\n처음부터 다시해주세요!')
#     else:
#         print('잘못 입력했습니다.\n처음부터 다시해주세요!')
# else:
#     print('잘못 입력했습니다.\n처음부터 다시해주세요!')

# # 통신사 맞추기
# # 011 = SKT, 016 = KT, 019 = LGU, 010 = 알수없음 단, 전화번호 입력시 '-' 사용
# tel_nu = input('전화번호: ')
# phn3 = tel_nu.split('-')[0]
# if phn3 == '011':
#     print(f'전화번호 {tel_nu}의 통신사는 SKT 입니다.')
# elif phn3 == '016':
#     print(f'전화번호 {tel_nu}의 통신사는 KT 입니다.')
# elif phn3 == '019':
#     print(f'전화번호 {tel_nu}의 통신사는 LGU 입니다.')
# elif phn3 == '010':
#     print(f'전화번호 {tel_nu}의 통신사는 알 수 없습니다.')
# else:
#     print('잘 못 입력했습니다.\n다시 입력해 주세요')

# # 나이에 맞는 교통요금을 출력하는 프로그램을 만드시오.
# #  8세 미만: 450원, 8세 이상 19세 미만 청소년: 720원, 20세 이상 성인: 1250원
# h_age = int(input('나이를 입력하세요: '));
# if h_age < 0:
#     print('다시입력하세요!')
# else:
#     if 0 <= h_age < 8:
#         print('어린이 입니다.\n교통요금은 450원 입니다.')
#     elif 8<= h_age <= 19:
#         print('청소년 입니다.\n교통요금은 720원 입니다.')
#     else:
#         print('성인 입니다.\n교통요금은 1,250원 입니다.')

# # 출생년도를 입력받아 무슨띠인지 찾는 프로그램을 만드시오.
# h_year = int(input('태어난 년도를 입력하세요: ')); h_an = h_year%12
# if h_year <= 0:
#     print('잘 못 입력했습니다.')
# else:
#     if h_an == 0:
#         print(f'{h_year}은 원숭이띠 입니다.')
#     elif h_an == 1:
#         print(f'{h_year}은 닭띠 입니다.')
#     elif h_an == 2:
#         print(f'{h_year}은 개띠 입니다.')
#     elif h_an == 3:
#         print(f'{h_year}은 돼지띠 입니다.')
#     elif h_an == 4:
#         print(f'{h_year}은 쥐띠 입니다.')
#     elif h_an == 5:
#         print(f'{h_year}은 소띠 입니다.')
#     elif h_an == 6:
#         print(f'{h_year}은 호랑이띠 입니다.')
#     elif h_an == 7:
#         print(f'{h_year}은 토끼띠 입니다.')
#     elif h_an == 8:
#         print(f'{h_year}은 용띠 입니다.')
#     elif h_an == 9:
#         print(f'{h_year}은 뱀띠 입니다.')
#     elif h_an == 10:
#         print(f'{h_year}은 말띠 입니다.')
#     else:
#         print(f'{h_year}은 양띠 입니다.')

# # 훈련과정 1개월 == 30일, 소정훈련일수의 80%이상 일때 훈련장려금 지급, 1일당 15,800원 최대 316,000원
# a = 20; b = 25; c = 30; pr_money = 15800
# cutLine = 30*0.8
# if cutLine <= a:
#     if a == 30 or a*pr_money >= 316000:
#         print(f'총 훈련 참여일수 {a}일 이고, 훈련장려금은 316,000원 입니다.')
#     else:
#         print(f'총 훈련 참여일수 {a}일 이고, 훈련장려금은 {a*pr_money:,}원 입니다.')
# else:
#     print('출석률이 저조합니다.\n분발하세요!')
# if cutLine <= b:
#     if b == 30 or b*pr_money >= 316000:
#         print(f'총 훈련 참여일수 {b}일 이고, 훈련장려금은 316,000원 입니다.')
#     else:
#         print(f'총 훈련 참여일수 {b}일 이고, 훈련장려금은 {b*pr_money:,}원 입니다.')
# else:
#     print('출석률이 저조합니다.\n분발하세요!')
# if cutLine <= c:
#     if c == 30 or c*pr_money >= 316000:
#         print(f'총 훈련 참여일수 {c}일 이고, 훈련장려금은 316,000원 입니다.')
#     else:
#         print(f'총 훈련 참여일수 {c}일 이고, 훈련장려금은 {c*pr_money:,}원 입니다.')
# else:
#     print('출석률이 저조합니다.\n분발하세요!')

# # 철도 지연 배상금 계산기 프로그램 만들기
# # 지연시간 20분 미만은 지원배상금에 포함되지 않는다
# print('철도 지연 배상금 계산기입니다.')
# t_money = int(input('승차권 구매 금액을 입력하시오: '))
# t_ch = input('환불 수단을 선택하세요 [1. 현금환불 2. 할인증] >>> ')
# t_delay = int(input('지연 시간을 입력하시오(분): '))

# if t_delay < 20:
#     print('지원배상금이 없습니다.')
# else:
#     if t_ch == '1':
#         if 20 <= t_delay < 40 :
#             print(f'지원배상금은 {round(t_money*0.125):,}원입니다.')
#         elif 40 <= t_delay <60 :
#             print(f'지원배상금은 {round(t_money*0.25):,}원입니다.')
#         else:
#             print(f'지원배상금은 {round(t_money*0.5):,}원입니다.')
#     elif t_ch == '2':
#         if 20 <= t_delay < 40 :
#             print(f'지원배상금은 {round(t_money*0.25):,}원입니다.')
#         elif 40 <= t_delay <60 :
#             print(f'지원배상금은 {round(t_money*0.5):,}원입니다.')
#         else:
#             print(f'지원배상금은 {round(t_money):,}원입니다.')
#     else:
#         print('잘못 선택했습니다.\n다시 선택하세요'

# # 사과: 3000원, 배: 2000원
# ap = int(input('사과 개수(3000원): ')); pa = int(input('배 개수(2000월): ')); h_mo = int(input('소지금액: '))
# to_fu = ap * 3000 + pa * 2000; h_co = h_mo - to_fu
# if h_co < 0:
#     print(f'구매할 수 없습니다. 추가금액 : {-h_co:,}')
# else:
#     print(f'사과: {ap}개, 배: {pa}개를 구매하고 잔돈은 {h_co:,}원 입니다.')

# # 입장료를 계산하는 프로그램을 만드시오
# h_mem = int(input('총 인원: '));
# to_mo = h_mem * 4000; h_check = 0; mo_di = 0;
# if h_mem < 0:
#     print('잘 못 입력했습니다.\n다시 입력하세요')
# else:
#     h_ch = int(input('10세 이하 어린이는 몇 명입니까? '))
#     h_check += h_ch
#     mo_di += h_ch*2000
#     h_ol = int(input('65세 이상 어르신은 몇 명입니까? '))
#     h_check += h_ol
#     mo_di += h_ol*4000
#     if h_mem < h_check or h_check < 0:
#         print('잘못 입력했습니다.\n다시 입력하세요')
#     else:
#         print(f'총 구매금액 - 할인금액 = {to_mo:,} - {mo_di:,}\n결재 금액 : {to_mo-mo_di:,}원 입니다.')

# # 시험 등급 출력
# score = int(input("시험 점수 입력:"))
# if score < 0:
#     print('잘 못 입력했습니다.')
# else:
#     if score >= 90:
#         print('A')
#     elif score >=80:
#         print('B')
#     elif score >=70:
#         print('C')
#     elif score >=60:
#         print('D')
#     else:
#         print('F')

# # 계절 출력
# month = int(input("월을 입력해주시오 :"))
# if month == 3 or month == 4 or month == 5:
#     print(f"{month}월은 봄 입니다.")
# elif month == 6 or month == 7 or month == 8:
#     print(f"{month}월은 여름 입니다.")
# elif month == 9 or month == 10 or month == 11:
#     print(f"{month}월은 가을 입니다.")
# elif month == 12 or month == 1 or month == 2:
#     print(f"{month}월은 겨울 입니다.")
# else:
#     print("잘못 입력하셨습니다.")

# # 주사위 3개
# a = int(input('주사위 눈: ')); b = int(input('주사위 눈: ')); c = int(input('주사위 눈: '))
# if 1<=a<=6 and 1<=b<=6 and 1<=c<=6:
#     if a != b and b != c and c != a:
#         if a > b and a > c:
#             print(f'{a*100}원')
#         elif b > a and b > c:
#             print(f'{b*100}원')
#         else:
#             print(f'{a*100}원')
#     elif a==b and a!=c:
#         print(f'{a*1000:,}원')
#     elif b==c and b!=a:
#         print(f'{b*1000:,}원')
#     elif c==a and c!=b:
#         print(f'{b*1000:,}원')
#     else:
#         print(f'{a*10000:,}원')
# else:
#     print('다시 입력하세요')

# # 평균을 구하고 등급을 출려하는 프로그램
# st_name = input('학생이름: '); st_kor = int(input('국어: ')); st_eng = int(input('영어: ')); st_math = int(input('수학: '))

# if st_kor<0 or st_kor>100:
#     st_kor = int(input('다시 입력하세요: '))
# elif st_eng<0 or st_eng>100:
#     st_eng = int(input('다시 입력하세요: '))
# elif st_math<0 or st_math>100:
#     st_math = int(input('다시 입력하세요: '))

# st_sum = st_kor + st_eng + st_math; st_avg = st_sum / 3; 

# if st_avg >= 90:
#     st_g = 'A'
# elif st_avg >= 80:
#     st_g = 'B'
# elif st_avg >= 70:
#     st_g = 'C'
# else:
#     st_g = 'D'

# print(f'{st_name}님의 등급은 {st_g} 입니다.')