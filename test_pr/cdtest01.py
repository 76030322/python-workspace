# A, B, C에 각각 수를 입력 후 최대값과 최소값을 구하고 A * B * C가 3의 배수이면서 짝수일때는 최대값을 출력 3의 배수이면서 홀수일대는 최소값을 출력하시오.
# 단, A, B, C는 정수만 입력이 가능하고 A * B * C의 값이 양수일때만 출력

a = int(input('A값 입력: ')); b = int(input('B값 입력: ')); c = int(input('C값 입력: '))
max_n, min_n = 0, 0; total = a*b*c
if a >= b and a >= c:
    if b >= c:
        min_n = c
    elif c >= b:
        min_n = b
    max_n = a
elif b >= a and b >= c :
    if a >= c:
        min_n = c
    elif c >= a:
        min_n = a
    max_n = b
else:
    if a >= b:
        min_n = b
    elif b >= a:
        min_n = a
    max_n = c
if total > 0 and total != 0:
    if total%2 == 0 and total%3  == 0:
        print(f'최대값: {max_n}')
    elif total%2 != 0 and total%3 == 0:
        print(f'최소값: {min_n}')
    else:
        print('출력 실패')
else:
    print('출력 실패')


# 생년월일을 정수로 8자리 입력받고 년, 월 일을 나눠서 출력하시오
birth = int(input('생년월일 8자리를 입력하세요: '))
year = birth//10000; month = (birth%10000)//100; day=(birth%10000)%100
print(f'{year}년 {month}월 {day}일')

# 윤년을 여부를 출력하시오
# 윤년의 조건은 4의 배수이면서 100의 배수가 아닐때 또는 400의 배수일때이다.
year = int(input('년도를 입력하세요: '))
if year % 400 == 0:
    print(f'{year}은(는)윤년이다')
elif year%4 == 0 and year % 100 !=0:
    print(f'{year}은(는)윤년이다')
else:
    print(f'{year}은(는) 윤년이 아니다')

# 알람 45분 일찍 설정하기 단, 시간은 24를 초과할 수 없고, 분은 60을 초과할 수 없다.
c_hour = int(input('시간: ')); c_min = int(input('분: '))
if 0 <= c_hour <= 23 and 0 <= c_min <= 59:
    c_min -= 45
    if c_min < 0:
        c_hour -= 1
        if c_hour < 0:
            print(f'알람시간은 23시 {c_min+60}분 입니다.')
        else:
            print(f'알람시간은 {c_hour}시 {c_min+60}분 입니다')
    else:
        print(f'알람시간은 {c_hour}시 {c_min}분 입니다.')
else:
    print('잘못 입력했습니다.')