import React from "react";
import "./style.css";

const Input = ({ name, label, type }) => {
  return (
    <div className="form-group">
      <label htmlFor={name}>{label}:</label>
      <input type={type} name={name} id={name} />
    </div>
  );
};

export default Input;
