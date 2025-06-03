import axios from 'axios'

axios.defaults.baseURL = '/api';
axios.defaults.withCredentials = true;

const axiosInstance = axios.create();

const checkAuthStatus = async () => {
    try {
        await axiosInstance.get('/auth/status');
    }
    catch (error) {
        console.error('Unable to authenticate:', error);
        const pathname = window.location.pathname;
        if (!pathname.includes('login') && !pathname.includes('register')) {
            window.location.pathname = '/login';
        }
    }
}

export { checkAuthStatus };
export default axiosInstance;