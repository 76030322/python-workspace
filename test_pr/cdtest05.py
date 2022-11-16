import os

# # 딕셔너리를 사용하여서 이름과 전화번호를 저장하자
# # 이름을 입력하지 않고 엔터키를 치면 검색모드로 변경
# # 검색모드에서 저장한 이름으로 전화번호를 검색할 수 있도록 한다.
# # 검색모드에서도 이름을 입력하지 않고 엔터키를 치면 프로그램 종료

# li = {}
# while True:
#     name = input('저장할 이름 입력: ')
#     if not name:
#         print('입력모드 종료')
#         break
#     elif li.get(name) != None:
#         print("저장된 사람입니다. 다시 입력")
#         continue
#     li[name] = input('저장할 전화번호 입력: ')

# while True:
#     name2 = input('검색할 이름 입력: ')
#     if not name2:
#         print('프로그램 종료')
#         break
#     elif li.get(name2) == None:
#         print("찾고자 하는 사람이 없습니다 다시입력")
#         continue

#     print(f'{name2}의 전화번호는 {li[name2]} 입니다.')


# # 문제 (10명의 남녀 비율(명)을 구하시오)
# # 주민등록 번호
# li = """
# 170522-4185902
# 010403-4195574
# 860122-1466919
# 900127-2351114
# 961023-1167050
# 150107-4367190
# 050403-3806690
# 140808-3906302
# 980113-1575274
# 101103-4152319
# """

# a = 0
# m,w = 0,0
# for i in range(li.count("-")):
#     a = li.find("-",a+1)
#     if int(li[a+1])%2 == 0:
#         w += 1
#     else:
#         m += 1
# print(f"남자: {m}명 여자: {w}명")

# 붕어빵가게 메뉴판을 만듭니다
# 메뉴는 맛 등록, 맛 수정, 맛 삭제, 전체 맛 보기, 종료로 구성됩니다
# 필요한 정보는 맛과 개수, 개수 대비 가격입니다
# 이중 딕셔너리를 활용하여 푸세요
# 메뉴 수정시에는 맛을 입력한 뒤, 개수와 가격만 수정 가능합니다
# 금액은 1,000 과 같이 ','를 붙여줍니다

button = True; cho = None; cara_B = {}; 

while button:
    os.system('cls')
    print(' 메뉴 '.center(60,'='));
    print('1.맛 등록'.ljust(10),end=''); print('2.맛 수정'.ljust(10),end=''); print('3.맛 삭제'.ljust(10),end=''); print('4.전체 보기'.ljust(10),end=''); print('5.종료'.ljust(10)); 
    print('='*62)
    cho = input('>>> ')

    if cho == '1':
        cara = {'개수':None, '가격':None}
        cara_t = input('맛 입력: ')
        
        if cara_B.get(cara_t) == None:
            cara_B[cara_t] = cara
            cara['개수'] = input('개수 입력: ')
            cara['가격'] = input('가격 입력: ')
            
        else:
            print(f'{cara_t}은(는) 메뉴에 있습니다.')
            os.system('pause')

    elif cho == '2':
        up_t = input('수정할 맛 입력: ')
        if cara_B.get(up_t) != None:
            up = cara_B[up_t]
            up['개수'] = input('개수 입력: ')
            up['가격'] = input('가격 입력: ')
        else:
            print('등록된 값이 없습니다.')
            os.system('pause')

    elif cho == '3':
        de = input('삭제할 맛 입력: ')
        if cara_B.get(de) != None:
            del cara_B[de]
            print(f'{de} 삭제했습니다')
            os.system('pause')
        else:
            print('등록된 값이 없습니다.')
            os.system('pause')

    elif cho == '4':
        if len(cara_B.keys()) == 0:
            print('등록된 메뉴가 없습니다.')
            os.system('pause')
        else:
            for i, j in cara_B.items():
                print(f'맛 : {i}')
                for x, y in j.items():
                    print(f'{x} : {y}')
                print('='*40)
            os.system('pause')

    elif cho == '5':
        print('종료')
        button = False

    else:
        continue