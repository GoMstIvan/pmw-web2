from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Notification
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 發送通知
@router.post("/SendNotification")
def send_notification(source: str, title: str, content: str, parking_name: str, token: str, db: Session = Depends(get_db)):
    notification = Notification(source=source, title=title, content=content, parking_name=parking_name, token=token)
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return {"success": True, "notification_id": notification.id}
