import os

# 1에서 N 까지 이어적었을때 총 길이를 출력하는 프로그램 단, N > 0
p = 1; N = None; cho = None;
while p :
    os.system('cls')
    
    print('1 부터 N까지 길이를 구하는 프로그램 시작')
    print('1.시작\t2.종료',end=' |')
    cho = input(' >>> ')

    if cho == '1':
        N = int(input('수 입력: '))
        if N <= 0:
            continue
        else:
            ls = list()
            for i in range(1,N+1):
                ls.append(str(i))
            num = "".join(ls)
        print(f'출력: {ls}\n길이: {len(num)}')
        os.system('pause')

    elif cho == '2':
        print('프로그램 종료')
        p = 0
    else:
        continue

# 알파벳으로 이루어진 N개의 단어가 들어오면 길이가 짧은 순으로 정렬하는 프로그램을 작성하시오. 단, 길이가 같을경우 사전순으로 빠른걸 앞에 두시오 ex) a > b
# sort(key=len)옵션 사용할것!
wor = None; p = 1; cho = None; 
while p:
    os.system('cls')
    
    print('단어를 순서대로 정렬하는 프로그램 시작')
    print('1.시작\t2.종료',end=' |')
    cho = input(' >>> ')
    if cho == '1':
        wordP = []
        N = 0;
        N = int(input('반복할 횟수 입력: '))
        if N <= 0:
            continue
        else:
            for i in range(N):
                wor = input('단어 입력: ')
                wordP.append(wor)
            wordP.sort(key=len) # 
            print(f'단어 정렬 출력: {wordP}')
            os.system('pause')

    elif cho == '2':
        print('프로그램 종료')
        p = 0

    else:
        continue