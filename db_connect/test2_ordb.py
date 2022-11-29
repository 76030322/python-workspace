import oracledb

class Oracle():

    def __init__(self):

    # 데이터베이스의 기본 정보를 넣어준다
        lib = 'C:\\app\\instantclient_19_17'
        oracledb.init_oracle_client(lib_dir = lib)
        
        dsn = oracledb.makedsn('192.168.65.128',1521,service_name='orcl.localdomain')
        
        # DB와 연결된 객체를 얻어온다.
        con = oracledb.connect(user='c##python',password='1234',dsn=dsn,encoding = 'utf-8')
        
        # 명령어 전송객체 얻어오기
        self.cur = con.cursor()

    def selectAll(self):
        return self.cur.execute('select* from newst')
    
    def selectAll02(self):
        sql = 'select * from newst';
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def selectOne(self,userId):
        sql = f"select * from newst where id='{userId}'";
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insert(self, *user):
        # sql = f"insert into newst(id,name,age) values('{user[0]}','{user[1]}',{user[2]})";
        sql = 'insert into newst(id,name,age) values(:1,:2,:3)';
        try:
            self.cur.execute(sql,user)
            self.con.commit()
        except:
            return 0;
        return self.cur.rowcount

    def delete_func(self, *userId):
        # sql = f"delete from newst where id = '{userId}'"
        sql = "delete from newst where id = :1"
        try:
            self.cur.execute(sql,userId)
            self.con.commit()
        except:
            return 0;
        return self.cur.rowcount

    def update(self,userId, userName, userAge):
        sql = "update newst set name=:1, age=:2 where id=:3"
        try:
            self.cur.execute(sql,(userName,userAge,userId))
            self.con.commit()
        except:
            return 0;
        return self.cur.rowcount

db = Oracle()
print(db.selectAll())

print('---'*27)
print('ID\t이름\t나이')
for row in db.selectAll():
    # print(row)
    print(f'{row[0]}\t{row[1]}\t{row[2]}')
print('---'*27); print()
print('---'*27)
print(db.selectAll02())

for row in db.selectAll02():
    print(row[0],row[1],row[2])
print('---'*27); print()

print('---'*27)
print(db.selectOne('111'))
print(db.selectOne("222"))
print(db.selectOne(333))
print('---'*27);print()

print('---'*27)
print('[ 저장 전 결과 값 ]')
print(db.selectAll02()); print()
print('새로운 값 입력!!!')
userId = input('아이디 입력: ')
userName = input('이름 입력: ')
userAge = int(input('나이 입력: '))
print(db.insert(userId,userName,userAge))
print('[ 저장 후 결과 값 ]')
print(db.selectAll02())
print('---'*27);print()

print('---'*27)
userID = input('삭제할 이이디 입력: ')
print(db.delete_func(userID))
print('[ 저장 후 결과 값 ]')
print(db.selectAll02())
print('---'*27);print()

print('---'*27)
print('[ 수정전 데이터 ]')
print(db.selectAll02()); print()
userId = input('수정할 아이디 입력: ')
userName = input('수정할 이름 입력: ')
userAge = int(input('수정할 나이 입력: '))
print(db.update(userId,userName,userAge))
print('[ 수정후 데이터 ]')
print(db.selectAll02())
print('---'*27);print()
