// components/ProtectedRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ children }) => {
  const token = localStorage.getItem('token');
  
  if (!token) {
    // 如果沒有 token，則跳轉到登入頁面
    return <Navigate to="/login" />;
  }

  // 如果有 token，則顯示子組件（例如儀表板）
  return children;
};

export default ProtectedRoute;
