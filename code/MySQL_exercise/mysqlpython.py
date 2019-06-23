from pymysql import *

class Mysqlpython:
	def __init__(self,database,
				 host='localhost',
				 user='root',
				 password='123456',
				 charset='utf8',
				 port=3306):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.database = database
		self.charset = charset

	def open(self):
		# 1. 创建数据库连接对象
		self.db = connect(host=self.host,
						  port=self.port,
						  user=self.user,
						  password=self.password,
						  database=self.database,
						  charset=self.charset)
		# 2. 创建游标对象
		self.cur = self.db.cursor()

	def sql(self,sql,L=[]):
		try:	
			self.open()
			# 3. sql命令
			self.cur.execute(sql,L)
			# 4. 执行sql命令
			self.db.commit()
			print('ok')
		except Exception as e:
			self.db.rollback()
			print('false',e)
		self.close()

	def all(self,sql,L=[]):
		try:
			self.open()
			self.cur.execute(sql,L)
			result = self.cur.fetchall()
			return result		
		except Exception as e:
			self.db.rollback()
			print('false',e)
		self.close()
	
	def close(self):
		# 5. 关闭游标对象
		self.cur.close()
		# 6. 断开数据库连接
		self.db.close()
