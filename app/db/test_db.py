from app.db.db_config import SessionLocal
from sqlalchemy import text

def test_db():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        print("database connected")
    except Exception as e:
        print("Error connecting to DB: ", e)
    
    db.close()

if __name__ == "__main__":
    test_db()