import { createContext, useState } from "react";

export const ItemContext = createContext()
export const LoginContext = createContext()
export const CartContext = createContext()

const initialItemState = {
    "count": 0,
    "next": null,
    "previous": null,
    "results": []
}

const initialUserState = {
    isLoggedIn: false,
    access: "",
    refresh: ""
}

const Store = ({ children }) => {

    const [items, setItems] = useState(initialItemState)
    const [userToken, setUserToken] = useState(initialUserState)
    const [cart, setCart] = useState([])

    return (
        <ItemContext.Provider value={{ items, setItems }}>
            <LoginContext.Provider value={{ userToken, setUserToken }}>
                <CartContext.Provider value={{ cart, setCart }}>
                    {children}
                </CartContext.Provider>
            </LoginContext.Provider>
        </ItemContext.Provider>
    )
}

export default Store;