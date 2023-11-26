import { useState } from "react";
import axios from "axios";
import validator from "validator";
import { DOMEN_SERVER } from "../../config/const.js";


const Login = () => {

    const [login, setRegister] = useState(() => {
    return {
      username: "",
      email: "",
      password: "",
      password2: "",
    };
  });
  const changeInputRegister = (event) => {
    event.persist();
    setRegister((prev) => {
      return {
        ...prev,
        [event.target.name]: event.target.value,
      };
    });
  };
  const submitChackin = (event) => {
    event.preventDefault();
    if (!validator.isEmail(login.email)) {
      alert("You did not enter email");
    }   else {
      axios
        .post(DOMEN_SERVER + "/users/sign_in", {
          username: login.username,
          email: login.email,
          password: login.password,
        })
        .then((res) => {
          if (res.status === 200) {
            alert("You login");
            window.location.href = "/users";
          } else {
            alert("There is already a user with this email");
          }
        })
        .catch((error) => {
          alert("An error occurred on the server");
          console.log(error);
        });
    }
  };
  return (
    <div className="form">
      <h2>Login user:</h2>
      <form onSubmit={submitChackin}>
        <p>
          Name:{" "}
          <input
            type="username"
            id="username"
            name="username"
            value={login.usernamr}
            onChange={changeInputRegister}
          />
        </p>
        <p>
          Email:{" "}
          <input
            type="email"
            id="email"
            name="email"
            value={login.email}
            onChange={changeInputRegister}
            formNoValidate
          />
        </p>
        <p>
          Password:{" "}
          <input
            type="password"
            id="password"
            name="password"
            value={login.password}
            onChange={changeInputRegister}
          />
        </p>
        <input type="submit" />
      </form>
    </div>
  );
  
};

export default Login;


