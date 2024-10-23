import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from '@mui/material';

function OtherPage() {
  return (
    <div>
      <h1>This is the Other Page</h1>
      <Button variant="contained" color="primary" component={Link} to="/other/subpage1">
        Go to SubPage 1
      </Button>
      <Button variant="contained" color="secondary" component={Link} to="/other/subpage2" style={{ marginLeft: '10px' }}>
        Go to SubPage 2
      </Button>
    </div>
  );
}

export default OtherPage;
