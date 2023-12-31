import sqlite3
import time
import random
import os
conn=sqlite3.connect('index.db')
cur=conn.cursor()
# creat a random number 
def random_num():
    return random.randint(0,9999999999)
def random_data():
    return os.urandom(1024*1024)

""" 设计查询语句,  对比有索引和没有索引在查询效率上的区别. 
首先，随机生成数据，生成一个音频与音频id的对应表，每个音频的大小为1MB。
然后创建索引，最后进行查询"""
# 生成数据
cur.execute('create table audio(id int, audio blob)')
for i in range(30000):
    cur.execute('insert into audio values(?,?)',(random_num(),sqlite3.Binary(random_data())))

# 有索引
with_index_time_list=[]
cur.execute('create index index_audio on audio(id)')
begin=time.time()
for i in range(10000):
    cur.execute(f'select * from audio where id={i}')
end=time.time()
cur.execute('drop index index_audio')
print('有索引查询一万次:',end-begin)

# 没有索引
without_index_time_list=[]
begin=time.time()
for i in range(10000):
    cur.execute(f'select * from audio where id={i}')
end=time.time()
print('没有索引查询一万次:',end-begin)
conn.commit()
conn.close()