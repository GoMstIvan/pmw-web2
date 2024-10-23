// src/pages/Login.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { TextField, Button, Container, Typography } from '@mui/material';
import apiClient from 'pmw-web2/src/api';  // 引入我們剛才建立的 api 客戶端

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError(null);
    
    try {
      const response = await apiClient.post('/User/Login', {
        username,
        password
      });

      // 假設成功返回 token
      localStorage.setItem('token', response.data.token);

      // 登入成功，跳轉到儀表板
      navigate('/dashboard');
    } catch (err) {
      setError('登入失敗，請檢查用戶名或密碼');
    }
  };

  return (
    <Container maxWidth="sm">
      <Typography variant="h4" align="center" gutterBottom>
        登入
      </Typography>
      <form onSubmit={handleLogin}>
        <TextField
          label="用戶名"
          variant="outlined"
          fullWidth
          margin="normal"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <TextField
          label="密碼"
          variant="outlined"
          fullWidth
          margin="normal"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && <Typography color="error">{error}</Typography>}
        <Button type="submit" variant="contained" color="primary" fullWidth>
          登入
        </Button>
      </form>
    </Container>
  );
}

export default Login;
