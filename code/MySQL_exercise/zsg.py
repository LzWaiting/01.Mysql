'''sql命令增加/删除/修改使用'''

import pymysql

# 1. 创建数据库连接对象
db = pymysql.connect(host='localhost',user='root',password='123456',database='country',charset='utf8')

# 2. 创建游标对象
cur = db.cursor()

# 3. 执行SQL语句
try:	
	sql_insert = "insert into sheng values (12,200005,'新疆省');"
	cur.execute(sql_insert)
	sql_delete = "delete from sheng where s_name='日本省'"
	cur.execute(sql_delete)
	sql_update = "update sheng set id= 11,s_id=200003 where id=12;"
	cur.execute(sql_update)
	# 4. 提交数据库执行
	db.commit()
	print('ok')
except Exception as e:
	db.rollback()
	print('SQL语句有误,已回滚!',e)

# 5. 关闭游标对象
cur.close()

# 6. 断开数据库连接
db.close()