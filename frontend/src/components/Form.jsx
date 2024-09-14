import { useState } from "react";
import api from "../api";
import { Link, useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
    // route we go to when submit the form
    // method for logining or registering
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const name_of_method = method === "login" ? "Login" : "Register";
    const other_method = method === "register" ? "Login" : "Register";

    const handleChangeInputPage = (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            if (method === "login") {
                navigate("/register");
            } else {
                navigate("/login");
            }
        } catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
    };

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();
        // prevent submitting the incompleted form and reloading the page when that happens

        // send request to the correct route
        try {
            const res = await api.post(route, {username, password, email});
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate("/");
            } else {
                console.log(username + " " + password);
                navigate("/login");
            }
        } catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
    };
    return (
        <>
            <form onSubmit={handleSubmit} className="form-container">
                <h1>{name_of_method}</h1>
                <input
                    className="form-input"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                />
                {method === "register" && <input
                    className="form-input"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                />}
                <input
                    className="form-input"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                />
                {loading && <LoadingIndicator />}
                <button className="form-button" type="submit">
                    {name_of_method}
                </button>
                {(method === 'login') && <a onClick={handleChangeInputPage}>Having no account?</a>}
                {(method === 'register') && <a onClick={handleChangeInputPage}>Already have an account?</a>}

            </form>
            
        </>
    );
}

export default Form;
