'''
num1 = int(input('수를 입력하세요: '))
print(f'입력값: {num1}',type(num1))

name1 = input('이름 입력: ')
age1 = int(input('나이 입력: '))
print(f'결과출력 : {name1} 님의 나이는 {age1} 살 입니다.')

print('='*20)
print('두 수의 합을 구해줍니다')
n1 = input('수 입력: ')
n2 = input('수 입력: ')
s = int(n1) + int(n2)
print(f"두 수의 합 {n1} + {n2} = {s}")
'''
'''
# 올해 년도와 태어난 년도를 구하여 나이를 계산하는 프로그램을 코딩
ny = int(input('올해의 년도를 4자리로 입력하세요: '))
by = int(input('당신이 태어난 년도를 4자리로 입력하세요: '))
yAge = ny - by + 1
print(f'당신의 나이는 {yAge}입니다.')

# 600kg제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로 입력받아ㅏ 현재 엘리베이터에 더 적재할 수 있는 무게를 구하시오
we1 = float(input('첫 번째 물건의 무게를 입력 하시오: '))
we2 = float(input('두 번째 물건의 무게를 입력 하시오: '))
ele = 600 - (we1 + we2)
print(f'현재 엘리베이터에 허용 무게는 {ele}kg 입니다.')

# 표준체중과 비만도 비율을 구하시오
nKey = float(input("키를 입력하세요: "))
nWei = float(input('몸무게를 입력하세요: '))
dw = (nKey-100) * 0.9
oDw = (nWei/dw)*100
print(f'표준체중은 {dw}이고 비만도는 {round(oDw,2)}입니다.')
'''

# 학생 이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오
st_name = input('학생이름: '); kor = input('국어 점수: '); eng = input('영어 점수: '); math = input('수학 점수: ');
st_sum = float(kor) + float(eng) + float(math)
st_avg = st_sum / 3
print('='*17,'학생 정보','='*17)
print('이름\t국어\t영어\t수학\t합계\t평균')
print('-'*45)
print(f'{st_name}\t{kor}\t{eng}\t{math}\t{st_sum}\t{round(st_avg,2)}')