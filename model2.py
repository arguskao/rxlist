#建立資料庫還有資料表
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String,Text,DateTime,Boolean, create_engine
from datetime import datetime


DATABASE_URI= "postgresql://arguskao:7TRNzGxKlLt1@polished-snowflake-578646.cloud.neon.tech:5432/main"
engine = create_engine(DATABASE_URI, pool_recycle=55)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Book(Base):
    __tablename__ = "rxlist4" # table name in the database
    id = Column(Integer, primary_key=True, unique=True, index=True)
    tel = Column(String)
    date= Column(DateTime)
    mode= Column(String)
    bool=Column(Boolean,default=False)
    point=Column(Integer)

def create_table():                         #從這邊定義如果創建table
    Base.metadata.create_all(engine)

def drop_table():                           #定義砍掉table
    Base.metadata.drop_all(engine)
    
if __name__ == "__main__":  
    create_table()
    #drop_table()    