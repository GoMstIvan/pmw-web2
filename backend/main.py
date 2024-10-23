from fastapi import FastAPI
from routers import customer_routes, fee_routes, info_routes
from routers import log_routes, record_routes, notification_routes
from routers import option_routes, blpr_routes, user_routes, paymachine_routes
from models import Base, engine
import logging

app = FastAPI()

# 設置日誌級別和日誌文件路徑
logging.basicConfig(filename="backend/log/backend.log",
                    format='%(asctime)s %(message)s',
                    filemode='a',
                    level=logging.INFO)

logger = logging.getLogger()

# 確保資料庫表格已存在
Base.metadata.create_all(bind=engine)

# 引入 Customer 路由
app.include_router(customer_routes.router, prefix="/Customer")
app.include_router(fee_routes.router, prefix="/Fee")
app.include_router(info_routes.router, prefix="/Info")
app.include_router(log_routes.router, prefix="/Log")
app.include_router(record_routes.router, prefix="/Reccord")
app.include_router(notification_routes.router, prefix="/Notification")
app.include_router(option_routes.router, prefix="/Option")
app.include_router(blpr_routes.router, prefix="/Blpr")
app.include_router(user_routes.router, prefix="/User")
app.include_router(paymachine_routes.router, prefix="/PayMachine")

# 根路由測試
@app.get("/")
def read_root():
    return {"message": "API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
