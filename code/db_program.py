import sqlite3
'''
(1)	以用户名+口令, 登录数据库
(2)	创建一个数据库和一张表格
(3)	向表格插入5行数据, 显示插入的结果
(4)	修改一行数据, 显示修改后的结果
(5)	删除一行数据, 显示删除后的结果
'''


class DBProgram:
    def __init__(self):
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = sqlite3.connect('test.db')
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS COMPANY
               (ID INT PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               AGE            INT     NOT NULL,
               ADDRESS        CHAR(50),
               SALARY         REAL);''')

    def insert_data(self):
        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )")
        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
        self.cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    def update_data(self):
        self.cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")

    def delete_data(self):
        self.cur.execute("DELETE from COMPANY where ID=2")

    def select_data(self):
        cursor = self.cur.execute("SELECT id, name, address, salary  from COMPANY")
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])
            print("ADDRESS = ", row[2])
            print("SALARY = ", row[3], "\n")

    def run(self):
        self.connect()
        self.create_table()
        self.insert_data()
        print("after insert:")
        self.select_data()
        self.update_data()
        print("After update:")
        self.select_data()
        self.delete_data()
        print("After delete:")
        self.select_data()
        self.disconnect()

dbp=DBProgram()
dbp.run()