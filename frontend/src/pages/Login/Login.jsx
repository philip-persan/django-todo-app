import React, { useContext } from "react";
import Input from "../../components/Input/Input";
import Button from "../../components/Button/Button";
import "./style.css";
import AuthContext from "../../context/AuthContext";

const Login = () => {
  const { loginUser } = useContext(AuthContext);
  return (
    <div className="login-form">
      <h1>Login!</h1>
      <form onSubmit={loginUser}>
        <Input name={"username"} type={"text"} label={"Username"} />
        <Input name={"password"} type={"password"} label={"Password"} />
        <Button type={"submit"} text={"Login"} />
      </form>
    </div>
  );
};

export default Login;
