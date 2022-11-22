#這裡是增加內容，最重要的！
from sqlalchemy.orm import Session
from models import *              #導入models.py


#如果只要查詢單一數據行，使用first()；如果要回傳所有符合條件的數據，使用all()。

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()      #這裡是單一數據

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):                
    return db.query(models.User).offset(skip).limit(limit).all()                #這裡是所有數據



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()




Session = sessionmaker(bind=engine)
s=Session()                         #之後用s取代Session()

book = Book(
    序號="1",
    上傳日期='2',
    狀態='3',
    
)
s.add(book)
s.commit()