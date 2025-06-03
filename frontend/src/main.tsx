import { RouterProvider } from "react-router";
import { createRoot } from 'react-dom/client';
import router from '@/routes';

createRoot(document.getElementById('root')!).render(
    <RouterProvider router={router} />
);
