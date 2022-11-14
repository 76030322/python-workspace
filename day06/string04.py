st = "Have a nice day"

print(st); print(st[0]); print(st[1]); print(st[-1]); print(len(st))

for i in st:
    print(i, end='\t')
print()

print(st[3:6])
print('='*50)

st = "Python test. 그리고 programming 할만하다 ^^"
print(st)
print(st.upper()) # 대문자로 변경
print(st.lower()) # 소문자로 변경
print(st.swapcase()) # 상호변경. 대/소문자
print(st.title()) # 단어의 첫번째 대문자로 변경
print(f'st : {st}')

# 대문자는 소문자로, 특수문자, 숫자, 공백 다음의 첫 글자는 대문자로 변환 하시오
st = 'NevEr -eVer 110glVe up'
st = st.title() # 영구적용
print(st)
print('='*50)

st = 'Have a nice day'
print(st)
print(st.count('a'))
print(st.count('day'))
print(st.count('dak'))

print(st.startswith('Ha')) # 시작문자
print(st.startswith('ha')) 
print(st.endswith('day')) # 끝문자
print(st.endswith('da'))

st = 'It is a fun Python class'
print(f'{st.count("a")}\t{len(st)}')
print('='*50)

st = "Have a nice day"
print(st)
print(st.find('day'))
print(st.index('day'))
print(st.find('dddd'))
# print(st.index('dddd')) # 해당하는 문자가 없을시 에러가 발생

print(st.find('a')) # 제일 처음에 만나는 index값
print(st.find('a',2)) # index 2 이후로 'a'를 찾아달라
print(st.find('a',6))
print(st.find('a',14))

num = st.find('a')
print(st.find('a'))
print(st.find('a',num+1))

num = st.find('a', num+1)
print(st.find('a',num+1))
print(st.find('a',14))
print('='*50)

# a의 총 개수와 index의 위치를 list에 저장 후 출력 하시오.
st = 'Have a nice day Have a nice day Have a nice day'
cnt = 0
ls = []
while True:
    cnt = st.find('a' , cnt )
    if cnt != -1:
        ls.append( cnt )
        cnt += 1
    else:
        break
print('a 개수 : ' , st.count('a') )
print('index : ' , ls )

# 다음 문자열에서 대, 소문자 구분없이 ab로 시작하는 문자열과 test로 끝나는 문자열들을 출력하시오
li = ['AbCe test123','acd efg','a123 TEST 123','123 TEst']
for i in li:
    lo = i.lower()
    if lo.startswith('ab') or lo.endswith('test'):
        print(i)
print('='*50)

st = '  파이썬  '
print(f'*{st}*')
print(f'*{st.strip()}*')

# name = input('이름 입력 : ')
# print('이름 : ', name)
# if name.strip() == '홍길동':
#     print('인증통과')
# else:
#     print('인증실패!!')

st = "+++파 이 썬+++"
print(st)
print(st.strip("+"))
print(st.rstrip("+"))
print(st.lstrip("+"))
print('='*50)

st = "2015/04/02"
print(st)
print(st.replace("/","-"))
print(st.replace(st[:4],"2022"))
print("="*50)

st = """
aaaa
bbbb
cccc
dddd
eeee
"""
print(st)
print('='*50)

st = """
김개똥 -2017년 03월 24일
홍길동구리 -2015년 04월 02일
선우선녀 -2018년 05월14일
"""
st = st.replace('-' , ':' )
i = 0
for k in range( st.count(':') ):
    i = st.find(':' , i+1 )
    print('i' , i )
    st = st.replace( st[i+1:i+5] , "1999" )
print('st:' , st )