import pymysql

# 1. 创建数据库连接对象
db = pymysql.connect(host='localhost',user='root',password='123456',database='db1',cahrset='utf8')

# 2. 创建游标对象
cur = db.cursor()

# 3. 执行SQL语句
cur.execute()

# 4. 提交到数据库执行
db.commit()

# 5. 关闭游标对象
cur.close()

# 6. 断开数据库连接
db.close()
