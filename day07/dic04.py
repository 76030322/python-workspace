import os

# st = {'학번':1234,'이름':'홍길동'}
# print(st)
# print(st.items())
# for k, v in st.items():
#     print(f'{k} : {v}')


# print(st.setdefault('학번', 5555)) # 해당하는 key값이 있으면 value값을 추가하지 않는다.
# print(st)

# print(st.setdefault('학번1', 5555)) # 해당하는 key값이 없으면 추가해준다.
# print(st)

# print('='*30)

# ls = [10,{'키':'키에의한 값'},30]
# print(ls[0])
# dic = ls[1]
# print(ls[1],ls[1]['키'],dic['키'])
# print(ls[2])

# dic = {'li':[10,20,30],'k':'value'}
# li = dic['li']
# print(dic['li'],dic['li'][0],li[1])
# print(dic['k'])

# info = {}
# info02 = {}

# info02['가수'] = '개가수'
# info02['인원수'] = 3
# info02['노래'] = '신나리'

# info[info02['가수']] = info02.copy()

# print(info02)
# print(info)

# for i, j in info.items():
#     print(f'{i} : {j}')
#     for x,y in j.items():
#         print(f'{x} : {y}')

# info02['안녕'] = '하세요'
# print('-'*50)
# print(info)
# print(info02)

# info = {}
# info.clear() # 초기화
# print(info)

button = True; cho = None; st_num = {};

while button:
    os.system('cls')    
    print('1.인적사항 등록'); print('2.검색(학번)'); print('3.수정'); print('4.삭제'); print('5.전체학생 보기'); print('6.종료'); cho = input('>>> '); 

    if cho == '1':
        stn = input('학번 입력 : ')
        if st_num.get(stn) == None:
            st_info = {'이름':None,'등급':None,'주소':None}; 
            st_num[stn] = st_info
            st_info['이름'] = input('이름 입력: ')
            st_info['등급'] = input('등급 입력: ')
            st_info['주소'] = input('주소 입력: ')
        else:
            print(f'학번 {stn}은 등록되어 있습니다.')
            os.system('pause')
            continue

    elif cho == '2':
        find_num = input('찾고자하는 학생 학번 입력: ')
        if st_num.get(find_num) != None:
            find = st_num[find_num]
            print(f'학번 : {find_num}')
            for x, y in find.items():
                print(f'{x} : {y}')
            os.system('pause')
        else:
            print('찾고자하는 학생이 없습니다.')
            os.system('pause')

    elif cho == '3':
        find_num = input('찾고자하는 학생 학번 입력: ')
        if st_num.get(find_num) != None:
            up = st_num[find_num]
            up['이름'] = input('이름 입력: ')
            up['등급'] = input('등급 입력: ')
            up['주소'] = input('주소 입력: ')
        else:
            print('찾고자하는 학생이 없습니다.')
            os.system('pause')
    
    elif cho == '4':
        find_num = input('찾고자하는 학생 학번 입력: ')
        if st_num.get(find_num) != None:        
            del st_num[find_num]
            print('삭제가 완료되었습니다.')
            os.system('pause')
            continue
        else:
            print('찾고자하는 학생이 없습니다.')
            os.system('pause')    

    elif cho == '5':
        for i, j in st_num.items():
            print(f'학번 : {i}')
            for x, y in j.items():
                print(f'{x} : {y}')
            print('='*40)
        os.system('pause')

    elif cho == '6':
        print('종료합니다.')
        button = False
        
    else:
        continue
    
