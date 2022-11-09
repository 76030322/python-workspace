import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))) # 파일간의 경로 설정

# import day02.elif05
# print('현재페이지')
'''
data = 0; data = None; # 초기화 방법
while True:
    print('='*30)
    print('1.데이터 입력'); print('2.데이터 출력'); print('3.종료')
    print('='*30)
    num = input('>>> ')

    if num == '1':
        data = input('데이터 입력 >> ')
    elif num == '2':
        if data == None:
            print('저장 데이터 없음')
        else:
            print(f'입력 데이터 : {data}')
    elif num == '3':
        print('종료합니다')
        os._exit(1)
    else:
        print('다시 입력하세요')
        continue

    os.system('pause')
    os.system('cls')
'''
st_name = None; st_kor = 0; st_eng = 0; st_math = 0; st_sum = None; st_avg = None;
while True:
    print('='*30)
    print('1. 학생 이름 입력\n2. 성적 3과목(국,영수) 입력\n3. 학생 이름 출력\n4. 합계 출력\n5. 평균 출력\n6. 종료')
    print('='*30)
    cho_nu = input('>>>> ')
    
    if cho_nu == '1':
        st_name = input('학생 이름 : ')
    elif cho_nu == '2':
        st_kor = int(input('국어: '))
        st_eng = int(input('영어: '))
        st_math = int(input('수학: '))
        st_sum = st_kor + st_eng + st_math; st_avg = st_sum / 3
    elif cho_nu == '3':
        if st_name == None:
            print('학생 이름을 입력해주세요!')
        else:
            print(f'학생 이름: {st_name}')
    elif cho_nu == '4':
        if st_sum == None:
            print('3과목 점수를 먼저 입력해 주세요')
        else:
            print(f'합계 출력: {st_sum}')
    elif cho_nu == '5':
        if st_avg == None:
            print('3과목 점수를 먼저 입력해 주세요')
        else:
            print(f'평균 출력: {round(st_avg,2)}')
    elif cho_nu == '6':
        print('종료합니다')
        os._exit(1)
    else:
        print('잘못입력했습니다.')
        os.system('pause')
        os.system('cls')
        continue
    os.system('pause')
    os.system('cls')
    