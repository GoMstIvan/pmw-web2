from sqlalchemy import Column, Integer, String, Boolean, create_engine, ForeignKey, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os
import logging
import pymysql  # 引入 pymysql 驅動
from datetime import datetime

# 設置日誌級別
logging.basicConfig(level=logging.INFO)

Base = declarative_base()

#-----------------------------------------------------
# 測試用
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

#-----------------------------------------------------
# 車牌辨識模型
class BLPR(Base):
    __tablename__ = "blpr"
    
    id = Column(Integer, primary_key=True, index=True)
    plate_number = Column(String, index=True)  # 車牌號碼
    detected_at = Column(DateTime, default=datetime.utcnow)  # 偵測時間
    parking_name = Column(String)  # 停車場名稱
    token = Column(String)  # 驗證 token


#-----------------------------------------------------
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)  # 使用者名稱
    hashed_password = Column(String)  # 已加密的密碼
    is_active = Column(Boolean, default=True)  # 是否啟用
    group_id = Column(Integer, ForeignKey('groups.id'))  # 使用者群組

#-----------------------------------------------------

class PayMachine(Base):
    __tablename__ = "pay_machines"
    
    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String, index=True, unique=True)  # 繳費機序列號
    cash_box_total = Column(Integer)  # 總金額
    last_update = Column(DateTime, default=datetime.utcnow)  # 最後更新時間
    is_active = Column(Boolean, default=True)  # 是否啟用
#-----------------------------------------------------
class ParkingOption(Base):
    __tablename__ = "parking_options"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_name = Column(String, index=True)  # 停車場名稱
    option_name = Column(String, index=True)  # 參數名稱
    option_value = Column(String, nullable=True)  # 參數值

# 停車場推播參數模型
class NotifyOption(Base):
    __tablename__ = "notify_options"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_name = Column(String, index=True)  # 停車場名稱
    notify_name = Column(String, index=True)  # 推播名稱
    notify_value = Column(String, nullable=True)  # 推播值


#-----------------------------------------------------
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

# 通知模型
class Notification(Base):
    __tablename__ = "notifications"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)  # 通知的來源
    title = Column(String, nullable=True)  # 通知的標題
    content = Column(String, nullable=True)  # 通知的內容
    parking_name = Column(String, index=True)  # 停車場名稱
    token = Column(String)  # 驗證用 token
    created_at = Column(DateTime, default=datetime.utcnow)  # 創建時間


#-----------------------------------------------------
# 通行紀錄模型
class PassingLog(Base):
    __tablename__ = "passing_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    driveway = Column(Integer, index=True)
    log_id = Column(Integer, index=True)  # 日誌 ID
    min_id = Column(Integer, index=True)  # 最小 ID
    count = Column(Integer, default=1)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)

# 通行紀錄影像模型
class PassingLogImage(Base):
    __tablename__ = "passing_log_images"
    
    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer, index=True)
    image_path = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


#-----------------------------------------------------

# 日誌模型
class Log(Base):
    __tablename__ = "logs"
    
    id = Column(Integer, primary_key=True, index=True)
    parking_name = Column(String, index=True)  # 停車場名稱
    level = Column(Integer)  # 日誌級別 (如 0: Trace, 1: Debug, 2: Info 等等)
    device_name = Column(String, nullable=True)  # 設備名稱
    msg = Column(String)  # 日誌信息
    created_at = Column(DateTime, default=datetime.utcnow)  # 日誌創建時間

# 日誌影像模型
class LogImage(Base):
    __tablename__ = "log_images"
    
    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(Integer)  # 關聯的日誌 ID
    image_path = Column(String)  # 影像存放的路徑
    created_at = Column(DateTime, default=datetime.utcnow)  # 影像上傳時間

#-----------------------------------------------------

# 停車場模型
class Parking(Base):
    __tablename__ = "parking"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    total_spaces = Column(Integer)
    remain_spaces = Column(Integer)

    zones = relationship("ParkingZone", back_populates="parking")

# 停車區域模型
class ParkingZone(Base):
    __tablename__ = "parking_zones"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    total_spaces = Column(Integer)
    remain_spaces = Column(Integer)
    parking_id = Column(Integer, ForeignKey('parking.id'))

    parking = relationship("Parking", back_populates="zones")
    entrances = relationship("Entrance", back_populates="zone")

