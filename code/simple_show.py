import sqlite3


conn=sqlite3.connect("uni.db")

'''
show the usage of these sql commands:
(1)	Natural Join 
(2)	String Operations:  %  _
(3)	between
(4)	Rename Operation:  as
(5)	order by  
(6)	min 
(7)	max 
(8)	sum 
(9)	count
'''
cmd1="select * from instructor natural join teaches where dept_name=\'Comp. Sci.\'"
cmd2="select * from instructor where name like \'e__s%\'"
cmd3="select * from instructor where salary between 90000 and 100000"
cmd4="select * from instructor as i where i.salary between 90000 and 100000 order by i.salary desc"
cmd5="select min(salary) from instructor"
cmd6="select max(salary) from instructor"
cmd7="select sum(salary) from instructor"
cmd8="select count(*) from instructor"


# execute the command and print the result
print("The result of command 1 is:")
for row in conn.execute(cmd1):
    print(row)
print("The result of command 2 is:")
for row in conn.execute(cmd2):
    print(row)
print("The result of command 3 is:")
for row in conn.execute(cmd3):
    print(row)
print("The result of command 4 is:")
for row in conn.execute(cmd4):
    print(row)
print("The result of command 5 is:")
for row in conn.execute(cmd5):
    print(row)
print("The result of command 6 is:")
for row in conn.execute(cmd6):
    print(row)
print("The result of command 7 is:")
for row in conn.execute(cmd7):
    print(row)
print("The result of command 8 is:")
for row in conn.execute(cmd8):
    print(row)


