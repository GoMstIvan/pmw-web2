from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Log, LogImage
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 紀錄車牌觸發事件的日誌
@router.post("/PlateTriggered")
def plate_triggered(parking_name: str, level: int, device_name: str, msg: str, db: Session = Depends(get_db)):
    log_entry = Log(parking_name=parking_name, level=level, device_name=device_name, msg=msg)
    db.add(log_entry)
    db.commit()
    db.refresh(log_entry)
    return {"success": True, "log_id": log_entry.id}

# 取得指定條件的日誌
@router.get("/GetLogs", response_model=List[dict])
def get_logs(parking_name: str, level: int, db: Session = Depends(get_db)):
    logs = db.query(Log).filter(Log.parking_name == parking_name, Log.level == level).all()
    return [{"id": l.id, "parking_name": l.parking_name, "level": l.level, "device_name": l.device_name, "msg": l.msg, "created_at": l.created_at} for l in logs]

# 取得指定日誌的影像
@router.get("/GetLogImage")
def get_log_image(log_id: int, db: Session = Depends(get_db)):
    log_image = db.query(LogImage).filter(LogImage.log_id == log_id).first()
    if log_image:
        return {"image_path": log_image.image_path}
    return {"error": "Image not found"}

# 紀錄影像
@router.post("/LogImage")
def log_image(log_id: int, image_path: str, db: Session = Depends(get_db)):
    log_image = LogImage(log_id=log_id, image_path=image_path)
    db.add(log_image)
    db.commit()
    db.refresh(log_image)
    return {"success": True, "log_image_id": log_image.id}
