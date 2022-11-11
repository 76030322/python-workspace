# ls = [[값],[값],[값]]

print('='*50)
ls = [[1,[2,100,200],3,4],[5,6,7,8],[9,10,11,12]]
print(ls[0])
print(ls[0][1])
print(ls[0][1][2])

print('='*50)
ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
for i in ls:
    for j in i:
        print(f'{j}',end="\t")
    print()

print('='*40)
ls = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# arr = ls[0] # 얕은  복사
# arr = ls[0][:]
arr = ls[0].copy()
arr[1] = 1000
print(ls)
print(arr)

print('='*50)
ls_1 = []; ls_2= []; value = 1

for i in range(3):
    for j in range(4):
        ls_1.append(value)
        value += 1
    ls_2.append(ls_1)
    ls_1 = []

for i in ls_2:
    for j in i:
        print(f'{j}',end='\t')
    print()

print(ls_2)

print('='*50)
ls_1 = []; ls_2= []; value = 1

for i in range(12):
    ls_1.append(value)
    if value%4 == 0:
        ls_2.append(ls_1)
        ls_1 = []
    value += 1

for i in ls_2:
    for j in i:
        print(f'{j}',end='\t')
    print()

print(ls_2)

print('='*50)
ls = [10,20,30]
s = ls[0] * 100
print(s)

ls = ['10','20','30']
print('변환전 : ', ls)
s = list(map(int, ls))
print('변환후 : ', s)