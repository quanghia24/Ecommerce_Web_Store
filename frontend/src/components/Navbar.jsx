import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
    return (
        <>
            <ul>
                <li><Link to="/">Task</Link></li>
                <li><Link to="/">Pomodoro</Link></li>
                <li><Link to="/">Eishenhower Mactrix</Link></li>
                <li><Link to="/">Profile</Link></li>
                <li><Link to="/login">Login</Link></li>
                <li><Link to="/logout">Logout</Link></li>
                <li><Link to="/register">Register</Link></li>
            </ul>
        </>
    )
}


export default Navbar