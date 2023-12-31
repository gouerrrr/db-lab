import sqlite3
conn=sqlite3.connect("uni.db")

'''show the usage these data_operation sql commands:
(1)	delete
(2)	insert 
(3)	update
'''

def execute(cmd,ith):
    print(f"The result of {ith}command is:")
    for row in conn.execute(cmd):
        print(row)
# 创造一个1234567老师，改变他的名字，删除他
cmd_print = "select * from instructor where salary=1234567"
cmd_insert = "insert into instructor values('1234567','Zhang','Comp. Sci.',1234567)"
cmd_update = "update instructor set name='Li' where salary=1234567"
cmd_delete = "delete from instructor where salary=1234567"




execute(cmd_print,'first_print')
conn.execute(cmd_insert)
execute(cmd_print,"print-after-insert")
conn.execute(cmd_update)
execute(cmd_print,"print-after-update")
conn.execute(cmd_delete)
execute(cmd_print,"print-after-delete")


