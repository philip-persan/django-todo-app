import { Outlet, Navigate } from "react-router-dom";

import React from "react";

const PrivateRoute = () => {
  const isAuth = false;
  return isAuth ? <Outlet /> : <Navigate to="/login" />;
};

export default PrivateRoute;
