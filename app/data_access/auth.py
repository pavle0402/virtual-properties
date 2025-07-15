from app.models.auth import User
from app.db.db_config import SessionLocal

#Data access layer for AUTH services

def register_new_user_dao(user_data: dict, db):
    if user_data:
        print("user dat", user_data)
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
    return True

def login_dao(email, username, db):
    user = db.query(User).filter(username=username).first() if username else db.query(User).filter(email=email).first()
    return user 