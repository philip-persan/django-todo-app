import React from "react";
import "./style.css";

const Button = ({ type, text }) => {
  return (
    <button className="p-btn" type={type}>
      {text}
    </button>
  );
};

export default Button;
