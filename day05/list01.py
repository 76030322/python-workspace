'''
리스트
 - 여러개의 값을 저장할 경우 사용
 - 순서를 가지고 있다.
 - index는 0부터 시작한다
 - [](대괄호)으로 표현한다
'''

ls = [500,200,300,100,400]
# print(ls)
# print(ls[0]); print(ls[1]); print(ls[2]); print(ls[3]); print(ls[4])

# ls = [0,0,0,0]
# ls[0] = int(input('0. 수 입력 : '))
# ls[1] = int(input('1. 수 입력 : '))
# ls[2] = int(input('2. 수 입력 : '))
# ls[3] = int(input('3. 수 입력 : '))

# l_sum = ls[0] + ls[1] + ls[2] + ls[3]
# print('sum : ',l_sum )

# ls = [0,0,0,0]; lsum = 0; print('len: ', len(ls))
# for i in range(len(ls)):
#     ls[i] = int(input(f'{i}. 수 입력 : '))
#     lsum += ls[i]

# print(f'sum: {lsum}')

print('='*30)

for i in range((len(ls))):
    print(f'ls[{i}] : {ls[i]}')

for i in 'abcd':
    print (i)