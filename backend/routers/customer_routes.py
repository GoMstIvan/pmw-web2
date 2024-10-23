from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Customer, Group, SessionLocal
from typing import List
import logging

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 獲取所有群組資料
@router.get("/GetGroups", response_model=List[dict])
def get_groups(db: Session = Depends(get_db)):
    logging.info("Fetching all customer groups from database")
    groups = db.query(Group).all()
    return [{"id": group.id, "name": group.name, "description": group.description} for group in groups]

# 新增或更新群組
@router.post("/InsertUpdateGroup")
def insert_update_group(group_id: int, name: str, description: str, db: Session = Depends(get_db)):
    logging.info(f"Inserting or updating group with id: {group_id}")
    group = db.query(Group).filter(Group.id == group_id).first()
    
    if group:  # 更新現有群組
        group.name = name
        group.description = description
        logging.info(f"Updated group with id: {group_id}")
    else:  # 新增新群組
        group = Group(id=group_id, name=name, description=description)
        db.add(group)
        logging.info(f"Inserted new group with id: {group_id}")
    
    db.commit()
    db.refresh(group)
    return group

# 獲取所有或單個客戶資料
@router.get("/GetCustomers", response_model=List[dict])
def get_customers(customerid: List[int] = None, db: Session = Depends(get_db)):
    if customerid:
        logging.info(f"Fetching customer(s) with ID(s): {customerid}")
        customers = db.query(Customer).filter(Customer.id.in_(customerid)).all()
    else:
        logging.info("Fetching all customers")
        customers = db.query(Customer).all()

    return [{"id": customer.id, "name": customer.name, "phone": customer.phone, "is_active": customer.is_active} for customer in customers]

# 新增或更新客戶
@router.post("/InsertUpdateCustomer")
def insert_update_customer(customer_id: int, name: str, phone: str, is_active: bool, db: Session = Depends(get_db)):
    logging.info(f"Inserting or updating customer with ID: {customer_id}")
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    
    if customer:  # 更新現有客戶
        customer.name = name
        customer.phone = phone
        customer.is_active = is_active
        logging.info(f"Updated customer with ID: {customer_id}")
    else:  # 新增新客戶
        customer = Customer(id=customer_id, name=name, phone=phone, is_active=is_active)
        db.add(customer)
        logging.info(f"Inserted new customer with ID: {customer_id}")
    
    db.commit()
    db.refresh(customer)
    return customer

# 根據 groupid 獲取客戶資料，若無則列出全部
@router.get("/GetGroupCustomers", response_model=List[dict])
def get_group_customers(groupid: List[int] = None, db: Session = Depends(get_db)):
    if groupid:
        logging.info(f"Fetching customers for group(s) with ID(s): {groupid}")
        customers = db.query(Customer).filter(Customer.group_id.in_(groupid)).all()
    else:
        logging.info("Fetching all customers in all groups")
        customers = db.query(Customer).all()

    return [{"id": customer.id, "name": customer.name, "phone": customer.phone, "group_id": customer.group_id} for customer in customers]

# 根據車牌號碼獲取車輛資料，並從車輛資料中取得客戶資料
@router.get("/GetVehicleWithPlate", response_model=dict)
def get_vehicle_with_plate(plateNumber: str, db: Session = Depends(get_db)):
    logging.info(f"Fetching vehicle with plate number: {plateNumber}")
    
    # 假設你在 Customer 模型中有關聯的車輛資料
    customer = db.query(Customer).join(Customer.vehicles).filter(Customer.vehicles.any(plate=plateNumber)).first()

    if not customer:
        logging.info(f"No customer found for vehicle with plate number: {plateNumber}")
        return {"error": "Vehicle not found"}

    return {
        "customer_id": customer.id,
        "customer_name": customer.name,
        "customer_phone": customer.phone,
        "vehicle_plate": plateNumber
    }

# 檢查車牌是否存在
@router.get("/ChekcPlateExist", response_model=dict)
def check_plate_exist(plate: str, db: Session = Depends(get_db)):
    logging.info(f"Checking if plate exists: {plate}")
    
    # 假設你在 Customer 模型中有關聯的車輛資料
    vehicle = db.query(Customer).join(Customer.vehicles).filter(Customer.vehicles.any(plate=plate)).first()

    if vehicle:
        logging.info(f"Plate {plate} exists in the database.")
        return {"exists": True, "plate": plate}
    else:
        logging.info(f"Plate {plate} does not exist.")
        return {"exists": False, "plate": plate}


# 檢查 ETag 是否存在
@router.get("/ChekcETagExist", response_model=dict)
def check_etag_exist(etag: str, db: Session = Depends(get_db)):
    logging.info(f"Checking if ETag exists: {etag}")
    
    # 假設你在 Customer 模型中有關聯的車輛資料，並且有 eTag 欄位
    vehicle = db.query(Customer).join(Customer.vehicles).filter(Customer.vehicles.any(eTag=etag)).first()

    if vehicle:
        logging.info(f"ETag {etag} exists in the database.")
        return {"exists": True, "etag": etag}
    else:
        logging.info(f"ETag {etag} does not exist.")
        return {"exists": False, "etag": etag}


# 根據 groupid 取得 Customer 資料
@router.get("/GetGroupCustomers", response_model=List[dict])
def get_group_customers(groupid: int, db: Session = Depends(get_db)):
    customers = db.query(Customer).filter(Customer.group_id == groupid).all()
    
    return [{"id": customer.id, "name": customer.name, "phone": customer.phone} for customer in customers]

# 根據 customer id 取得 Customer 資料
@router.get("/GetCustomers", response_model=List[dict])
def get_customers(customerid: List[int], db: Session = Depends(get_db)):
    customers = db.query(Customer).filter(Customer.id.in_(customerid)).all()
    
    return [{"id": customer.id, "name": customer.name, "phone": customer.phone} for customer in customers]

# 根據車牌取得車輛資料
@router.get("/GetVehicleWithPlate", response_model=dict)
def get_vehicle_with_plate(plateNumber: str, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.vehicles.any(plate=plateNumber)).first()

    if customer:
        return {"customer_id": customer.id, "customer_name": customer.name, "plate": plateNumber}
    else:
        return {"error": "Vehicle not found"}

# 檢查車牌是否存在
@router.get("/ChekcPlateExist", response_model=dict)
def check_plate_exist(plate: str, db: Session = Depends(get_db)):
    vehicle_exists = db.query(Customer).filter(Customer.vehicles.any(plate=plate)).first()

    if vehicle_exists:
        return {"exists": True}
    else:
        return {"exists": False}

# 檢查 ETag 是否存在
@router.get("/ChekcETagExist", response_model=dict)
def check_etag_exist(etag: str, db: Session = Depends(get_db)):
    etag_exists = db.query(Customer).filter(Customer.vehicles.any(eTag=etag)).first()

    if etag_exists:
        return {"exists": True}
    else:
        return {"exists": False}
