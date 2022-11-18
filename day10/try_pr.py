import os

def checkId():
    pass

def checkFile(c,s):

    checkinfo = os.path.exists(c)

    if checkinfo != True:
        fs = open(c,'w')
        fs.write(s)
        fs.close()
        print('가입가능')
    else:
        print('이미 존재하는 회원입니다.')

def createInfo():

    try:
        a = int(input('주민번호 앞6자리 입력: '))
        s = str(a)
        try:
            if len(s) == 6:
                if a > 900101:
                    print('가입불가')
                else:
                    file_name = input('파일 이름 : ')
                    c = path+file_name+'.txt'
                    checkFile(c,s)
            else:
                raise Exception('잘못입력')
        except Exception as e:
            print(e)
    except:
        print('잘못된 숫자입력')

button = True; cho = None;
path = 'C:\\Users\\ASUS\\Desktop\\python-workspace\\day10\\info\\'

while button:

    print('1.가입 2.종료'); cho = input('>>> ')

    if cho == '1':
        createInfo()
    elif cho == '2':
        button = False
        print('종료')
    else:
        continue
