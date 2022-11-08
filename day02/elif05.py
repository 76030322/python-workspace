'''
if 조건식 :
    종속문장
elif 조건식:
    종속문장
    …
elif 조건식:
    종속문장
else:
    종속문장
다음문장
'''

num = int(input('수 입력: '))
if num > 100:
    print('100보다 크다')
elif num > 90:
    print('90보다 크다')
elif num > 80:
    print('80보다 크다')
elif num > 70:
    print('70보다 크다')
else:
    print('그 외의 값')
print('다음 문장들 실행!!!!')