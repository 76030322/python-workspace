for i in range(3):
    print('상위 for문 실행')
    for k in range(5):
        print(f'이중 for 문 (i:{i}, k:{k})')
    print('종료 상위 for문')

# 구구단 (가로)
for i in range(2,10):
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}',end='\t')
    print()

print('='*160)

# 구구단(세로)
for i in range(1,10):
    for j in range(2,10):
        print(f'{j} X {i} = {j*i}',end='\t')
    print()

for i in range(5):
    print(f'상위포문 {i}일때 하위 포문 :',end=' ')
    for j in range(5):
        print(f'{i*j}',end=' ')
    print()

print(); print(); print()

for i in range(1,26,5):
    for j in range(5):
        print(f'{i+j}',end='\t')
    print()