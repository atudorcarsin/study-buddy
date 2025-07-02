import { createBrowserRouter } from "react-router";
import App from "@/app";
import LoginPage from "@/auth/login";
import RegisterPage from "@/auth/register";
import AppLayout from "@/app-layout";

const router = createBrowserRouter([
    {
        Component: App,
        children: [
            {
                path: "/",
                Component: AppLayout,
                children: [

                ],
            },
            {
                path: "register",
                Component: RegisterPage,
            },
            {
                path: "login",
                Component: LoginPage,
            },
        ],
    },
]);

export default router;