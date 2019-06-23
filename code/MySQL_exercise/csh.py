'''SQL 语句参数化
'''
import pymysql

class Mysql:	
	# 1. 创建数据库连接对象
	db = pymysql.connect(host='localhost',user='root',password='123456',database='country',charset='utf8')
	# 2. 创建游标对象
	cur = db.cursor()
	# 3. 游标方法 sql
	try:
		s_id = input('请输入省编号:')
		name = input('请输入省名字:')
		sql_insert = "insert into sheng(s_id,s_name) values(%s,%s);"
		print('ok')
		# 4. 提交到数据库执行
		cur.execute(sql_insert,[s_id,name])		# 列表传参
		db.commit()
	except Exception as e:
		# 回滚
		db.rollback()
		print('sql语句有误,已回滚',e)
	# 5. 关闭游标对象
	cur.close()
	# 6. 断开数据库连接
	db.close() 



