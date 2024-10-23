from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import SessionLocal, Business
from typing import List

router = APIRouter()

# 獲取數據庫會話
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 獲取商業資訊
@router.get("/GetBusiness", response_model=List[dict])
def get_business(businessIndex: int, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == businessIndex).first()

    if business:
        return {"id": business.id, "name": business.name, "address": business.address}
    else:
        return {"error": "Business not found"}

# 取得繳費機的資訊
@router.get("/GetPaymachine", response_model=dict)
def get_paymachine(paymachineIndex: int, db: Session = Depends(get_db)):
    paymachine = db.query(PayMachine).filter(PayMachine.id == paymachineIndex).first()

    if paymachine:
        return {"id": paymachine.id, "location": paymachine.location, "status": paymachine.status}
    else:
        return {"error": "Paymachine not found"}

# 取得停車場的資訊
@router.get("/GetParking", response_model=dict)
def get_parking(parkingIndex: int, db: Session = Depends(get_db)):
    parking = db.query(Parking).filter(Parking.id == parkingIndex).first()

    if parking:
        return {
            "id": parking.id,
            "name": parking.name,
            "totalSpaces": parking.total_spaces,
            "remainSpaces": parking.remain_spaces
        }
    else:
        return {"error": "Parking not found"}

# 根據停車場Id取得停車場區域的資訊
@router.get("/GetParkingZone", response_model=List[dict])
def get_parking_zone(parkingIndex: int, db: Session = Depends(get_db)):
    parking_zones = db.query(ParkingZone).filter(ParkingZone.parking_id == parkingIndex).all()

    return [{"id": zone.id, "name": zone.name, "totalSpaces": zone.total_spaces, "remainSpaces": zone.remain_spaces} for zone in parking_zones]

# 根據停車場區域Id取得停車場區域出入口的資訊
@router.get("/GetZoneEntrance", response_model=List[dict])
def get_zone_entrance(zoneids: List[int], db: Session = Depends(get_db)):
    entrances = db.query(Entrance).filter(Entrance.zone_id.in_(zoneids)).all()

    return [{"id": entrance.id, "name": entrance.name, "driveWays": entrance.drive_ways} for entrance in entrances]

# 根據停車場區域出入口Id取得停車場區域出入口車道的資訊
@router.get("/GetEntranceDriveways", response_model=List[dict])
def get_entrance_driveways(entranceids: List[int], db: Session = Depends(get_db)):
    driveways = db.query(DriveWay).filter(DriveWay.entrance_id.in_(entranceids)).all()

    return [{"id": driveway.id, "name": driveway.name, "isDirectIn": driveway.is_direct_in} for driveway in driveways]

# 取得指定攝影機ID、畫質的RTSP
@router.get("/GetCameraRTSP", response_model=dict)
def get_camera_rtsp(cameraID: int, isMain: bool = False, db: Session = Depends(get_db)):
    camera = db.query(Camera).filter(Camera.id == cameraID).first()

    if camera:
        return {"cameraID": camera.id, "rtsp": camera.rtsp_str, "isMain": isMain}
    else:
        return {"error": "Camera not found"}

# 接收設備辨識程式心跳封包
@router.post("/DeviceHeartBeat", response_model=dict)
def device_heartbeat(deviceID: str, memo: str = "", db: Session = Depends(get_db)):
    # 記錄心跳封包信息
    logging.info(f"Received heartbeat from device {deviceID} with memo: {memo}")

    # 可以將心跳信息寫入數據庫或進行其他處理
    return {"status": "Heartbeat received"}

# 取得停車場各設備的狀態與最後運作時間
@router.get("/GetDeviceStatus", response_model=List[dict])
def get_device_status(db: Session = Depends(get_db)):
    devices = db.query(Device).all()

    return [{"id": device.id, "name": device.name, "status": device.status, "lastUpdate": device.last_update} for device in devices]
