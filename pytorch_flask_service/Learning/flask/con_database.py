from flask import Flask
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',database='db01',port=3306,charset='utf8')
cursor = conn.cursor()

# 创建表
# sql = "create table user(name varchar(40),age int );"

# 增加
'''try:
    sql = "insert into user(name,age) values('tom',18);"
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()'''

# 查询
'''sql = "select * from user ;"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    name = row[0]
    age = row[1]
    print('name=%s,age=%s'%(name,age))

cursor.close()
conn.close()'''

# 修改
'''try:
    sql = "update user set name='jerry' where age=18;"
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()'''

# 删除
try:
    sql = "delete from user where name='jerry';"
    cursor.execute(sql)
    conn.commit()
except Exception as e:
    print(e)
    conn.rollback()

if __name__ == '__main__':
    app.run()