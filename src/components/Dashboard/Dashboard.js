// components/Dashboard/Dashboard.js
import React from 'react';
import { Container, Typography, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function Dashboard() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');  // 清除 token
    navigate('/login');  // 返回登入頁面
  };

  const goToCustomerManagement = () => {
    navigate('/customers');  // 導航到客戶管理頁面
  };

  return (
    <Container>
      <Typography variant="h3" gutterBottom>
        儀表板
      </Typography>
      <Button variant="contained" color="primary" onClick={goToCustomerManagement} style={{ marginRight: '10px' }}>
        客戶管理
      </Button>
      <Button variant="contained" color="secondary" onClick={handleLogout}>
        登出
      </Button>
    </Container>
  );
}

export default Dashboard;
