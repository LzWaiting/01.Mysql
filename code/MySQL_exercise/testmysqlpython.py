'''测试mysqlpython'''

from mysqlpython import Mysqlpython

sqlh = Mysqlpython('country')

# sql_update = "update sheng set s_name='福建省'\
			  # where s_name='黑龙江省'"

sql_select = "select * from sheng where id = %s;"


# sqlh.sql(sql_update)
select_info = sqlh.all(sql_select,[1])
print(select_info)