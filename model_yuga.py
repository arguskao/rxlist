#建立資料庫還有資料表
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String,Text,DateTime,Boolean, create_engine
from datetime import datetime
import psycopg2

#DATABASE_URI="postgresql://admin:xhxH2spnUyu47OBf7OBUKNvnzEpdVy@asia-east1.74d9c3bb-0415-43bb-a6a2-c014807120b7.gcp.ybdb.io:5433/yugabyte?ssl=true&sslmode=verify-full&sslrootcert=/Users/user/.postgresql/root.cert"

DATABASE_URI="postgresql://admin:OzeFaZB-tFTE3ZDBt4hDEdYzpOgNu3@asia-east1.869cafc0-88e9-4d81-b4d8-3f8222c3bcb5.gcp.ybdb.io:5433/yugabyte"


engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Book(Base):
    __tablename__ = "rxlist" # table name in the database
    id = Column(Integer, primary_key=True, unique=True, index=True)
    tel = Column(String)
    date= Column(DateTime)
    mode= Column(String)
    bool=Column(Boolean,default=False)
    point=Column(Integer)

def create_table():                         #從這邊定義如果創建table
    Base.metadata.create_all(engine)

    
if __name__ == "__main__":  
    create_table()
    #drop_table()    


