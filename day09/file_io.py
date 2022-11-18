import os
'''
사용모드
 - w : 파일에 내용 출력
 - r : 파일에 내용 가져오기
 - wb : 텍스트가 아닌 이미지, 동영상 등 바이너리로 처리도는 값 출력
 - rb : 읽어오기

스트림
 - 두 파일간의 통로 역할
 - close() : 스트림(연결통로)이 끊김
 - flush() : 스트림(연결통로)이 끊기지는 않으나 내부 내용이 지워짐 즉, 연결해서 사용이 가능
'''

# w: 새로운 파일에 값을 저장 만약 파일이 있으면 새로운 값으로 저장
# a: 새로운 파일에 값을 저장 만약 파일이 있으면 내용을 이어서 저장
# r: 파일에 값을 불러옴

os.system('cls')

'''
file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','w')

a = input('이름 입력 : ')
b = input('나이 입력 : ')
c = input('주소 입력 : ')

file.write(a+'\n')
file.write(b+'\n')
file.write(c+'\n')
file.close()

write_file = open('C:/Users/ASUS/Desktop/python-workspace/test1.txt','w')
read_file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','r')

# print(read_file.read())
write_file.write(read_file.read())
write_file.flush()
write_file.write('반가워~~~')
# write_file.close()
read_file.close()
'''

# read_file = open('C:/Users/ASUS/Desktop/python-workspace/abcd.txt','r',encoding='utf-8')

# print(read_file.read())

'''
read_file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','r')

st1 = read_file.readline()
st2 = read_file.readline()
st3 = read_file.readline()
st4 = read_file.readline()

print(st1); print(st2); print(st3); print(st4);
if st4 == "":
    print('더이상 데이터 없음')
'''

'''
read_file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','r')
while True:
    s = read_file.readline()
    if s == '':
        print('데이터 없음!!')
        read_file.close()
        break
    print(s,type(s))
'''

'''
read_file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','r')

s = read_file.readlines()
print(s, type(s))
read_file.close()

print()

for i in range(len(s)):
    print(f'{i} {s[i]}')

print()

for x,y in enumerate(s):
    print(x,y)
'''

read_file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','r')

buf = read_file.readlines()
for i, v in enumerate(buf):
    print(f"{i}.{v}")
num = int( input("수정할 번호 입력 : ") )
value = input("수정할 값 입력 : ")

if len(buf)-1 == num: 
    buf[num] = value
else:
    buf[num] = value+"\n"
read_file.close()

file = open('C:/Users/ASUS/Desktop/python-workspace/test.txt','w')
for i in buf:
    file.write(i)
file.close()

path = 'C:/Users/ASUS/Desktop/python-workspace/'

fileName = input('파일명 입력: ')

path += fileName + '.txt'

print('path: ',path)
print(os.path.exists(path))

if os.path.exists(path):
    file = open(path,'r')
    print('-----파일읽기-----')
    print(file.read())
    file.close()