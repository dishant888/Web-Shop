import { createContext, useState } from "react";


// export const Store = createContext({
//     isLoading: false,
//     items: [],
//     setItems: () => {},
// })

export const ItemContext = createContext()
export const LoginContext = createContext()

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

const Store = ({children}) => {

    const [items, setItems] = useState(initialItemState)
    const [userToken, setUserToken] = useState(initialUserState)


    return (
        <ItemContext.Provider value={{items, setItems}}>
            <LoginContext.Provider value={{userToken, setUserToken}}>
                {children}
            </LoginContext.Provider>
        </ItemContext.Provider>

    )
}

export default Store;