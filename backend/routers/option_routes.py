from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, ParkingOption, NotifyOption
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 取得停車場運作參數的資訊
@router.get("/GetOptions")
def get_options(parking_name: str, db: Session = Depends(get_db)):
    options = db.query(ParkingOption).filter(ParkingOption.parking_name == parking_name).all()
    return [{"id": o.id, "option_name": o.option_name, "option_value": o.option_value} for o in options]

# 更新或插入停車場運作參數
@router.post("/SetOptions")
def set_options(parking_name: str, option_name: str, option_value: str, db: Session = Depends(get_db)):
    option = db.query(ParkingOption).filter(ParkingOption.parking_name == parking_name, ParkingOption.option_name == option_name).first()
    if option:
        option.option_value = option_value
    else:
        option = ParkingOption(parking_name=parking_name, option_name=option_name, option_value=option_value)
        db.add(option)
    db.commit()
    return {"success": True, "option_id": option.id}

# 取得停車場推播參數的資訊
@router.get("/GetNotifyOptions")
def get_notify_options(parking_name: str, db: Session = Depends(get_db)):
    options = db.query(NotifyOption).filter(NotifyOption.parking_name == parking_name).all()
    return [{"id": o.id, "notify_name": o.notify_name, "notify_value": o.notify_value} for o in options]

# 更新或插入停車場推播參數
@router.post("/SetNotifyOptions")
def set_notify_options(parking_name: str, notify_name: str, notify_value: str, db: Session = Depends(get_db)):
    option = db.query(NotifyOption).filter(NotifyOption.parking_name == parking_name, NotifyOption.notify_name == notify_name).first()
    if option:
        option.notify_value = notify_value
    else:
        option = NotifyOption(parking_name=parking_name, notify_name=notify_name, notify_value=notify_value)
        db.add(option)
    db.commit()
    return {"success": True, "notify_option_id": option.id}
