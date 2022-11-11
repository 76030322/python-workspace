# ls = list()

# for i in range(3):
#     value = input(f'{i+1}번째 입력: ')
#     ls.append(value)
# print('총 개수 : ', len(ls))
# print('type : ', type(ls))
# print('ls : ', ls)

# ls = []
# print('초기화 후 ls : ', ls)

print('='*45)

ls = [30,10,20,40]
print('ls : ', ls)

ls.pop()
print('pop : ', ls)

ls.reverse()
print('reverse : ', ls)

ls.sort()
print('sort : ', ls)

print('='*45)

ls = [10,50,70,30,20]
arr = ls[:]; arr.reverse()
# arr = ls1.copy(); arr.reverse()
sort_arr = sorted(ls)
reverse_arr = sort_arr[:]; reverse_arr.reverse()
# reverse_arr = sort_arr.copy() ; reverse_arr.reverse()
print(f'arr : {arr}')
print(f'sort_arr : {sort_arr}')
print(f'reverse_arr : {reverse_arr}')

print('='*45)

ls = [10,20,30]
print('ls : ', ls)
del(ls[1])
print('del(ls.1 : ', ls)
ls.remove(30)
print('remove(30) : ', ls)

print('='*45)

ls = [30,20,10]
print(ls)
i = ls.index(20)
print('index(20) : ', i)
# i = ls.index(40)

ls.append(100)
print('append(100) : ', ls)

ls.insert(2,500)
print('insert(2,500) : ', ls)

arr = [1,2,3,1]
# ls = ls + arr
ls.extend(arr)
print(ls)

cnt = ls.count(1)
print('count(1) : ', cnt)
cnt = ls.count(60)
print('count(60) : ', cnt)

