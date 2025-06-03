import { RouterProvider } from "react-router";
import { createRoot } from 'react-dom/client';
import router from '@/routes';
import { checkAuthStatus } from '@/axios.config'

checkAuthStatus();

createRoot(document.getElementById('root')!).render(
    <RouterProvider router={router} />
);
