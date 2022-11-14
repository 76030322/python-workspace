'''
set
 - 중복된 데이터를 허용하지 않음
 - 처리 속도가 빠름
 - 순서를 유지하지 않는다
 
사용방법
 - set(데이터)
 - {값, 값, ..., 값 }
'''

s = {'안녕하세요'}
print(s)
print(type(s))

s = set([1,1,1,1,2,2,3,4,5,6,7,7,7,8,8,9,9,9,9])
print(s)
# print(s[0]) # 인덱스(Index)가 없으므로 인덱스로 접근할 수 없다. 따라서 list로 형변환 해서 사용하면 된다.

ls = [1,1,1,1,2,3,3,4,4,5,6,7,7,7,8,8,8,8,9,9,10,10]
s = set(ls)
li = list(s)
print(li)
print(li[0])

s = {1,2,3}
print(f'변경전 : {s}')

s.add(4)
print(f'add(4) : {s}')

s.update([5,6,7])
print(f'update[5,6,7] : {s}')

s.remove(7)
print(f'remove(7) : {s}')

# issuperset : set내부의 값의 존재 여부로 True / False로 구분해줌
print('issuperset : ', s.issuperset({1,2}))
print('issuperset : ', s.issuperset({11}))

s.pop()
print(s)