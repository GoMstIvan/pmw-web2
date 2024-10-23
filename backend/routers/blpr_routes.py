from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, BLPR
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 車牌辨識事件處理
@router.post("/PlateTriggered")
def plate_triggered(plate_number: str, parking_name: str, token: str, db: Session = Depends(get_db)):
    blpr_entry = BLPR(plate_number=plate_number, parking_name=parking_name, token=token)
    db.add(blpr_entry)
    db.commit()
    return {"success": True, "blpr_id": blpr_entry.id}

# # 根據車牌號碼獲取車輛資訊
# @router.get("/GetVehicleWithPlate")
# def get_vehicle_with_plate(plate_number: str, db: Session = Depends(get_db)):
#     blpr_entry = db.query(BLPR).filter(BLPR.plate_number == plate_number).first()
#     if blpr_entry:
#         return {"plate_number": blpr_entry.plate_number, "detected_at": blpr_entry.detected_at}
#     return {"error": "Vehicle not found"}
