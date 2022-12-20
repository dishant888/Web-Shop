import { createContext } from "react";


export const Store = createContext({
    isLoading: false,
    items: [],
    setItems: () => {},
})    