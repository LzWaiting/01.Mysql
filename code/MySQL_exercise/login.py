from mysqlpython import Mysqlpython
from hashlib import sha1

u_name = input('请输入用户名:')
p_word = input('请输入密码:')

# 用 sha1 给 p_word 加密
s1 = sha1()		# 创建sha1加密对象
s1.update(p_word.encode('utf8'))
p_word2 = s1.hexdigest()	# 返回16进制加密结果

sqlh = Mysqlpython('country')
select = 'select password from user where\
		  username=%s;'

date = sqlh.all(select,[u_name])
if len(date) == 0:
	print('用户名不存在')
elif date[0][0] == p_word2:
	print('登录成功')
else:
	print('密码错误')