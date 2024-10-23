// src/components/Vehicle/Vehicle.js
import React, { useState, useEffect } from 'react';
import { apiClient } from '../../apiClient';
import { Button, Table, TableBody, TableCell, TableHead, TableRow, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from '@mui/material';

function VehicleManagement() {
    const [vehicles, setVehicles] = useState([]);
    const [open, setOpen] = useState(false);
    const [currentVehicle, setCurrentVehicle] = useState({ id: null, plate: '' });

  useEffect(() => {
    fetchVehicles();
  }, []);

  const fetchVehicles = async () => {
    try {
      const response = await apiClient.get('/api/Customer/GetVehicleWithPlate', {
        headers: {
          'ParkingName': 'YourParkingName',
          'Token': localStorage.getItem('token'),
        },
      });
      setVehicles(response.data);
    } catch (error) {
      console.error('Failed to fetch vehicles', error);
    }
  };

  const handleOpenDialog = (vehicle) => {
    setCurrentVehicle(vehicle || { id: null, plate: '' });
    setOpen(true);
  };

  const handleCloseDialog = () => {
    setOpen(false);
  };

  const handleSaveVehicle = async () => {
    try {
      if (currentVehicle.id) {
        // 更新車輛
        await apiClient.post('/api/Customer/InsertUpdateCustomer', {
          ...currentVehicle,
        }, {
          headers: {
            'ParkingName': 'YourParkingName',
            'Token': localStorage.getItem('token'),
          },
        });
      } else {
        // 新增車輛
        await apiClient.post('/api/Customer/InsertUpdateCustomer', {
          plate: currentVehicle.plate,
        }, {
          headers: {
            'ParkingName': 'YourParkingName',
            'Token': localStorage.getItem('token'),
          },
        });
      }
      fetchVehicles();
      handleCloseDialog();
    } catch (error) {
      console.error('保存車輛失敗:', error);
    }
  };

  const handleDeleteVehicle = async (vehicleId) => {
    try {
      await apiClient.delete(`/api/Customer/DeleteVehicle?vehicle_id=${vehicleId}`, {
        headers: {
          'ParkingName': 'YourParkingName',
          'Token': localStorage.getItem('token'),
        },
      });
      fetchVehicles();  // 刪除後重新加載車輛列表
    } catch (error) {
      console.error('刪除車輛失敗:', error);
    }
  };
  

  return (
    <div>
      <h2>車輛管理</h2>
      <Button onClick={() => handleOpenDialog(null)} variant="contained">新增車輛</Button>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>車牌號碼</TableCell>
            <TableCell>操作</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {vehicles.map((vehicle) => (
            <TableRow key={vehicle.id}>
              <TableCell>{vehicle.plate}</TableCell>
              <TableCell>
                <Button variant="outlined" color="primary" onClick={() => handleOpenDialog(vehicle)} style={{ marginRight: '10px' }}>
                  修改
                </Button>
                <Button variant="outlined" color="secondary" onClick={() => handleDeleteVehicle(vehicle.id)}>
                  刪除
                </Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>

      {/* 車輛新增/修改對話框 */}
      <Dialog open={open} onClose={handleCloseDialog}>
        <DialogTitle>{currentVehicle.id ? '修改車輛' : '新增車輛'}</DialogTitle>
        <DialogContent>
          <TextField
            label="車牌號碼"
            value={currentVehicle.plate}
            onChange={(e) => setCurrentVehicle({ ...currentVehicle, plate: e.target.value })}
            fullWidth
            margin="normal"
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>取消</Button>
          <Button onClick={handleSaveVehicle} variant="contained" color="primary">
            保存
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}


export default VehicleManagement;
