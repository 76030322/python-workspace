'''
반복문
 - 어떤 내용을 반복하고자 하는 경우
 - 규칙적으로 값이 변경 된다면 사용가능
 
    for 변수 range(초기값, 비교값, 증가값):
        종속문장
'''
num = 0; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)
num += 1; print(num)

print('='*20)

for i in range(0,11):
    print(i)
print('다음 문장 실행')

for i in range(1,11):
    print('for 시작')
    if i%2 == 0:
        print('i = ', i)
    print('for 끝')
print('다음 문장 실행')

for i in range(1, 11, 2):
    print(i)

print('안녕',end=""); print('하'); print('세요')

for i in range(1,11):
    print(i,end=" ")
print()

sum = 0;
for i in range(1,11):
    sum += i    
print(sum)

for i in range(1,31):
    print(i,end='\t')
    if i % 5 == 0:
        print()

sum_d = 0; sum_o = 0;
for i in range(1,11):
    if i % 2== 0:
        sum_d += i
    else:
        sum_o += i
print(f'짝수의 합: {sum_d}\n홀수의 합: {sum_o}')

print('='*10)

for i in range(0,10):
    print(i,end=', ')
print()

for i in range(10):
    print(i,end=', ')
print()

# 두 수를 입력 받은 두 수의 범위 안의 합을 구하시오
n1 = int(input('수 입력: ')); n2 = int(input('수 입력: '))
n_sum = 0
if n1 == n2 :
    print(f'두 수의 범위 안의 합: {n1}입니다.')
else:
    if n1 > n2 :
        max_n = n1; min_n = n2
    else:
        max_n =n2; min_n =n1
    for i in range(min_n,max_n+1):
        n_sum += i
    print(f'{n1}입력, {n2}입력 >> {n_sum}')

st = "Hello Python"
for i in st:
    print(i,end=",")

st = "It is a fun Python class"
ct = 0; a_c = 0; s_c = 0;
for i in st:
    ct += 1
    if i == 'a':
        a_c += 1
    elif i == 's':
        s_c += 1
print(f'===결과===\n총 개수: {ct}\na 개수: {a_c}\ns 개수: {s_c}') 
