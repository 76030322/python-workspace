'''
if 조건식:
    종속문장
else:
    종속문장
다음문장
'''
'''
n = int(input('수 입력: '))
if n%2 == 0:
    print(f'{n}은(는) 짝수이다.')
else:
    print(f'{n}은(는) 홀수이다')

n1 = 10;
if n1 > 0:
    print('0보다 크다')
    if n1%2 == 0:
        print(f'{n1}은(는) 양의 짝수 입니다.')
    else:
        print(f'{n1}은(는) 음의 홀수 입니다.')
else:
    print('음수입니다.')
'''

'''
n1 = 'aaa'; n2 = 'aaa'
if n1 == n2 :
    print('같다')
else:
    print('다르다')
'''

'''
user_id = input('저장할 ID 입력: ')
user_pw = input('저장할 PW 입력: ')
print('인증 프로그램 입니다.')
print('ID와 PW를 입력하세요')
in_id = input('ID 입력: ')
in_pw = input('PW 입력: ')
if user_id == in_id and user_pw == in_pw:
    print('인증 통과 했습니다.')
else:
    if user_id == in_id:
        print('비밀번호가 같지 않습니다.')
    else:
        print('아이디가 같지 않습니다.')
'''