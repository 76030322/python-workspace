# ls = [10,20,30,40,50]

# print(ls)
# print('='*10)
# print(ls[0:3])
# print(ls[2:])
# print(ls[:2])

# # arr = ls # 얕은 복사
# # arr = ls[:] # 깊은 복사
# # arr = ls.copy() # 깊은 복사
# import copy
# arr = copy.deepcopy(ls)
# arr[0] = '안녕'
# print(ls,':',id(ls))
# print(arr,':',id(arr))

# print('-'*10)
# ls = [10,20,30]
# arr = [40,50,60]
# print(ls)
# print(arr)

# arr02 = ls + arr
# print(arr02)

# arr03 = ls*3
# print(arr03)

# str = [0,0,0]; string=[0,0,0]
# for i in range(len(str)):
#     str[i] = ls[i] + arr[i]
# print(f'ls + arr => Str : {str}')

# for i in range(len(str)):
#     string[i] = ls[i]*3
# print(f'ls * 3 => string : {string}')

ls = [10,5,20,7,9,31,12,11,19,32]

evenSum = [0,0,0,0,0]; oddSum = [0,0,0,0,0]; result = [0,0,0,0,0]; a,b = 0,0; evSum,odSum = 0,0

for i in range(len(ls)):
    if i % 2 == 0:
        evenSum[a] = ls[i]
        a+=1
    else:
        oddSum[b] = ls[i]
        b+=1

for i in range(len(result)):
    result[i] = evenSum[i] - oddSum[i]
print(result)

for i in range(len(evenSum)):
    evSum += evenSum[i]
    odSum += oddSum[i]
print(evSum - odSum)

invertList = [0,0,0,0,0,0,0,0,0,0]; j = len(ls)
for i in ls:
    j -= 1
    invertList[j] = i
print(invertList)

score = [82,85,76,79,96]; grade = [0,0,0,0,0]; gr = 0; gind = 0

for i in score:
    gr = 1
    for j in score:
        if i < j :
            gr += 1
    grade[gind] = gr
    gind += 1

for i in range(5):
    print(f'score : {score[i]} | grade : {grade[i]}')


