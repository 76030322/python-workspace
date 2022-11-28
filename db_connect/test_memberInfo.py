import oracledb

class Member:

    def __init__(self) -> None:
        
        lib = 'C:\\app\\instantclient_19_17'
        oracledb.init_oracle_client(lib_dir = lib)

        dsn = oracledb.makedsn('192.168.10.128',1521,service_name='orcl.localdomain')

        self.con = oracledb.connect(user='c##python',password='1234',dsn=dsn,encoding='UTF-8')

        self.cur = self.con.cursor()

    def selectAll(self):
        sql = 'select * from memberInfo order by id desc'
        self.cur.execute(sql)
        return self.cur.fetchall()

    def selectOne(self,m_id):
        sql = f"select * from memberInfo where id = '{m_id}'"
        self.cur.execute(sql)
        return self.cur.fetchall()

    def insertMember(self,*user):
        sql = "insert into memberInfo(id,name,age) values(:1,:2,:3)"
        try:
            self.cur.execute(sql,user)
            self.con.commit()
        except:
            return 0;
        return self.cur.rowcount

member = Member()

print(member.selectAll())
# print(member.selectOne(1))
# print(member.insertMember('5','Chin',20))
# print(member.selectOne('4'))