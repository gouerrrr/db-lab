import sqlite3
conn=sqlite3.connect("uni.db")

'''show the usage of these nested sql commands:
(1)	Set Operations:  union, intersect,  except
(2)	Set Comparison:  some,  all  
(3)	Test for Empty Relations:  exists 
(4)	Test  Duplicate Tuples:  unique
(5)	from 后接子查询 
(6)	with ... as ...
'''

def execute(cmd,ith):
    print(f"The result of {ith}command is:")
    for row in conn.execute(cmd):
        print(row)
# Set operations
cmd1 = "select * from instructor where salary > 90000 union select * from instructor where salary < 60000"
cmd2 = "select * from instructor where salary > 70000 intersect select * from instructor where salary < 80000"
cmd3 = "select * from instructor where salary > 70000 except select * from instructor where salary < 90000"

# Set comparison
cmd4 = "select * from instructor where salary > (select MAX(salary) from instructor where dept_name = 'Comp. Sci.')"
cmd5 = "select * from instructor where salary > (select MIN(salary) from instructor where dept_name = 'Comp. Sci.')"

# Test for empty relations
cmd6 = "select * from instructor where exists (select * from instructor as i where i.dept_name = 'Comp. Sci.') and dept_name = 'Comp. Sci.'"
cmd7 = "select * from instructor where exists (select * from instructor as i where i.dept_name = 'no this deptname') and dept_name = 'Comp. Sci.'"

# Test for duplicate tuples
cmd9 = """
SELECT * FROM instructor
WHERE ID IN (
    SELECT ID FROM instructor
    WHERE dept_name = 'Comp. Sci.'
    GROUP BY ID
    HAVING COUNT(ID) > 1
)
"""

# From clause with a subquery
cmd10 = "select * from (select * from instructor where dept_name = 'Comp. Sci.') as i where i.salary>90000"

# With clause
cmd11 = "with temp as (select * from instructor where dept_name = 'Comp. Sci.') select * from temp where temp.salary>90000"

# execute the command and print the result




execute(cmd1,1)
execute(cmd2,2)
execute(cmd3,3)
execute(cmd4,4)
execute(cmd5,5)
execute(cmd6,6)
execute(cmd7,7)
execute(cmd9,9)
execute(cmd10,10)
execute(cmd11,11)



