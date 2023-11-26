import { useState } from "react";
import axios from "axios";
import validator from "validator";
import { DOMEN_SERVER } from "../../config/const.js";


const Register = () => {

    const [register, setRegister] = useState(() => {
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
    if (!validator.isEmail(register.email)) {
      alert("You did not enter email");
    } else if (register.password !== register.password2) {
      alert("Repeated password incorrectly");
    } else if (
      !validator.isStrongPassword(register.password, { minSymbols: 0 })
    ) {
      alert(
        "Password must consist of one lowercase, uppercase letter and number, at least 8 characters"
      );
    } else {
      axios
        .post(DOMEN_SERVER + "/users/sign_up", {
          username: register.username,
          email: register.email,
          password: register.password,
        })
        .then((res) => {
          if (res.status === 200) {
            alert("You reg");
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
      <h2>Register user:</h2>
      <form onSubmit={submitChackin}>
        <p>
          Name:{" "}
          <input
            type="username"
            id="username"
            name="username"
            value={register.usernamr}
            onChange={changeInputRegister}
          />
        </p>
        <p>
          Email:{" "}
          <input
            type="email"
            id="email"
            name="email"
            value={register.email}
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
            value={register.password}
            onChange={changeInputRegister}
          />
        </p>
        <p>
          Repeat password:{" "}
          <input
            type="password"
            id="password2"
            name="password2"
            value={register.password2}
            onChange={changeInputRegister}
          />
        </p>
        <input type="submit" />
      </form>
    </div>
  );
  
};

export default Register;


