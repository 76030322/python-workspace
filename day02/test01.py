flt =123.123
print(flt + 100)

st1, st2 = '파', '이썬'
print(st1+st2)

# print(st1+flt)

print('100', 100) # 둘다 출력값이 100 이지만 type값이 다르므로 나중에 오류가 발생 할 수 있다.

a, b, c = '100', 100, 100.1
print(type(a)) # str = 문자형
print(type(b)) # int = 정수형
print(type(c)) # float = 실수형
print()

# 형변환 >> type casting
print(int(a)+b)
print(b+c)
print(int(a)+c)
print(float(a)+c)
print()

su = 100; num = '100'; flt='1.111'
print(su+int(num))
print(su+float(flt))
print(str(su)+num)
print()

print(type(flt),flt)
# print(int(flt)) # 에러 발생
print(int(float(flt))) # 문자열모양이 실수이므로 실수로 먼저 변환 후 그 후에 정수형으로 변환이 가능하다.
print(su, float(su))
print(num, float(num))