import axios from 'axios';
const axiosInstance = axios.create({
    baseURL: 'http://192.168.101.184:8000/'
}); 
export default axiosInstance;