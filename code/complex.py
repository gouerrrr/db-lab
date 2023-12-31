import sqlite3
conn=sqlite3.connect('uni.db')
cur=conn.cursor()

'''1.	请问领取最高工资的老师信息(姓名, 院系, 薪水)?           10'
2.	请问领取物理学院最高工资的老师信息(姓名, 院系, 薪水)?   10' 
3.	列出每个学院最高的工资和人                            10'
4.	不用group by解决第三个问题。使用with语句，不用group by，列出每个学院工资最高的人                                           15'*3 
5.	选择每个学院工资前四的人。                      25'
'''
cmd1='select name,dept_name,salary from instructor where salary=(select max(salary) from instructor)'
cmd2='select name,dept_name,salary from instructor where dept_name="Physics" and salary=(select max(salary) from instructor where dept_name="Physics")'
cmd3='select name,dept_name,max(salary) from instructor group by dept_name'
cmd4='with max_salary(dept_name,max_salary) as (select instructor.dept_name,max(salary) from instructor group by instructor.dept_name) select name,instructor.dept_name,salary from instructor,max_salary where instructor.dept_name=max_salary.dept_name and instructor.salary=max_salary.max_salary'
cmd5='select name,dept_name,salary from instructor where (select count(*) from instructor as i where i.dept_name=instructor.dept_name and i.salary>instructor.salary)<4'
print("answer 1:")
for line in conn.execute(cmd1):
    print(line)
print("answer 2:")
for line in conn.execute(cmd2):
    print(line)
print("answer 3:")
for line in conn.execute(cmd3):
    print(line)
print("answer 4:")
for line in conn.execute(cmd4):
    print(line)
print("answer 5:")
for line in conn.execute(cmd5):
    print(line)


