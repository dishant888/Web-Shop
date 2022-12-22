import { useContext } from "react"
import { Navigate, Outlet } from "react-router"
import { LoginContext } from "../Store"


export default function ProtectedRoutes() {
    const { userToken } = useContext(LoginContext)
    return (
        userToken.isLoggedIn ? <Outlet /> : <Navigate to="/login" />
    )
}
