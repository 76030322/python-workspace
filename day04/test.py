'''
f5 : 디버깅 실행 모드
f9 : 브레이크 포인트
f11 : 한줄씩 실행
f10 : 한줄씩 실행
shiift + f5 : 디버깅 종료


'''

sum = 0
for i in range(100000):
    sum += i
print(sum)
print(sum)
print(sum)
print(sum)

for i in range(5):
    print('실행')
    for k in range(3):
        print('종속')
    print('끝')