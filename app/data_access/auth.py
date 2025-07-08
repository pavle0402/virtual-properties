from app.models.auth import User
from app.db.db_config import SessionLocal

def register_new_user(user_data: dict, db):
    if user_data:
        print("user dat", user_data)
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
    return True