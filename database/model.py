from sqlalchemy.orm import DeclarativeBase
from pgvector.sqlalchemy import Vector
from sqlalchemy import Column, Integer, JSON

class Base(DeclarativeBase):
    pass

class BaseRecord(Base):
    __abstract__ = True

    id         = Column(Integer, primary_key=True, autoincrement=True)
    data       = Column(JSON, nullable=True) 
    embedding  = Column(Vector(1536), nullable=True)   
