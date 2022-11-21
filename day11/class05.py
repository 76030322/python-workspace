import os

class Member:
    
    def memberInput(self,info):
        self.name = input('이름 입력: ')

        while True:
            self.id = input('아이디 입력: ')
            if info.get(self.id) != None: print('존재하는 아이디 입니다'); continue
            break

        self.pwd = input('비밀번호 입력: ')
        print('회원가입 완료')

    def memberInfo(self,info):
        print('===모든 사용자 정보===')
        for x,y in info.items():
            print(f'이름: {y.name}\n아이디: {y.id}\n비밀번호: {y.pwd}')
            print('='*22)

    def memberLogin(self,info,userId,userPwd):
        if info.get(userId) != None:
            if info.get(userId).pwd == userPwd: return 1
            else: return 0
        else: return -1

class Computer:

    def __init__(self,version={},function={}) -> None:
        self.version = version
        self.function = function

    def versionP(self):
        print('컴퓨터 사양')
        for x,y in self.version.items():
            print(f'{x} : {y}')

    def functionP(self):
        print('컴퓨터 기능')
        for x,y in self.function.items():
            print(f'{x} : {y}')
        print('='*30)
        value = input('사용할 기능 입력: ')
        os.system(self.function[value])   

    def comDisplay(self):
        self.version = {'cpu':'R9','memory':'32GB'}
        self.function = {'계산기':'calc','메모장':'notepad'}
        num = None
        while True:
            print('1. version확인\n2.기능 확인\n3.종료'); num = input('>>> ')
            if num == '1': self.versionP()
            elif num == '2': self.functionP()
            elif num == '3': break
            else: os.system('cls')

info = {}; button = True; cho = None;
while button:
    print('1.로그인 2.회원가입 3.모든 사용자 보기 4. 종료'); cho = input(">>> ")
    member = Member(); com = Computer()
    if cho == '1': 
        print('===로그인===')
        userId = input('아이디: '); userPwd=input('비밀번호: ')
        result = member.memberLogin(info,userId,userPwd)
        if result == 1: print('인증통과'); com.comDisplay()
        elif result == 0: print('비밀번호 틀림')
        else: print('존재하지 않는 아이디입니다.')
    elif cho == '2': member.memberInput(info); info[member.id] = member
    elif cho == '3': member.memberInfo(info)
    elif cho == '4': print('종료'); button = False;
    else: os.system('cls');