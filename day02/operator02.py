'''
    // : 몫을 구해준다
    % : 나머지를 구해준다
    ** : 승수를 의미한다

'''

n1 = 9; n2 =2

print(f'{n1} + {n2} = {n1+n2}')
print(f'{n1} * {n2} = {n1*n2}')
print(f'{n1} / {n2} = {n1/n2}')
print(f'{n1} // {n2} = {n1//n2}')
print(f'{n1} % {n2} = {n1%n2}')
print(f'{n1} ** {n2} = {n1**n2}')

'''
관계 연산자
    >, <, <=, >=, ==
    - 결과적으로 참(True)인지 거짓(False)인지 판단
    - 이항 연산자
'''

n1 =3.1; n2 =3;
print('n1 >= n2 : ',(n1>=n2))
print('n1 < n2 : ',(n1<n2))
print('n1 == n2 : ',(n1==n2))
print('n1 != n2 : ',(n1!=n2))

'''
    num = 10;
    num += 100; == num = num + 100;
'''

n1 = n2 = 5;
n1 += 1; print(n1)
n1 -= 1; print(n1)
n1 *= n2; print(n1)
n1 //= n2; print(n1)
n1 %= n2; print(n1)

n1 = 5; n2 = 3;
n1 **= n2
n1 -= 2
print(n1/4)
print(n1//4)
print(n1%4)

'''
 논리연산자
 - 여러개의 식을 묶어서 연산한다
    num = 10
    * and : 모두가 참일때 결과는 참, 하나라도 거짓이면 결과는 거짓
        (num>10) and (num%2 == 0)
    * or : 하나라도 참이면 결과는 참
        (num>10) or (num%2 == 0)
    * not : 결과를 반전 시켜준다
'''

print( True and True)
print( False and True)
print( True and False)
print( False and False)

n1 = 12
print('n1 > 10 : ',n1>10)
print('n1 % 2 : ',n1%2)
print('0 == 0 : ', 0 == 0)

print(n1>10 and n1%2 == 0)

print( True or True)
print( False or True)
print( True or False)
print( False or False)

print('not True : ', not True)
print('n1 > 10 : ', n1>10)
print('not n1 > 10 : ', not n1>10)
