import os
'''
while 조건식:
    종속문장
'''
i = 0
while i<5:
    print(i,'.종속문장')
    i+=1
print('다음문장')

# for 문으로 변경 ▽

for i in range(5):
    print(i,'종속문장')
print('다음문장\n')

i = 1; odd,even =0,0
while i <= 10:
    if i%2 == 0:
        even += i
    else:
        odd += i
    i+=1
print(f'짝수의 합: {even}\n홀수의 합: {odd}\n')

# for문으로 변경 ▽

odd,even = 0,0;
for i in range(11):
    if i % 2 == 0:
        even += i
    else:
        odd += i
print(f'짝수의 합: {even}\n홀수의 합: {odd}\n')

i = 1; flag =True
while flag:
    print(i,'종속문장',end=' ')
    if i ==5:
        flag = False
        print()
    i += 1
print('다음문장실행')

'''
break : 반복문을 빠져나올 경우 사용
continue : 반복문 위로 올려보낸다
'''

i = 0
while i < 5:
    i += 1
    if i == 3:
        # break
        print('33333')
    print(f'{i} 출력')
print('다음문장 출력')

i = 0
while i < 5:
    i += 1
    if i == 3:
        # continue
        print('33333')
    print(f'{i} 출력')
print('다음문장 출력')

i = 0
while i < 5:
    i += 1
    print(i,'종속문장')
    if i == 2:
        break
else:
    print('else 실행')
print('다음문장')

# po = 1; n = None;
# while po:
#     os.system('cls')
#     n = input('10~20사이의 숫자 입력 : ')
#     inN = int(n); nSum = 0;
#     if 10 <= inN <= 20:
#         for i in range(1,inN+1):
#             nSum += i
#         print(f'\n1 에서 {n}까지의 합: {nSum}\n')
#         os.system('pause')
#     else:        
#         continue

for i in range(3):
    for k in range(5):
        if k ==3:
            break
        print(f'i: {i}, k: {k}')

print(); print()

i = 0
while i < 3:
    k = 0
    while k < 5:
        if k == 3:
            break
        print(f'i : {i}, k : {k}')
        k += 1
    i+=1

os.system('cls')

cho = 1; cl = 0;
money = int(input('요금을 투입하세요: '))

while cho:
    print('{:=^50}'.format('커피 자판기'))
    print('1.커피(200)\t2.코코아(250)\t3.반환\t4.종료',end='\n')
    cl = input('메뉴 선택 >>> ')
    if cl == '1':
        if money < 200:
            print('구매할 수 없습니다.')
            continue
        money -= 200
        print('커피맛있게 드세요')

    elif cl == '2':
        if money < 2500:
            print('구매할 수 없습니다.')
            continue
        money -= 250
        print('코코아 맛있게 드세요')
    elif cl == '3':
        print(f'잔돈 {money}가 반환 되었습니다.')
        money -= money
    elif cl == '4':
        print(f'잔돈 {money}가 반환 되었습니다.')
        cho = 0
    else:
        print('다시 입력하세요: ')
        os.system('pause')
        continue
