from sqlalchemy import create_engine, MetaData, Column, Integer, String, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

def set_up():
	engine = create_engine('sqlite:///qazar.db', echo=True)
	metadata = MetaData()
	provision_requests = Table("provision_requests", metadata,
		Column("id", Integer, primary_key=True, autoincrement=True),
		Column("user_id", Integer, ForeignKey('users.id')),
		Column("ip_address", String(15)),
		Column("status", Integer)
	)
	users = Table("users", metadata,
		Column("id", Integer, primary_key=True),
		Column("name", String)
	)
	metadata.create_all(engine)
	return engine

class ProvisionRequest(Base):
    __tablename__ = 'provision_requests'

	id = Column(Integer, primary_key=True, autoincrement=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	ip_address = Column(String(15))
	status = Column(Integer)

	user = relationship("User")

	def __init__(self, user_id, ip_address, status):
		self.user_id = user_id
		self.ip_address = ip_address
		self.status = status

	def __repr__(self):
		return "<ProvisionRequest('%s','%s', '%s')>" % (self.user_id, self.ip_address, self.status)

class User(Base):
	 __tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "<User('%s')>" % (self.name)
