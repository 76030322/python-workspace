st = 'Never ever give up'
print(st)
print(st.split())

st = '안녕하세요 오늘 2300/5/14 날씨는 error 춥다'
st = st.split()
print(st)
del(st[4]); del(st[2])
print(st)
st.insert(2,'2300년5월14')
print(st)
for i in st:
    print(i,end=' ')
print('='*50)

st = '안녕하세요 반갑습니다'
print(st)
print(st.splitlines())

st = '''
안녕하세요
안녕하세요
안녕하세요
'''
print(st.splitlines())
print(st.split('\n'))
print('='*50)

st = '123'
test = '%'
print(test.join(st))
print('$'.join(st))

print(st.join("안녕하세요"))

li = ["","123","456"]
print("그래".join(li))

print('='*10)
st = 'python'
print(st)
print(st.center(10))
print(st.center(10,'-'))

print(st.ljust(10))
print(st.ljust(10,'-'))
print(st.rjust(10))
print(st.rjust(10,'-'))
print('='*50)

accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
acB = accountBook.split(',')
nAcb = []
for i in range(len(acB)):
    acB[i]=acB[i].split()
    for j in acB[i]:
        nAcb.append(j)

print(nAcb)
print(len(nAcb))

print('='*30)
print('item'.ljust(10),end='')
print('date'.ljust(10),end='')
print('$(price)'.ljust(10))
print('='*30)
for i in range(1,len(nAcb)+1):
    if i % 3 == 0:
        print(f'${int(nAcb[i-1]):,}'.ljust(10))
    else:
        print(f'{nAcb[i-1]}'.ljust(10),end='')
    
print('='*50)

st = 'pythonte12st1234'
print(st.isdigit()) # 숫자로만 구성
print(st[9:11].isdigit())

print(st.isalpha()) # 알파벳으로만 구성
print(st[:6].isalpha())

print(st.isalnum()) # 알파벳 + 숫자로만 구성
print(st[7:13].isalnum())

print(st.islower()) # 알파벳이 전부 소문자

st = st.upper()
print(st.isupper()) # 알파벳이 전부 대문자

st = ' '
print(st.isspace()) # 공백으로만 이루어져 있는지 확인

info = """
jo 9abc08-3022023
cho 900402-1011232
test 1234567-1234567 
lee 980908-3a2b0c3
kim 900514-2022023
"""

info = info.splitlines()
del(info[0])
for i in info:
    x = i.split()
    y = x[1].split('-')
    if len(y[0]) == 6 and len(y[1]) == 7:
        if y[0].isnumeric() and y[1].isnumeric():
            y[1] = '*'*7
    print(f'{x[0]}\t{y[0]}-{y[1]}')

info = """
jo 9abc08-3022023
cho 900402-1011232
test 1234567-1234567 
lee 980908-3a2b0c3
kim 900514-2022023
"""

info = info.split()

for i in range(len(info)):

    if i % 2 == 0:
        print(f'{info[i].ljust(5)}',end='')

    else:
        x = info[i].split('-')
        if x[0].isnumeric() and x[1].isnumeric():
            if len(x[0]) == 6 and len(x[1]) == 7:
                x[1] = '*'*7
        print(f'{x[0]}-{x[1]}')