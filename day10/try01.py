import os

# 예외처리
'''
try:
    n1 = int(input('수 입력: '))
    n2 = int(input('수 입력: '))

    s = n1/n2
    print('결과: ',s)
except ZeroDivisionError:
    print('문제발생')
except ValueError:
    print('문제발생')
print('다음 문장')
'''

'''
while True:
    try:
        num = int(input("수 입력(종료 0) : "))
    except:
        num = '잘 못 입력. 다시...'
    if num == 0:
        break
    print('입력 한 수: ',num)

print('다음 문장들 실행')
'''

'''
try:
    n1 = int(input('수 입력 : '))
    n2 = int(input('수 입력 : '))
    s = n1/n2
except:
    print('except 실행')
else:
    print(f'{n1} / {n2} = {s}')
print('다음 문장 실행!!!')
'''

'''
try:
    n1 = int(input('수 입력 : '))
    n2 = int(input('수 입력 : '))
    s = n1/n2
except:
    print('except 실행')
else:
    print(f'{n1} / {n2} = {s}')
finally:
    print('finally 실행~~~')
print('다음 문장 실행')
'''

'''
def test():
    file = None
    try:
        file = open("C:/aaa111.txt",'r')
    except:
        print('파일이 존재하지 않습니다.')
    else:
        print(file.read())
    finally:
        if file:
            file.close()
    print('이어서 진행')
    
    try:
        n = input("수 입력: ")
        if n == '1':
            return 111
        elif n == '2':
            return 222
    except:
        pass
    finally:
        print('test 함수 실행')
        print('이 코드는 무조건 실행 되어야 한다') # finally에 넣어 무조건 처리할 수 있게 해준다. return 또는 오류발생시에도 무조건 실행시켜줄 수 있다.
    print('test 함수 종료')
re = test()
print('결과 : ',re)
'''

try:
    age = int(input('나이 입력: '))
    # print('당신의 나이는 : ',age-1)
    if age < 0:
        raise Exception('00000 안됨') # 강제로 예외를 발생시키는 문법
except ValueError:
    print('문자는 입력할 수 없음')
except Exception as e:
    print('0살 아래 안됨!!')
    print(e)
except:
    print('문제 발생!!!')
else:
    print('당신의 나이는 : ',age)

while True:
    try:
       age = int(input('입력 : '))
       st = str(age)
       if age >= 900101 or len(st) != 6:
           print('가입 불가')
       elif age <= 891231:
           print('가입 가능')
           break
    except:
        print('잘못 입력')

while True:
    try:
        min=input("주민번호 앞 자리 입력(예 900402) : ")
        if len(min) != 6:
            raise Exception("잘못 입력")
        if not min.isdigit(): #숫자로 구성되어 있냐
            raise Exception("잘못 입력 숫자 입력하세요")
        elif min[0] > '8':
            raise Exception(min)
    except Exception as e:
        print(e,"가입불가")
    else:
        print(min,":가입가능")
    finally:
        print("프로그램 종료 합니다")