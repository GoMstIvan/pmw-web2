{
  "openapi": "3.0.1",
  "info": {
    "title": "ASCDigit.PMS.APMS",
    "version": "1.0"
  },
  "paths": {
    "/BLPR/PlateTriggered": {
      "post": {
        "tags": [
          "BLPR"
        ],
        "summary": "接收後端辨識程式發送車牌辨識事件",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIIdentification"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIIdentification"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIIdentification"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIIdentification"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/GetGroups": {
      "get": {
        "tags": [
          "Customer"
        ],
        "summary": "根據groupid取得Group資料",
        "description": "若無id，則列出全部",
        "parameters": [
          {
            "name": "groupid",
            "in": "header",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/InsertUpdateGroup": {
      "post": {
        "tags": [
          "Customer"
        ],
        "summary": "新增修改Group資料",
        "description": "",
        "parameters": [
          {
            "name": "Id",
            "in": "query",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "Name",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Description",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "isBan",
            "in": "query",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "Customers",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/components/schemas/APICustomer"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/GetGroupCustomers": {
      "get": {
        "tags": [
          "Customer"
        ],
        "summary": "根據groupid取得Customer資料",
        "description": "若無id，則列出全部",
        "parameters": [
          {
            "name": "groupid",
            "in": "header",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/GetCustomers": {
      "get": {
        "tags": [
          "Customer"
        ],
        "summary": "根據customer id取得Customer資料",
        "description": "若無id，則列出全部",
        "parameters": [
          {
            "name": "customerid",
            "in": "header",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/GetVehicleWithPlate": {
      "get": {
        "tags": [
          "Customer"
        ],
        "summary": "根據車牌取得車輛資料",
        "description": "再由車輛資料中，取得Customer資料",
        "parameters": [
          {
            "name": "plateNumber",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/InsertUpdateCustomer": {
      "post": {
        "tags": [
          "Customer"
        ],
        "summary": "新增修改Customer資料",
        "description": "刪除Customer請將Enabled設定為false，便會視為訪客",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APICustomer"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APICustomer"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APICustomer"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APICustomer"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/ChekcPlateExist": {
      "get": {
        "tags": [
          "Customer"
        ],
        "summary": "檢查車牌是否存在",
        "description": "",
        "parameters": [
          {
            "name": "plate",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Customer/ChekcETagExist": {
      "get": {
        "tags": [
          "Customer"
        ],
        "summary": "檢查ETag是否存在",
        "description": "",
        "parameters": [
          {
            "name": "etag",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetPolicies": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "取得費率資料",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/InsertUpdatePolicy": {
      "post": {
        "tags": [
          "Fee"
        ],
        "summary": "新增修改費率資料",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIChargingPolicy"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIChargingPolicy"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIChargingPolicy"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIChargingPolicy"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetCalendars": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "取得節日紀錄",
        "description": "",
        "parameters": [
          {
            "name": "isContainOldData",
            "in": "query",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/InsertUpdaeCalendar": {
      "post": {
        "tags": [
          "Fee"
        ],
        "summary": "新增修改節日紀錄",
        "description": "不包含對應費率",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendar"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendar"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendar"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendar"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetRegularCharges": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "取得平日群組費率資料",
        "description": "日一二三四五六=\u003E0123456",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/InsertUpdateRegularCharge": {
      "post": {
        "tags": [
          "Fee"
        ],
        "summary": "新增修改平日群組費率",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIRegularCharge"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIRegularCharge"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIRegularCharge"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIRegularCharge"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetSpecialCharges": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "取得假日群組費率資料",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/InsertUpdateSpecialCharge": {
      "post": {
        "tags": [
          "Fee"
        ],
        "summary": "新增修改假日群組費率",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendarChrge"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendarChrge"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendarChrge"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APICalendarChrge"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetFreeBufferTime": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "取得指定時間的入場免費時間或出場緩衝時間",
        "description": "",
        "parameters": [
          {
            "name": "nTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetFeeWithCustomerGroup": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "計算指定群組在指定時間需要花費的金額",
        "description": "",
        "parameters": [
          {
            "name": "GroupID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "sTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "eTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Fee/GetFeeWithCustomer": {
      "get": {
        "tags": [
          "Fee"
        ],
        "summary": "計算指定顧客ID在指定時間需要花費的金額",
        "description": "",
        "parameters": [
          {
            "name": "CustomerID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "sTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "eTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetBusiness": {
      "get": {
        "tags": [
          "Info"
        ],
        "parameters": [
          {
            "name": "businessIndex",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetPaymachine": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "取得繳費機的資訊",
        "description": "",
        "parameters": [
          {
            "name": "paymachineIndex",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetParking": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "取得停車場的資訊",
        "description": "",
        "parameters": [
          {
            "name": "parkingIndex",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetParkingZone": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "根據停車場Id取得停車場區域的資訊",
        "description": "",
        "parameters": [
          {
            "name": "parkingIndex",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/SetParkingZone": {
      "post": {
        "tags": [
          "Info"
        ],
        "summary": "設定停車場區域的名稱、最大、使用中停車位",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIZone"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIZone"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIZone"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIZone"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetZoneEntrance": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "根據停車場區域Id取得停車場區域出入口的資訊",
        "description": "",
        "parameters": [
          {
            "name": "zoneids",
            "in": "header",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetEntranceDriveways": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "根據停車場區域出入口Id取得停車場區域出入口車道的資訊",
        "description": "",
        "parameters": [
          {
            "name": "entranceids",
            "in": "header",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetCameraRTSP": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "取得指定攝影機ID、畫質的RTSP",
        "description": "",
        "parameters": [
          {
            "name": "cameraID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "isMain",
            "in": "header",
            "schema": {
              "type": "boolean",
              "default": false
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/DeviceHeartBeat": {
      "post": {
        "tags": [
          "Info"
        ],
        "summary": "接收設備辨識程式心跳封包",
        "description": "",
        "parameters": [
          {
            "name": "deviceID",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "memo",
            "in": "query",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Info/GetDeviceStatus": {
      "get": {
        "tags": [
          "Info"
        ],
        "summary": "取得停車場各設備的狀態與最後運作時間",
        "description": "超過update_frequency*off_line_round的時間沒有更新，表示斷線",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Log/PlateTriggered": {
      "post": {
        "tags": [
          "Log"
        ],
        "summary": "紀錄Log",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APILog"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APILog"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APILog"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APILog"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Log/GetLogs": {
      "post": {
        "tags": [
          "Log"
        ],
        "summary": "取得指定時間段Log",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APILogparam"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APILogparam"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APILogparam"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APILogparam"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Log/GetLogImage": {
      "post": {
        "tags": [
          "Log"
        ],
        "summary": "取得指定Log的影像",
        "description": "",
        "parameters": [
          {
            "name": "id",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Notification/SendNotification": {
      "post": {
        "tags": [
          "Notification"
        ],
        "parameters": [
          {
            "name": "source",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "title",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "content",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Option/Restart": {
      "post": {
        "tags": [
          "Option"
        ],
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Option/GetOptions": {
      "get": {
        "tags": [
          "Option"
        ],
        "summary": "取得停車場運作參數的資訊",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Option/GetNotifyOptions": {
      "get": {
        "tags": [
          "Option"
        ],
        "summary": "取得停車場推播參數的資訊",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/PayMachine/GetUnExchangedData": {
      "get": {
        "tags": [
          "PayMachine"
        ],
        "summary": "取得尚未交班資訊",
        "description": "",
        "parameters": [
          {
            "name": "paymachineSN",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/PayMachine/InsertExchangeData": {
      "post": {
        "tags": [
          "PayMachine"
        ],
        "summary": "設定交班資訊",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIExchangData"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIExchangData"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIExchangData"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIExchangData"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/PayMachine/UpdateCashBox": {
      "post": {
        "tags": [
          "PayMachine"
        ],
        "summary": "更新錢箱金額",
        "description": "時間以Server時間為準。",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APICashBox"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APICashBox"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APICashBox"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APICashBox"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/PayMachine/GetCashBox": {
      "get": {
        "tags": [
          "PayMachine"
        ],
        "summary": "獲取錢箱金額",
        "description": "時間已Server時間為準。",
        "parameters": [
          {
            "name": "paymachineSN",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/PayMachine/GetInsideRecordsWithoutImage": {
      "get": {
        "tags": [
          "PayMachine"
        ],
        "summary": "搜尋場內車牌(不含影像)",
        "description": "",
        "parameters": [
          {
            "name": "ParkindId",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "Keyword",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/PayMachine/GetInsideRecordsWithImage": {
      "get": {
        "tags": [
          "PayMachine"
        ],
        "summary": "搜尋場內車牌(含影像)",
        "description": "",
        "parameters": [
          {
            "name": "ParkindId",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "Keyword",
            "in": "header",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Record/GetPassingLogWithID": {
      "post": {
        "tags": [
          "Record"
        ],
        "summary": "取得指定通行紀錄(無影像)",
        "description": "",
        "parameters": [
          {
            "name": "logID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Record/GetPassingLogImage": {
      "post": {
        "tags": [
          "Record"
        ],
        "summary": "取得指定通行紀錄的影像",
        "description": "",
        "parameters": [
          {
            "name": "logID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Record/GetPassingLogs": {
      "post": {
        "tags": [
          "Record"
        ],
        "summary": "取得指定條件通行紀錄(無影像)",
        "description": "",
        "parameters": [
          {
            "name": "Count",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "Driveway",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": -1
            }
          },
          {
            "name": "minID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/Record/GetPassingLogsByTime": {
      "post": {
        "tags": [
          "Record"
        ],
        "summary": "取得指定條件通行紀錄(無影像)",
        "description": "",
        "parameters": [
          {
            "name": "Count",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32"
            }
          },
          {
            "name": "StartTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "EndTime",
            "in": "header",
            "schema": {
              "type": "string",
              "format": "date-time"
            }
          },
          {
            "name": "Driveway",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": -1
            }
          },
          {
            "name": "minID",
            "in": "header",
            "schema": {
              "type": "integer",
              "format": "int32",
              "default": 0
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/Login": {
      "post": {
        "tags": [
          "User"
        ],
        "summary": "使用者登入。",
        "parameters": [
          {
            "name": "user",
            "in": "header",
            "description": "使用者名稱。",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "password",
            "in": "header",
            "description": "使用者密碼。",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/GetAuthority": {
      "get": {
        "tags": [
          "User"
        ],
        "summary": "獲取權限清單",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/GetGroups": {
      "get": {
        "tags": [
          "User"
        ],
        "summary": "獲取指定群組的權限資料",
        "description": "",
        "parameters": [
          {
            "name": "groupids",
            "in": "header",
            "description": "群組 ID 陣列。",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/GetGroupUsers": {
      "get": {
        "tags": [
          "User"
        ],
        "summary": "獲取指定群組的使用者資料",
        "description": "",
        "parameters": [
          {
            "name": "groupids",
            "in": "header",
            "description": "群組 ID 陣列。",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/GetUsers": {
      "get": {
        "tags": [
          "User"
        ],
        "summary": "獲取指定編號的使用者資料",
        "description": "",
        "parameters": [
          {
            "name": "userids",
            "in": "header",
            "schema": {
              "type": "array",
              "items": {
                "type": "integer",
                "format": "int32"
              }
            }
          },
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/InsertUpdateGroup": {
      "post": {
        "tags": [
          "User"
        ],
        "summary": "新增修改UserGroup",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "使用者群組資料。",
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIUserGroup"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIUserGroup"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIUserGroup"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIUserGroup"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    },
    "/User/InsertUpdateUser": {
      "post": {
        "tags": [
          "User"
        ],
        "summary": "新增修改User",
        "description": "",
        "parameters": [
          {
            "name": "ParkingName",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "Token",
            "in": "header",
            "required": true,
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "description": "使用者資料。",
          "content": {
            "application/json-patch+json": {
              "schema": {
                "$ref": "#/components/schemas/APIUser"
              }
            },
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/APIUser"
              }
            },
            "text/json": {
              "schema": {
                "$ref": "#/components/schemas/APIUser"
              }
            },
            "application/*+json": {
              "schema": {
                "$ref": "#/components/schemas/APIUser"
              }
            }
          }
        },
        "responses": {
          "200": {
            "description": "OK"
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "APIBLPR": {
        "type": "object",
        "properties": {
          "sn": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "ip": {
            "type": "string",
            "nullable": true
          },
          "port": {
            "type": "integer",
            "format": "int32"
          },
          "rtspStr": {
            "type": "string",
            "nullable": true
          },
          "enable": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "APICalendar": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "startTime": {
            "type": "string",
            "format": "date-time"
          },
          "endTime": {
            "type": "string",
            "format": "date-time"
          },
          "policyID": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "APICalendarChrge": {
        "type": "object",
        "properties": {
          "calendarID": {
            "type": "integer",
            "format": "int32"
          },
          "groupID": {
            "type": "integer",
            "description": "0表示為不在名單上的訪客",
            "format": "int32"
          },
          "policyID": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "APICamera": {
        "type": "object",
        "properties": {
          "suveillanceId": {
            "type": "integer",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "pName": {
            "type": "string",
            "nullable": true
          },
          "pIP": {
            "type": "string",
            "nullable": true
          },
          "pPort": {
            "type": "integer",
            "format": "int32"
          },
          "username": {
            "type": "string",
            "nullable": true
          },
          "password": {
            "type": "string",
            "nullable": true
          },
          "pEnabled": {
            "type": "boolean"
          },
          "channelIndex": {
            "type": "integer",
            "format": "int32"
          },
          "rtspStr": {
            "type": "string",
            "nullable": true
          },
          "enabled": {
            "type": "boolean"
          }
        },
        "additionalProperties": false
      },
      "APICashBox": {
        "type": "object",
        "properties": {
          "machineSN": {
            "type": "integer",
            "format": "int32"
          },
          "total": {
            "type": "integer",
            "format": "int32",
            "readOnly": true
          },
          "count100": {
            "type": "integer",
            "format": "int32"
          },
          "count50": {
            "type": "integer",
            "format": "int32"
          },
          "count10": {
            "type": "integer",
            "format": "int32"
          },
          "count5": {
            "type": "integer",
            "format": "int32"
          },
          "lastTime": {
            "type": "string",
            "format": "date-time"
          }
        },
        "additionalProperties": false
      },
      "APIChargingPeriod": {
        "type": "object",
        "properties": {
          "policyID": {
            "type": "integer",
            "format": "int32"
          },
          "startTime": {
            "type": "string",
            "description": "時段起始時間,24:00:00需寫作1.00:00:00",
            "format": "date-span"
          },
          "endTime": {
            "type": "string",
            "description": "時段結束時間,24:00:00需寫作1.00:00:00",
            "format": "date-span"
          },
          "rate": {
            "type": "integer",
            "description": "週期費率",
            "format": "int32",
            "nullable": true
          },
          "cycle": {
            "type": "integer",
            "description": "時間週期",
            "format": "int32",
            "nullable": true
          },
          "limit": {
            "type": "integer",
            "description": "週期費用上限",
            "format": "int32",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIChargingPolicy": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "dayLimit": {
            "type": "integer",
            "description": "null表示無上限限制",
            "format": "int32",
            "nullable": true
          },
          "chargingPeriods": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIChargingPeriod"
            },
            "description": "時間段費率，須為連續時間，且最後結束時間-最早開始時間為一天整",
            "nullable": true,
            "readOnly": true
          },
          "isTimeLegal": {
            "type": "boolean",
            "readOnly": true
          },
          "illLegalReason": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APICustomer": {
        "type": "object",
        "properties": {
          "groupID": {
            "type": "integer",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "phone": {
            "type": "string",
            "nullable": true
          },
          "vehiclesLimit": {
            "type": "integer",
            "format": "int32"
          },
          "effective": {
            "type": "string",
            "format": "date-time"
          },
          "expiry": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "enabled": {
            "type": "boolean"
          },
          "vehicles": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIVehicle"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APICustomerGroup": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "isBan": {
            "type": "boolean"
          },
          "customers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APICustomer"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIDriveWay": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "entranceId": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "isDirectIn": {
            "type": "boolean"
          },
          "cameras": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APICamera"
            },
            "nullable": true
          },
          "blpRs": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIBLPR"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIEntrance": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "inZoneId": {
            "type": "integer",
            "format": "int32"
          },
          "outZoneId": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "driveWays": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIDriveWay"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIExchangData": {
        "type": "object",
        "properties": {
          "paymachineSN": {
            "type": "integer",
            "format": "int32"
          },
          "userName": {
            "type": "string",
            "nullable": true
          },
          "exchangeTime": {
            "type": "string",
            "format": "date-time"
          },
          "payCount": {
            "type": "integer",
            "format": "int32"
          },
          "payAmount": {
            "type": "integer",
            "format": "int32"
          },
          "payEasyCardCount": {
            "type": "integer",
            "format": "int32"
          },
          "payEasyCardAmount": {
            "type": "integer",
            "format": "int32"
          },
          "refundAmount": {
            "type": "integer",
            "format": "int32"
          },
          "refund100Count": {
            "type": "integer",
            "format": "int32"
          },
          "refund50Count": {
            "type": "integer",
            "format": "int32"
          },
          "refund10Count": {
            "type": "integer",
            "format": "int32"
          },
          "refund5Count": {
            "type": "integer",
            "format": "int32"
          },
          "supply100Count": {
            "type": "integer",
            "format": "int32"
          },
          "supply50Count": {
            "type": "integer",
            "format": "int32"
          },
          "supply10Count": {
            "type": "integer",
            "format": "int32"
          },
          "supply5Count": {
            "type": "integer",
            "format": "int32"
          },
          "guiStart": {
            "type": "string",
            "nullable": true
          },
          "guiEnd": {
            "type": "string",
            "nullable": true
          },
          "guiCount": {
            "type": "integer",
            "format": "int32"
          },
          "guiAmount": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "APIIdentification": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "channel": {
            "type": "integer",
            "format": "int32"
          },
          "plate": {
            "type": "string",
            "nullable": true
          },
          "sceneImageStr": {
            "type": "string",
            "nullable": true
          },
          "plateImageStr": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APILog": {
        "type": "object",
        "properties": {
          "parkingID": {
            "type": "integer",
            "format": "int32",
            "nullable": true
          },
          "level": {
            "$ref": "#/components/schemas/Level"
          },
          "deviceName": {
            "type": "string",
            "nullable": true
          },
          "msg": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APILogparam": {
        "type": "object",
        "properties": {
          "sTime": {
            "type": "string",
            "format": "date-time"
          },
          "eTime": {
            "type": "string",
            "format": "date-time"
          },
          "levelList": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Level"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIParking": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "defaultFreeBefore": {
            "type": "integer",
            "format": "int32"
          },
          "defaultLeaveBuffer": {
            "type": "integer",
            "format": "int32"
          },
          "totalSpaces": {
            "type": "integer",
            "format": "int32"
          },
          "totalRemainSpaces": {
            "type": "integer",
            "format": "int32"
          },
          "zones": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIZone"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIRegularCharge": {
        "type": "object",
        "properties": {
          "dayOfWeek": {
            "type": "integer",
            "format": "int32"
          },
          "groupID": {
            "type": "integer",
            "description": "0表示為不在名單上的訪客",
            "format": "int32"
          },
          "policyID": {
            "type": "integer",
            "format": "int32"
          }
        },
        "additionalProperties": false
      },
      "APIUser": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "account": {
            "type": "string",
            "nullable": true
          },
          "password": {
            "type": "string",
            "nullable": true
          },
          "enabled": {
            "type": "boolean"
          },
          "groupID": {
            "type": "integer",
            "format": "int32"
          },
          "identity": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIUserGroup": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "description": {
            "type": "string",
            "nullable": true
          },
          "authorities": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Authority"
            },
            "nullable": true,
            "readOnly": true
          },
          "users": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIUser"
            },
            "nullable": true,
            "readOnly": true
          }
        },
        "additionalProperties": false
      },
      "APIVehicle": {
        "type": "object",
        "properties": {
          "customerID": {
            "type": "integer",
            "format": "int32"
          },
          "groupID": {
            "type": "integer",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "plate": {
            "type": "string",
            "nullable": true
          },
          "eTag": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "APIZone": {
        "type": "object",
        "properties": {
          "parkingID": {
            "type": "integer",
            "format": "int32"
          },
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "totalSpaces": {
            "type": "integer",
            "format": "int32"
          },
          "remainSpaces": {
            "type": "integer",
            "format": "int32"
          },
          "entrances": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/APIEntrance"
            },
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "Authority": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "format": "int32"
          },
          "name": {
            "type": "string",
            "nullable": true
          },
          "desc": {
            "type": "string",
            "nullable": true
          }
        },
        "additionalProperties": false
      },
      "Level": {
        "enum": [0, 1, 2, 3, 4, 5, 6],
        "type": "integer",
        "description": "\u003Cp\u003EPossible values:\u003C/p\u003E\r\n\u003Cul\u003E\r\n\u003Cli\u003E\u003Cb\u003E0[Trace]\u003C/b\u003E: \u003C/li\u003E\r\n\u003Cli\u003E\u003Cb\u003E1[Debug]\u003C/b\u003E: \u003C/li\u003E\r\n\u003Cli\u003E\u003Cb\u003E2[Information]\u003C/b\u003E: \u003C/li\u003E\r\n\u003Cli\u003E\u003Cb\u003E3[Warning]\u003C/b\u003E: \u003C/li\u003E\r\n\u003Cli\u003E\u003Cb\u003E4[Error]\u003C/b\u003E: \u003C/li\u003E\r\n\u003Cli\u003E\u003Cb\u003E5[Critical]\u003C/b\u003E: \u003C/li\u003E\r\n\u003Cli\u003E\u003Cb\u003E6[None]\u003C/b\u003E: \u003C/li\u003E\r\n\u003C/ul\u003E\r\n",
        "format": "int32"
      }
    }
  }
}