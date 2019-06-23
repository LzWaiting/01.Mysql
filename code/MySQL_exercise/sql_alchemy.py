'''使用映射对象的方法创建一张表:
'''
# 连接数据库模块:
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String

engine = create_engine("mysql+pymysql:\
//root:123456@localhost/country",encoding='utf8')
Base = declarative_base()	# 生成一个orm基类

class User(Base):
	__tablename__ = 't123'
	id = Column(Integer,primary_key=True)
	name = Column(String(20))
	address = Column(String(40))


Base.metadata.create_all(engine)