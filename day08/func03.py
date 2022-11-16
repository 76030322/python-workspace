def showAvg(a,b,c):
    print(f'{a}와 {b}의 평균 : {round(c,1)}')

def avrg(j,k):
    return (j+k)/2

def display():
    i =2; j=3;
    f = avrg(i,j)
    showAvg(i,j,f)

display()

print('다음문장실행')


def resultPrint():
        print('입력한 값은 존재합니다. 저장할 수 없음')

def checkList(a,chli):
    check = 0;
    for i in chli:
        if a == i: check = 1; break
    if check == 1:
        resultPrint()
    else:
        chli.append(a); print(a,'저장 되었습니다!!!')

year = [ '1999' , '2000' , '2001' ]
num = input('저장할 년도 입력 : ' )
a = checkList(num,year)
print(year)

menu = [ '라면' , '순대' , '김밥' ]
num = input('등록 메뉴 입력 : ' )
a = checkList(num,menu)
print(menu)