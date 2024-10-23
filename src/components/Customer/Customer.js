// components/Customer/Customer.js
import React, { useState, useEffect } from 'react';
import { Container, Typography, Button, Table, TableBody, TableCell, TableHead,  TableRow, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from '@mui/material';
import apiClient from '../../api';

function Customer() {
  const [customers, setCustomers] = useState([]);
  const [open, setOpen] = useState(false);
  const [currentCustomer, setCurrentCustomer] = useState({ id: '', name: '', phone: '' });

  useEffect(() => {
    fetchCustomers();
  }, []);

  const fetchCustomers = async () => {
    try {
      const response = await apiClient.get('/Customer/GetCustomers', {
        headers: {
          'ParkingName': 'YourParkingName',
          'Token': localStorage.getItem('token'),
        },
      });
      setCustomers(response.data);
    } catch (error) {
      console.error('無法獲取客戶資料:', error);
    }
  };

  const handleOpenDialog = (customer) => {
    setCurrentCustomer(customer || { id: null, name: '', phone: '', plate: '' });
    setOpen(true);
  };

  const handleCloseDialog = () => {
    setOpen(false);
  };

  const handleSave = async () => {
    try {
      await apiClient.post('/Customer/InsertUpdateCustomer', currentCustomer, {
        headers: {
          'ParkingName': 'YourParkingName',
          'Token': localStorage.getItem('token'),
        },
      });
      fetchCustomers();  // 保存成功後刷新客戶列表
      handleCloseDialog();  // 關閉對話框
    } catch (error) {
      console.error('Failed to save customer', error);
    }
  };
  const handleDelete = async (customerId) => {
    try {
      await apiClient.delete(`/Customer/DeleteCustomer?customer_id=${customerId}`, {
        headers: {
          'ParkingName': 'YourParkingName',
          'Token': localStorage.getItem('token'),
        },
      });
      fetchCustomers();  // 刪除成功後刷新客戶列表
    } catch (error) {
      console.error('Failed to delete customer', error);
    }
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        客戶管理
      </Typography>
      <Button variant="contained" color="primary" onClick={() => handleOpenDialog()} style={{ marginBottom: '20px' }}>
        新增客戶
      </Button>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>客戶 ID</TableCell>
            <TableCell>名稱</TableCell>
            <TableCell>電話</TableCell>
            <TableCell>車牌號碼</TableCell>  {/* 新增車牌欄位 */}
            <TableCell>操作</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {customers.map((customer) => (
            <TableRow key={customer.id}>
              <TableCell>{customer.id}</TableCell>
              <TableCell>{customer.name}</TableCell>
              <TableCell>{customer.phone}</TableCell>
              <TableCell>{customer.plate}</TableCell>  {/* 顯示車牌號碼 */}
              <TableCell>
                <Button variant="outlined" color="primary" onClick={() => handleOpenDialog(customer)} style={{ marginRight: '10px' }}>
                  修改
                </Button>
                <Button variant="outlined" color="secondary" onClick={() => handleDelete(customer.id)}>
                  刪除
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      {/* 編輯和新增客戶的彈窗 */}
      <Dialog open={open} onClose={handleCloseDialog}>
        <DialogTitle>{currentCustomer.id ? '修改客戶' : '新增客戶'}</DialogTitle>
        <DialogContent>
          <TextField
            label="客戶名稱"
            fullWidth
            margin="normal"
            value={currentCustomer.name}
            onChange={(e) => setCurrentCustomer({ ...currentCustomer, name: e.target.value })}
          />
          <TextField
            label="電話"
            fullWidth
            margin="normal"
            value={currentCustomer.phone}
            onChange={(e) => setCurrentCustomer({ ...currentCustomer, phone: e.target.value })}
          />
          <TextField
            label="車牌號碼"
            fullWidth
            margin="normal"
            value={currentCustomer.plate}
            onChange={(e) => setCurrentCustomer({ ...currentCustomer, plate: e.target.value })}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog} color="secondary">取消</Button>
          <Button onClick={handleSave} color="primary">保存</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );

}

export default Customer;
