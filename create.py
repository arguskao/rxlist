#建立資料庫還有資料表
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String,Text,DateTime,Boolean, create_engine
from datetime import datetime


DATABASE_URI = "postgresql://arguskao:v2_3vgis_Nj4NYLkSH25TS7k6sC7afai@db.bit.io/arguskao/demo"
engine = create_engine(DATABASE_URI, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # inherit from this class to create ORM models，相當重要

class Book(Base):
    __tablename__ = "rxlist4" # table name in the database
    id = Column(Integer, primary_key=True, unique=True, index=True)
    tel = Column(String)
    date= Column(DateTime)
    mode= Column(String)
    bool=Column(Boolean,default=False)
    point=Column(Integer)

Base.metadata.create_all(engine)    