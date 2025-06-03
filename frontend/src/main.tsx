import { RouterProvider } from "react-router";
import { createRoot } from 'react-dom/client';
import router from '@/routes.ts';

createRoot(document.getElementById('root')!).render(
    <RouterProvider router={router} />
);
