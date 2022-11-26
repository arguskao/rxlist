#建立資料庫還有資料表
import psycopg2
import pandas as pd 
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column, Integer, String,Text,DateTime,Boolean, create_engine
# from datetime import datetime

# DATABASE_URI="postgresql://arguskao:9iaQGFco27uHSEpWZwNF3A@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/ldb?sslmode=verify-full&options=--cluster%3Dlinebot-3532"

# engine = create_engine(DATABASE_URI)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class Book(Base):
#     __tablename__ = "rxlist" # table name in the database
#     id = Column(Integer, primary_key=True, unique=True, index=True)
#     tel = Column(String)
#     date= Column(DateTime)
#     mode= Column(String)
#     bool=Column(Boolean,default=False)
#     point=Column(Integer)

# def create_table():                         #從這邊定義如果創建table
#     Base.metadata.create_all(engine)

# def drop_table():                           #定義砍掉table
#     Base.metadata.drop_all(engine)
    
# if __name__ == "__main__":  
#     create_table()
#     #drop_table()    
    
    
DATABASE_URI="postgresql://arguskao:9iaQGFco27uHSEpWZwNF3A@free-tier6.gcp-asia-southeast1.cockroachlabs.cloud:26257/ldb?sslmode=verify-full&options=--cluster%3Dlinebot-3532"

conn = psycopg2.connect(DATABASE_URI)

cur = conn.cursor()

create='''
CREATE TABLE IF NOT EXISTS clinic7 (
                id serial PRIMARY KEY UNIQUE,          
                tel text NOT NULL,
                date date NOT NULL,
                mode text NOT NULL,
                bool boolean DEFAULT false NOT NULL,
                point Integer NOT NULL 
    )
'''
cur.execute(create)

conn.commit()


