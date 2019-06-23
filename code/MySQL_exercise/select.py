'''cur游标方法使用及select用法'''

import pymysql

db = pymysql.connect(host='localhost',user='root',password='123456',database='country',charset='utf8')
cur = db.cursor()

try:
	sql_select = "select * from sheng;"
	cur.execute(sql_select)
	i = 1
	data1 = cur.fetchone()
	print('第',i,'条记录:',data1)
	print('********************************')
	data2 = cur.fetchmany(3)
	for line in data2:
		i += 1
		print('前',i,'条记录:',line)
	print('********************************')
	data3 = cur.fetchall()
	for line in data3:
		i += 1
		print('前',i,'条记录:',line)
	print('********************************')
	db.commit()
	print('ok')
except Exception as e:
	db.rollback()
	print('命令输入有误,已回滚',e)

cur.close()
db.close()

