from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, PayMachine
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 取得繳費機資訊
@router.get("/GetCashBox")
def get_cash_box(serial_number: str, db: Session = Depends(get_db)):
    paymachine = db.query(PayMachine).filter(PayMachine.serial_number == serial_number).first()
    if paymachine:
        return {"id": paymachine.id, "serial_number": paymachine.serial_number, "cash_box_total": paymachine.cash_box_total}
    return {"error": "PayMachine not found"}

# 更新錢箱金額
@router.post("/UpdateCashBox")
def update_cash_box(serial_number: str, amount: int, db: Session = Depends(get_db)):
    paymachine = db.query(PayMachine).filter(PayMachine.serial_number == serial_number).first()
    if paymachine:
        paymachine.cash_box_total += amount
        db.commit()
        return {"success": True, "updated_total": paymachine.cash_box_total}
    return {"error": "PayMachine not found"}
