from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class Test(Base):
    __tablename__='tests'

    id = Column(Integer, primary_key = True)
    title = Column(String)
    content = Column(String)