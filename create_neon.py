from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String,Text,DateTime, create_engine
from datetime import datetime

#SQLALCHEMY_DATABASE_URL = "postgresql://arguskao:v2_3vTU2_QXafq8SDWbTMqBWU3Ay2Ydh@db.bit.io/arguskao/fate"
#DATABASE_URI = "postgresql://arguskao:v2_3vgis_Nj4NYLkSH25TS7k6sC7afai@db.bit.io/arguskao/demo"
#DATABASE_URI = "postgresql://arguskao:dp_0mZf0EiYOPgoZunun1g@liverx-3511.8nk.cockroachlabs.cloud:26257/fulunfung?sslmode=verify-full&options=--cluster%3Dliverx-3511"
DATABASE_URI= "postgresql://arguskao:7TRNzGxKlLt1@polished-snowflake-578646.cloud.neon.tech:5432/main"
engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # inherit from this class to create ORM models，相當重要

class Book(Base):
    __tablename__ = "rxlist" # table name in the database
    id = Column(Integer, primary_key=True, unique=True, index=True)
    序號 = Column(String)
    上傳日期= Column(DateTime)
    狀態= Column(String)

Base.metadata.create_all(engine)    