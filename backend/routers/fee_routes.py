from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, FeePolicy, FeeBuffer, ChargingPeriod, Calendar, RegularCharge, SpecialCharge
import logging
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def calculate_fee(GroupID: int, sTime: str, eTime: str, db: Session):
    # 自定義的費用計算邏輯，根據 GroupID 及時間段計算
    # 你可以使用 ChargingPeriod 和其他政策來計算總費用
    # 以下為示範計算邏輯
    total_fee = 0
    charging_periods = db.query(ChargingPeriod).filter(ChargingPeriod.policy_id == GroupID).all()
    for period in charging_periods:
        # 假設這裡有一個費率計算過程
        total_fee += period.rate
    return total_fee

def calculate_fee_for_customer(CustomerID: int, sTime: str, eTime: str, db: Session):
    # 根據 CustomerID 和時間範圍來計算總費用
    total_fee = 0
    # 自定義邏輯來計算費用
    return total_fee


# 取得費率資料
@router.get("/GetPolicies", response_model=List[dict])
def get_policies(db: Session = Depends(get_db)):
    logging.info("Fetching all fee policies from database")
    
    policies = db.query(FeePolicy).all()

    return [{"id": policy.id, "name": policy.name, "description": policy.description} for policy in policies]

# 新增或修改費率資料
@router.post("/InsertUpdatePolicy")
def insert_update_policy(policy_id: int, name: str, description: str, db: Session = Depends(get_db)):
    logging.info(f"Inserting or updating fee policy with ID: {policy_id}")
    
    policy = db.query(FeePolicy).filter(FeePolicy.id == policy_id).first()
    
    if policy:  # 更新現有費率
        policy.name = name
        policy.description = description
        logging.info(f"Updated fee policy with ID: {policy_id}")
    else:  # 新增新費率
        policy = FeePolicy(id=policy_id, name=name, description=description)
        db.add(policy)
        logging.info(f"Inserted new fee policy with ID: {policy_id}")
    
    db.commit()
    db.refresh(policy)
    return policy

# 取得指定時間的免費或緩衝時間
@router.get("/GetFreeBufferTime", response_model=dict)
def get_free_buffer_time(nTime: str, db: Session = Depends(get_db)):
    logging.info(f"Fetching free or buffer time for time: {nTime}")
    
    buffer_time = db.query(FeeBuffer).filter(FeeBuffer.nTime == nTime).first()

    if buffer_time:
        logging.info(f"Found buffer time for time: {nTime}")
        return {"nTime": nTime, "free_time": buffer_time.free_time, "buffer_time": buffer_time.buffer_time}
    else:
        logging.info(f"No buffer time found for time: {nTime}")
        return {"error": "Buffer time not found"}

# 獲取節日紀錄
@router.get("/GetCalendars", response_model=List[dict])
def get_calendars(db: Session = Depends(get_db)):
    calendars = db.query(Calendar).all()
    return [{"id": c.id, "name": c.name, "description": c.description, "start_time": c.start_time, "end_time": c.end_time} for c in calendars]

# 取得平日群組費率資料
@router.get("/GetRegularCharges", response_model=List[dict])
def get_regular_charges(db: Session = Depends(get_db)):
    logging.info("Fetching regular group charges")
    
    regular_charges = db.query(ChargingPeriod).filter(ChargingPeriod.policy_id == 1).all()  # 假設平日政策 ID 為 1

    return [{"id": charge.id, "start_time": charge.start_time, "end_time": charge.end_time, "rate": charge.rate} for charge in regular_charges]


# 取得假日群組費率資料
@router.get("/GetSpecialCharges", response_model=List[dict])
def get_special_charges(db: Session = Depends(get_db)):
    logging.info("Fetching special group charges")
    
    special_charges = db.query(ChargingPeriod).filter(ChargingPeriod.policy_id == 2).all()  # 假設假日政策 ID 為 2

    return [{"id": charge.id, "start_time": charge.start_time, "end_time": charge.end_time, "rate": charge.rate} for charge in special_charges]

# 計算指定群組在指定時間的費用
@router.get("/GetFeeWithCustomerGroup", response_model=dict)
def get_fee_with_customer_group(GroupID: int, sTime: str, eTime: str, db: Session = Depends(get_db)):
    logging.info(f"Calculating fee for GroupID: {GroupID} between {sTime} and {eTime}")
    
    # 假設有費用計算邏輯，這裡需要依照你的需求實現
    # 計算過程可依據 ChargingPeriod 的費率及其他參數進行
    total_fee = calculate_fee(GroupID, sTime, eTime, db)  # 自定義的計算函數
    
    return {"GroupID": GroupID, "total_fee": total_fee}

# 計算指定顧客 ID 在指定時間的費用
@router.get("/GetFeeWithCustomer", response_model=dict)
def get_fee_with_customer(CustomerID: int, sTime: str, eTime: str, db: Session = Depends(get_db)):
    logging.info(f"Calculating fee for CustomerID: {CustomerID} between {sTime} and {eTime}")
    
    # 假設有費用計算邏輯，這裡需要依照你的需求實現
    # 計算過程可依據 ChargingPeriod 的費率及其他參數進行
    total_fee = calculate_fee_for_customer(CustomerID, sTime, eTime, db)  # 自定義的計算函數
    
    return {"CustomerID": CustomerID, "total_fee": total_fee}

# 新增或更新節日紀錄
@router.post("/InsertUpdateCalendar")
def insert_update_calendar(calendar_id: int, name: str, start_time: str, end_time: str, db: Session = Depends(get_db)):
    calendar = db.query(Calendar).filter(Calendar.id == calendar_id).first()
    
    if calendar:
        calendar.name = name
        calendar.start_time = start_time
        calendar.end_time = end_time
    else:
        calendar = Calendar(id=calendar_id, name=name, start_time=start_time, end_time=end_time)
        db.add(calendar)
    
    db.commit()
    return {"success": True, "calendar_id": calendar.id}

# 新增或更新平日群組費率
@router.post("/InsertUpdateRegularCharge")
def insert_update_regular_charge(charge_id: int, day_of_week: int, group_id: int, policy_id: int, db: Session = Depends(get_db)):
    charge = db.query(RegularCharge).filter(RegularCharge.id == charge_id).first()
    
    if charge:
        charge.day_of_week = day_of_week
        charge.group_id = group_id
        charge.policy_id = policy_id
    else:
        charge = RegularCharge(id=charge_id, day_of_week=day_of_week, group_id=group_id, policy_id=policy_id)
        db.add(charge)
    
    db.commit()
    return {"success": True, "charge_id": charge.id}

# 新增或更新假日群組費率
@router.post("/InsertUpdateSpecialCharge")
def insert_update_special_charge(charge_id: int, group_id: int, policy_id: int, calendar_id: int, db: Session = Depends(get_db)):
    charge = db.query(SpecialCharge).filter(SpecialCharge.id == charge_id).first()
    
    if charge:
        charge.group_id = group_id
        charge.policy_id = policy_id
        charge.calendar_id = calendar_id
    else:
        charge = SpecialCharge(id=charge_id, group_id=group_id, policy_id=policy_id, calendar_id=calendar_id)
        db.add(charge)
    
    db.commit()
    return {"success": True, "charge_id": charge.id}