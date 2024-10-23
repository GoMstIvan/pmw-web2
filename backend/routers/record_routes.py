from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, PassingLog, PassingLogImage
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 根據 ID 取得通行紀錄 (無影像)
@router.post("/GetPassingLogWithID")
def get_passing_log_with_id(log_id: int, db: Session = Depends(get_db)):
    log_entry = db.query(PassingLog).filter(PassingLog.log_id == log_id).first()
    if log_entry:
        return {"id": log_entry.id, "driveway": log_entry.driveway, "start_time": log_entry.start_time, "end_time": log_entry.end_time}
    return {"error": "Log not found"}

# 取得通行紀錄的影像
@router.post("/GetPassingLogImage")
def get_passing_log_image(log_id: int, db: Session = Depends(get_db)):
    log_image = db.query(PassingLogImage).filter(PassingLogImage.log_id == log_id).first()
    if log_image:
        return {"image_path": log_image.image_path}
    return {"error": "Image not found"}

# 根據條件取得通行紀錄 (無影像)
@router.post("/GetPassingLogs")
def get_passing_logs(count: int, driveway: int, min_id: int = 0, db: Session = Depends(get_db)):
    logs = db.query(PassingLog).filter(PassingLog.driveway == driveway, PassingLog.min_id >= min_id).limit(count).all()
    return [{"id": l.id, "driveway": l.driveway, "log_id": l.log_id, "start_time": l.start_time, "end_time": l.end_time} for l in logs]

# 根據時間取得通行紀錄 (無影像)
@router.post("/GetPassingLogsByTime")
def get_passing_logs_by_time(start_time: str, end_time: str, db: Session = Depends(get_db)):
    logs = db.query(PassingLog).filter(PassingLog.start_time >= start_time, PassingLog.end_time <= end_time).all()
    return [{"id": l.id, "driveway": l.driveway, "log_id": l.log_id, "start_time": l.start_time, "end_time": l.end_time} for l in logs]
