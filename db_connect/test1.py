import cx_Oracle

def connection():

    global cur

    # 데이터베이스의 기본 정보를 넣어준다
    lib = 'C:\\app\\instantclient_19_17'
    cx_Oracle.init_oracle_client(lib_dir = lib)
    
    dsn = cx_Oracle.makedsn('192.168.65.128',1521,service_name='orcl.localdomain')
    
    # DB와 연결된 객체를 얻어온다.
    con = cx_Oracle.connect(user='c##python',password='1234',dsn=dsn,encoding = 'utf-8')
    
    # 명령어 전송객체 얻어오기
    cur = con.cursor()

def selectAll():
    return cur.execute('select* from newst')

cur = None;
connection()

# print(selectAll())

print('-'*25)
print('ID\t이름\t나이')
for row in selectAll():
    # print(row)
    print(f'{row[0]}\t{row[1]}\t{row[2]}')
print('-'*25)

