import os

class Member:

    def memberInput(self,info={}):
        self.name = input('이름 입력: ')

        while True:
            self.id = input('아이디 입력: ')
            if info.get(self.id) != None:
                print('id가 존재합니다.'); continue; 
            break

        self.pwd = input('비밀번호 입력: ')
        print('회원가입을 축하합니다.')

class MemebeChk:

    def memeberAllDisplay(self,info):
        
        print('===모든 사용자 보기===')
        for i,j in info.items():
            print(f'이름: {j.name}\n아이디: {j.id}\n비밀번호: {j.pwd}')
            print('='*22)
            
    def memberChk(self,info,userId,userPwd):

        if info.get(userId) != None:
            if info.get(userId).pwd == userPwd: return 1
            else: return 0
        else: return -1

info={}; cho = None; 
while True:
    member = Member(); memCheck = MemebeChk(); 
    print('1.로그인 2.회원가입 3.모든 사용자 보기 4.종료'); cho = input('>>> ')
    if cho == '1':
        userId = input('아이디: '); userPwd = input('비밀번호: ')
        result = memCheck.memberChk(info,userId,userPwd)
        if result == 1: print('인증통과')
        elif result == 0: print('비밀번호 틀림')
        else: print('존재하지 않는 아이디 입니다.')
    elif cho == '2': member.memberInput(info); info[member.id] = member
    elif cho == '3':
        if len(info) == 0: print('저잗된 값이 없습니다.')
        else:

            memCheck.memeberAllDisplay(info)
            
    elif cho == '4': print('종료'); break
    else:
        os.system('cls')