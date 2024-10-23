import React, { useState } from 'react';
import { Dialog, DialogActions, DialogContent, DialogTitle, TextField, Button } from '@mui/material';
import { apiClient } from '../../apiClient';

function CustomerDialog({ open, handleClose, currentCustomer, fetchCustomers }) {
  const [customer, setCustomer] = useState(currentCustomer || { id: null, name: '', phone: '', plate: '' });

  const handleSave = async () => {
    try {
      await apiClient.post('/api/Customer/InsertUpdateCustomer', customer, {
        headers: {
          'ParkingName': 'YourParkingName',
          'Token': localStorage.getItem('token'),
        },
      });
      fetchCustomers();  // 更新客戶列表
      handleClose();  // 關閉對話框
    } catch (error) {
      console.error('保存客戶失敗:', error);
    }
  };

  return (
    <Dialog open={open} onClose={handleClose}>
      <DialogTitle>{customer.id ? '修改客戶' : '新增客戶'}</DialogTitle>
      <DialogContent>
        <TextField
          label="姓名"
          value={customer.name}
          onChange={(e) => setCustomer({ ...customer, name: e.target.value })}
          fullWidth
          margin="normal"
        />
        <TextField
          label="電話"
          value={customer.phone}
          onChange={(e) => setCustomer({ ...customer, phone: e.target.value })}
          fullWidth
          margin="normal"
        />
        <TextField
          label="車牌號碼"
          value={customer.plate}
          onChange={(e) => setCustomer({ ...customer, plate: e.target.value })}
          fullWidth
          margin="normal"
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={handleClose}>取消</Button>
        <Button onClick={handleSave} variant="contained" color="primary">
          保存
        </Button>
      </DialogActions>
    </Dialog>
  );
}

export default CustomerDialog;
