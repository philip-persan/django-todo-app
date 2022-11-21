import React from "react";
import Input from "../../components/Input/Input";
import Button from "../../components/Button/Button";
import "./style.css";

const Login = () => {
  return (
    <div className="login-form">
      <h1>Login!</h1>
      <form action="" method="post">
        <Input name={"username"} type={"text"} label={"Username"} />
        <Input name={"password"} type={"password"} label={"Password"} />
        <Button type={"submit"} text={"Login"} />
      </form>
    </div>
  );
};

export default Login;
