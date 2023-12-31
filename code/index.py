import sqlite3
import time
conn=sqlite3.connect('uni.db')
cur=conn.cursor()

""" 设计查询语句,  对比有索引和没有索引在查询效率上的区别. """

# 有索引

cur.execute('create index index_name on student(name)')
begin=time.time()
for i in range(100000):
    cur.execute('select * from student where name="Samel"')

end=time.time()
cur.execute('drop index index_name')

print('有索引:',end-begin)

# 没有索引
begin=time.time()
for i in range(100000):
    cur.execute('select * from student where name="Samel"')
end=time.time()
print('没有索引:',end-begin)


