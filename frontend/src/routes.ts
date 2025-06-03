import { createBrowserRouter } from "react-router";
import App from "@/app";
import LoginPage from "@/auth/login";
import AppLayout from "@/app-layout";

const router = createBrowserRouter([
    {
        Component: App,
        children: [
            {
                index: true,
                Component: AppLayout,
            },
            {
                path: "login",
                Component: LoginPage,
            },
        ],
    },
]);

export default router;