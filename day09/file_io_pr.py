import os

def infoIn():

    a = input('이름 입력: ')
    b = input('나이 입력: ')
    c = input('주소 입력: ')

    return a,b,c

def createFile():

    x = infoIn(); file_name = input('파일 이름 입력: ')
    fs = open(path+f'{file_name}.txt','w')
    for i in range(len(x)):
        if i == 2:
            fs.write(x[i])
        else:    
            fs.write(x[i]+'\n')
    print('등록 완료!')
    fs.close()

def findFile():

    co_path = path
    file_name = input('파일 이름 입력: '); print()
    co_path += file_name + '.txt'
            
    if os.path.exists(co_path):
        file = open(co_path,'r')
        print(file.read())
        file.close()
        return co_path
    else:
        print('찾고자하는 파일이 없습니다.')

def findAllFile():
    for filename in os.listdir(path):
        with open(os.path.join(path,filename),'r') as f:
            text = f.read()
            print(text,'\n')

if __name__=="__main__":

    button = True; cho = None; 

    path = 'C:\\Users\\ASUS\\Desktop\\python-workspace\\day09\\info\\'

    while button:

        os.system('cls')
        print('1.회원가입'); print('2.회원보기'); print('3.회원수정'); print('4.모든회원보기') ;print('5.종료'); cho = input('>>> ')

        if cho == '1':
            createFile()
        
        elif cho == '2': 
            findFile()
            os.system('pause')

        elif cho == '3':
            x = findFile()

            print()

            read_file = open(x,'r')

            buf = read_file.readlines()

            print('0.이름 1.나이 2.주소')
            num = int( input("수정할 번호 입력 : ") )
            value = input("수정할 값 입력 : ")

            if len(buf)-1 == num: 
                buf[num] = value
            else:
                buf[num] = value+"\n"
            
            read_file.close()

            file = open(x,'w')
            for i in buf:
                file.write(i)
            file.close()

            print('수정완료')
            os.system('pause')
        
        elif cho == '4':
            findAllFile()
            os.system('pause')

        elif cho == '5':
            button = False
            print('종료')
            os.system('pause')
        
        else:
            continue
