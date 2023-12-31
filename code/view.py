import sqlite3
conn=sqlite3.connect("uni.db")

# 创建视图
conn.execute("CREATE VIEW view1 AS SELECT * FROM instructor WHERE salary > 100000")

# 创建 Instead of INSERT 触发器
conn.execute("""
CREATE TRIGGER view1_insert_instead
INSTEAD OF INSERT ON view1
BEGIN
    INSERT INTO instructor (ID, name, dept_name, salary) VALUES (NEW.ID, NEW.name, NEW.dept_name, NEW.salary);
END;
""")

# 尝试插入数据到视图
conn.execute("INSERT INTO view1 VALUES ('1234567', 'Zhang', 'Comp. Sci.', 1234567)")

# 查看结果
for row in conn.execute("SELECT * FROM instructor WHERE ID = '1234567'"):
    print(row)

# 清理环境
conn.execute("DROP VIEW view1")
# conn.execute("DROP TRIGGER view1_insert_instead")
conn.close()