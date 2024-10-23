from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, User
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 新增或修改使用者
@router.post("/InsertUpdateUser")
def insert_update_user(username: str, hashed_password: str, group_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if user:
        user.hashed_password = hashed_password
        user.group_id = group_id
    else:
        user = User(username=username, hashed_password=hashed_password, group_id=group_id)
        db.add(user)
    db.commit()
    return {"success": True, "user_id": user.id}

# 獲取使用者資訊
@router.get("/GetUsers")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "username": u.username, "is_active": u.is_active} for u in users]
