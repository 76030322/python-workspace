'''
lambda >> 함수를 축약시켜 놓은 함수
'''


# def func01(*par):
#     print(type(par))
#     for i in par:
#         print(i)
# func01(10,20,30,40)

# def big (a,b):
#     if a>b:
#         return a
#     else:
#         return b
# result = big(10,20)
# print(result)

# bi = lambda a,b : a if (a>b) else b
# result = bi(200,1000)
# print(result)

# bi = lambda a : a + 1000
# print(bi(100))

# li = ['100','200','300']
# li = list(map(int,li))
# for i in range(len(li)):
#     li[i] = str(li[i]+10)
# print(li)

# def test1(a):
#     return str(int(a)+10)

# li = ['100','200','300']
# li = list(map(test1, li))
# print('함수 : ', li)

# li = ['100','200','300']
# lb = lambda x : str(int(x)+100)
# li = list(map(lb,li))
# # li = list(map(lambda x : str(int(x)+100),li))
# print('lambda: ',li)

# day = {'날짜':['2018.01.01','2019.02.02','2020.03.03']}

# for x,y in day.items():
#     for i in y:
#         v = i.split('.')
#         print(f'for : {v[0]}년 {v[1]}월 {v[2]}일')

# ls = list(map(lambda x : x.split('.'), day['날짜']))
# for i in ls:
#     print(f'lambda : {i[0]}년 {i[1]}월 {i[2]}일')

a = lambda x : print(x,'입니다')
a(1234)