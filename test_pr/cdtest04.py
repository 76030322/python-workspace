import os,random

# # Updown 게임 만들기
# # 1-99 사이의 랜덤한 숫자를 프로그램이 가지게 되며, 해당 범위의 값을 맞추는 게임이다
# # 단, 숫자 입력시 범위값(1~99)을 벗어나거나 음수를 입력시 다시 입력하게 해주고 Count는 1씩 증가한다.
# ch = None; record = list(); 
# while True:
#     os.system('cls')
#     print('UpDown 게임')
#     print('1.게임시작 2.최고기록 확인 3.종료', end=' ')
#     ch = input('>>> ')
#     rn = random.randrange(1,100); # print(rn) # 확인용
#     if ch == '1':
#         cho = 1; cnt = 0; 
#         while cho:
#             cnt += 1
#             pn = int(input('수 입력: '))
#             if pn <= 0 or pn >= 100:
#                 print('잘못입력했습니다')
#                 continue
#             else:
#                 if pn == rn:
#                     print('정답입니다!')
#                     if len(record) == 0:
#                         print(f'{cnt}회 최고기록')
#                         record.append(cnt)
#                     else:
#                         record.sort()
#                         if cnt < record[0]:
#                             print(f'{cnt}, 최고기록 갱신')
#                         record.append(cnt)
#                     os.system('pause')
#                     cho = 0
#                 elif pn < rn:
#                     print('up')
#                 else:
#                     print('down')
#     elif ch == '2':
#         if len(record) == 0:
#             print('등록된 기록이 없습니다.')
#             os.system('pause')
#             continue
#         s_r = set(record)
#         record = sorted(s_r)
#         print(f'최고기록 {record[0]}')
#         os.system('pause')
#         continue
#     elif ch == '3':
#         print('종료합니다')
#         break
#     else:
#         print('다시입력하세요')
#         os.system('pause')
#         continue

# # 야구게임 1~9중 3개의 중복되지 않는 3개의 숫자를 맞추는 게임
# # 3개의 숫자를 입력한 후 입력한 자리와 숫자가 같을경우 스트라이크, 숫자만 같을 경우 볼, 다 틀린경우 아웃이라고 한다.
# # 단, 숫자 입력시 범위값(1~9)을 벗어나거나 음수 입력시 다시 입력하게 해주고 Count는 1씩 증가한다.

# ch = None; record = list(); 
# while True:
#     os.system('cls')
#     print('야구 게임')
#     print('1.게임시작 2.최고기록 확인 3.종료', end=' ')
#     ch = input('>>> ')

#     if ch == '1':

#         cho = 1; cnt = 0; b_n = set() 

#         while 1:
#             b_n.add(random.randrange(1,10))
#             if len(b_n) == 3:
#                 break
#        # print(b_n) # 확인용

#         while cho:
#             cnt += 1
#             pn = list(); st,bl = 0,0;
#             for i in range(3):
#                 n = int(input('수입력: '))
#                 pn.append(n)

#             s_pn = set(pn)

#             if len(s_pn) < 3:
#                 print('중복된 수를 입력하지 마세요!')
#                 continue
#             elif len(s_pn) == 3:
#                 b = 0
#                 for i in range(3):
#                     if pn[i] <= 0 or pn[i] > 9:
#                         b+=1
#                 if b > 0 :
#                     print('범위를 벗아난 수를 입력하지 마세요!!')
#                     continue
#                 else:
#                     b_n = list(b_n)
#                     for i in range(3):
#                         for j in range(3):
#                             if b_n[i] == pn[j]:
#                                 bl += 1
#                                 if i == j:
#                                     bl -= 1
#                                     st += 1
#                     ot = 3 - bl - st    

#                     if st == 3:
#                         print('정답입니다!')
#                         if len(record) == 0:
#                             print(f'{cnt}회 최고기록')
#                             record.append(cnt)
#                         else:
#                             record.sort()
#                             if cnt < record[0]:
#                                 print(f'{cnt}, 최고기록 갱신')
#                             record.append(cnt)
#                         os.system('pause')
#                         cho = 0
#                     else:
#                         print(f'{st}스트라이크, {bl}볼, {ot}아웃')
#                         os.system('pause')
#                         continue

#     elif ch == '2':
#         if len(record) == 0:
#             print('등록된 기록이 없습니다.')
#             os.system('pause')
#             continue
#         s_r = set(record)
#         record = sorted(s_r)
#         print(f'{record[0]}회')
#         os.system('pause')
#         continue

#     elif ch == '3':
#         print('종료')
#         break

#     else:
#         print('다시입력하세요')
#         os.system('pause')
#         continue

# # 알파벳을 원하는대로 입력하고, 해당 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
# # 단, 대문자와 소문자를 구분하지 않는다.
# # 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다.
# # 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# st = input('알파벳 입력 : ')
# st = st.lower()
# alpa = 'abcdefghijklmnopqrstuvwxyz'; 
# ls = []; max = 0; max_index = 0; 
# for i in alpa:
#     ls.append(st.count(i))
# for i in range(len(ls)):
#     if max < ls[i]:
#         max = ls[i]
#         max_index = i
# ls = sorted(ls)
# ls.reverse()
# if ls[0] == ls[1]:
#     print('?')
# else:
#     print(alpa[max_index].upper())

# 문자열을 입력후 특정 알파벳 위치 찾기

st = None; f_alpa = None; cnt = 0; ch = None; ls = []
while True:
    print('1.문자열입력 2.문자입력 3.종료',end=" "); ch = input('>>> ')

    if ch == '1':
        st = input('문자열 입력 : ')
        if len(st) == 0:
            print('문자열을 입력하세요!')
        continue
    elif ch == '2':
        f_alpa = input('찾고자하는 문자 입력 : ')
        if len(f_alpa) == 0:
            print('찾고자하는 문자를 입력하세요!')
            continue
        cnt = 0
        while True:
            cnt = st.find(f'{f_alpa}',cnt)
            if cnt != -1:
                print(f'{f_alpa}의 위치는 {cnt}')
                cnt += 1
            else:
                break
    elif ch == '3':
        print('종료')
        break
    else:
        print('잘못입력했습니다.')
        continue

