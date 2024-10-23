// src/api.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000',  // 這裡是 FastAPI 的 mock 伺服器 URL
  headers: {
    'Content-Type': 'application/json'
  }
});



export default apiClient;
