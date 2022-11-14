'''
범위를 지정해서 특정 범위의 무작위 수를 뽑음 (0.00...0 ~ 0.99..9)
'''

import random,os

# for i in range(5):
#     print(random.random(), end=" ")
# print()

# for i in range(5):
#     print(int(random.random()*3), end=" ")
# print()

# for i in range(5):
#     print(random.randrange(4), end=" ") # 0 ~ 3까지의 범위 값을 구해줌
# print()

# # 로또 프로그램 만들기
# # 1~45 사이의 무작위 중복되지 않는 6개의 수

# ls = []; b = 1 
# while b:
#     ls.append(random.randrange(1,46))
#     s = set(ls)
#     ls = list(s)
#     if len(ls) == 6:
#         b = 0
# nls = sorted(ls)
# print(nls)

# s = set(); b = 1
# while b:
#     s.add(random.randrange(1,46))
#     if len(s) == 6:
#         b = 0
# print(s)

# # Updown 게임 만들기
# # 1-99 사이의 랜덤한 숫자를 프로그램이 가지게 되며, 해당 범위의 값을 맞추는 게임이다

# ch = None; record = list(); 
# while True:
#     os.system('cls')
#     print('1.게임시작 2.최고기록 확인 3.종료', end=' ')
#     ch = input('>>> ')
#     rn = random.randrange(1,99); # print(rn) # 확인용
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
#         os._exit(0)
#     else:
#         print('다시입력하세요')
#         os.system('pause')
#         continue

# 야구게임 1~9중 3개의 중복되지 않는 3개의 숫자를 맞추는 게임
# 3개의 숫자를 입력한 후 입력한 자리와 숫자가 같을경우 스트라이크, 숫자만 같을 경우 볼, 다 틀린경우 아웃이라고 한다.
# 단, 숫자 입력시 범위값(1~9)을 벗어나거나 음수 입력시 다시 입력하게 해주고 Count는 1씩 증가한다.

ch = None; record = list(); 
while True:
    os.system('cls')
    print('1.게임시작 2.최고기록 확인 3.종료', end=' ')
    ch = input('>>> ')

    if ch == '1':

        cho = 1; cnt = 0; b_n = set() 

        while 1:
            b_n.add(random.randrange(1,10))
            if len(b_n) == 3:
                break
       # print(b_n) # 확인용

        while cho:
            cnt += 1
            pn = list(); st,bl = 0,0;
            for i in range(3):
                n = int(input('수입력: '))
                pn.append(n)

            s_pn = set(pn)

            if len(s_pn) < 3:
                print('중복된 수를 입력하지 마세요!')
                continue
            elif len(s_pn) == 3:
                b = 0
                for i in range(3):
                    if pn[i] <= 0 or pn[i] > 9:
                        b+=1
                if b > 0 :
                    print('범위를 벗아난 수를 입력하지 마세요!!')
                    continue
                else:
                    b_n = list(b_n)
                    for i in range(3):
                        for j in range(3):
                            if b_n[i] == pn[j]:
                                bl += 1
                                if i == j:
                                    bl -= 1
                                    st += 1
                    ot = 3 - bl - st    

                    if st == 3:
                        print('정답입니다!')
                        if len(record) == 0:
                            print(f'{cnt}회 최고기록')
                            record.append(cnt)
                        else:
                            record.sort()
                            if cnt < record[0]:
                                print(f'{cnt}, 최고기록 갱신')
                            record.append(cnt)
                        os.system('pause')
                        cho = 0
                    else:
                        print(f'{st}스트라이크, {bl}볼, {ot}아웃')
                        os.system('pause')
                        continue
    elif ch == '2':
        if len(record) == 0:
            print('등록된 기록이 없습니다.')
            os.system('pause')
            continue
        s_r = set(record)
        record = sorted(s_r)
        print(f'{record[0]}회')
        os.system('pause')
        continue

    elif ch == '3':
        print('종료')
        os._exit(0)

    else:
        print('다시입력하세요')
        os.system('pause')
        continue