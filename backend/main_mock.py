# main_mock.py
from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 啟用 CORS 中間件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或者限制為前端應用的URL，如 "http://localhost:3000"
    allow_credentials=True,
    allow_methods=["*"],  # 允許所有的 HTTP 方法
    allow_headers=["*"],  # 允許所有的 HTTP 頭
)

# 模擬的客戶數據
customers = [
    {"id": 1, "name": "John", "phone": "123456789", "plate": "ABC123"},
    {"id": 2, "name": "Jane", "phone": "987654321", "plate": "XYZ789"}
]


# 模擬登入 API
class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/User/Login")
async def login(request: LoginRequest):
    if request.username == "admin" and request.password == "admin":
        return {"token": "mock_token"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/Customer/InsertUpdateCustomer")
async def insert_update_customer(ParkingName: str = Header(None), Token: str = Header(None), customer: dict = {}):
    customer_id = customer.get("id")
    customer_name = customer.get("name")
    customer_phone = customer.get("phone")
    customer_plate = customer.get("plate")

    if not customer_name:
        raise HTTPException(status_code=400, detail="必需提供客戶名稱")

    if customer_id:
        # 更新客戶
        for c in customers:
            if c["id"] == customer_id:
                c["name"] = customer_name
                c["phone"] = customer_phone
                c["plate"] = customer_plate
                return {"message": "Customer updated successfully"}
    else:
        # 新增客戶
        new_id = max([c["id"] for c in customers]) + 1 if customers else 1
        customers.append({"id": new_id, "name": customer_name, "phone": customer_phone, "plate": customer_plate})
        return {"message": "Customer inserted successfully"}


@app.delete("/Customer/DeleteCustomer")
async def delete_customer(ParkingName: str = Header(None), Token: str = Header(None), customer_id: int = None):
    global customers
    if customer_id is None:
        raise HTTPException(status_code=400, detail="必需提供客戶ID")

    # 過濾出不需要刪除的客戶，實現刪除
    customers = [c for c in customers if c["id"] != customer_id]
    return {"message": "Customer deleted successfully"}



# GetCustomers 路由
@app.get("/Customer/GetCustomers")
async def get_customers(ParkingName: str = Header(None), Token: str = Header(None)):
    if not ParkingName or not Token:
        raise HTTPException(status_code=400, detail="ParkingName 和 Token 是必需的")
    return customers

# 查詢車輛根據車牌號碼
@app.get("/Customer/GetVehicleWithPlate")
async def get_vehicle_with_plate(ParkingName: str = Header(None), Token: str = Header(None), plateNumber: str = None):
    if not plateNumber:
        return vehicles
    vehicle = next((v for v in vehicles if v["plate"] == plateNumber), None)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

# 刪除車輛
@app.delete("/Customer/DeleteVehicle")
async def delete_vehicle(ParkingName: str = Header(None), Token: str = Header(None), vehicle_id: int = None):
    global vehicles
    vehicles = [v for v in vehicles if v["id"] != vehicle_id]
    return {"message": "Vehicle deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
