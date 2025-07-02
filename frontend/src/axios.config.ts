import axios from 'axios'

axios.defaults.baseURL = '/api';
axios.defaults.withCredentials = true;

const axiosInstance = axios.create();

axiosInstance.interceptors.request.use(config => {
  const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];

  if (csrfToken) {
    config.headers['X-CSRFToken'] = csrfToken;
  }

  return config;
}, error => {
  return Promise.reject(error);
});

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