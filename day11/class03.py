'''
상속
 - 이미 만들어진 코드를 상속 받는것
 - 상속받으면 상속받은 코드를 사용할 수 있다
'''

class Calc:

    def calc(self):
        print('부모 계산기')

# c = Calc()
# c.calc()

class Computer(Calc): # 상속받을려는 class를 ()안에 넣어주면 된다. 
    def calc(self):
        print('자식 계산기') # 오버라이딩 (자식과 부모의 값이 동시에 존재하는 것)

    def computer(self):
        print('컴퓨터')
        self.calc()
        super().calc() # 부모의 값을 가져온다
c = Computer()
c.computer()
# c.calc()

print('='*50)


class MemberInfo:

    def inputMember(self,m):

        while True:
            self.name = input('이름 입력: ')
            if m.get(self.name) != None:
                print('아이디 있음')
                continue
            break
        self.age = input('나이 입력: ')
        self.addr = input('주소입력: ')

    def __str__(self) -> str:
        return f'\t나이: {self.age}\t주소:{self.addr}'

class Display:
    def displayMember(self):
        mem_dic = {}
        for i in range(3):
            self.mem = MemberInfo()
            self.mem.inputMember(mem_dic)
            mem_dic[self.mem.name] = self.mem
        
        print('=====내용출력=====')

        for k,v in mem_dic.items():
            print(k,":",v)
            print(v.name)
            print(v.age)
            print(v.addr)


d = Display()

d.displayMember(); 