# 出入口模型
class Entrance(Base):
    __tablename__ = "entrances"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    zone_id = Column(Integer, ForeignKey('parking_zones.id'))

    zone = relationship("ParkingZone", back_populates="entrances")
    drive_ways = relationship("DriveWay", back_populates="entrance")

# 車道模型
class DriveWay(Base):
    __tablename__ = "drive_ways"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    is_direct_in = Column(Boolean, default=False)
    entrance_id = Column(Integer, ForeignKey('entrances.id'))

    entrance = relationship("Entrance", back_populates="drive_ways")
    cameras = relationship("Camera", back_populates="drive_way")

# 攝影機模型
class Camera(Base):
    __tablename__ = "cameras"
    
    id = Column(Integer, primary_key=True, index=True)
    rtsp_str = Column(String, index=True)
    is_main = Column(Boolean, default=False)
    drive_way_id = Column(Integer, ForeignKey('drive_ways.id'))

    drive_way = relationship("DriveWay", back_populates="cameras")

# 設備模型
class Device(Base):
    __tablename__ = "devices"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Boolean, default=True)
    last_update = Column(DateTime, default=datetime.utcnow)


# Business 模型
class Business(Base):
    __tablename__ = "businesses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)

# -----------------------------------------------------

# FeePolicy 模型
class FeePolicy(Base):
    __tablename__ = "fee_policies"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    day_limit = Column(Float, nullable=True)
    charging_periods = relationship("ChargingPeriod", back_populates="policy")

# ChargingPeriod 模型
class ChargingPeriod(Base):
    __tablename__ = "charging_periods"
    
    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey('fee_policies.id'))
    start_time = Column(String)  # 時段開始時間
    end_time = Column(String)  # 時段結束時間
    rate = Column(Float)  # 費率
    cycle = Column(Integer)  # 週期
    limit = Column(Float, nullable=True)  # 費率上限
    
    policy = relationship("FeePolicy", back_populates="charging_periods")

# FeeBuffer 模型
class FeeBuffer(Base):
    __tablename__ = "fee_buffers"
    
    id = Column(Integer, primary_key=True, index=True)
    nTime = Column(String)  # 查詢時間
    free_time = Column(Float)  # 免費時間
    buffer_time = Column(Float)  # 緩衝時間

# 節日模型
class Calendar(Base):
    __tablename__ = "calendars"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

# 平日群組費率模型
class RegularCharge(Base):
    __tablename__ = "regular_charges"
    
    id = Column(Integer, primary_key=True, index=True)
    day_of_week = Column(Integer)  # 0-6 代表日到六
    group_id = Column(Integer)
    policy_id = Column(Integer, ForeignKey("fee_policies.id"))

# 假日群組費率模型
class SpecialCharge(Base):
    __tablename__ = "special_charges"
    
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer)
    policy_id = Column(Integer, ForeignKey("fee_policies.id"))
    calendar_id = Column(Integer, ForeignKey("calendars.id"))

#-----------------------------------------------------

# Group 模型
class Group(Base):
    __tablename__ = "groups"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    customers = relationship("Customer", back_populates="group")

# Customer 模型
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    group_id = Column(Integer, ForeignKey('groups.id'))

    group = relationship("Group", back_populates="customers")

# MariaDB 連接字串，使用 pymysql 驅動
mariadb_url = "mysql+pymysql://qadmin:3753890@192.168.1.185:8000/asc_pms2"

# 嘗試連接 MariaDB，若失敗則連接 SQLite
try:
    # 使用 pymysql 進行 MariaDB 連接
    engine = create_engine(mariadb_url, pool_pre_ping=True)  # pool_pre_ping=True 用於檢查連接是否有效
    engine.connect()  # 測試連接
    logging.info("Connected to MariaDB")
except Exception as e:
    logging.error(f"MariaDB connection failed: {e}")
    logging.info("Switching to SQLite as fallback...")

    # 確保 SQLite 資料庫位於 backend 資料夾中
    sqlite_path = "./backend/fallback.db"
    if not os.path.exists("backend"):
        os.makedirs("backend")  # 確保 backend 資料夾存在

    sqlite_url = f"sqlite:///{sqlite_path}"
    engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})
    logging.info("Connected to SQLite")

# 創建資料庫會話
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 確保表格已存在
Base.metadata.create_all(bind=engine)
