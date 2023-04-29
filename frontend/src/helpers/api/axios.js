import axios from "axios";
import { useCookies } from "vue3-cookies";

const { cookies } = useCookies();

axios.defaults.withCredentials = true;

export const api = axios.create({
  baseURL: process.env.VUE_APP_API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});
const authInterceptor = (config) => {
  const token = cookies.get("token");
  config.headers.Authorization = `Bearer ${token}`;
  return config;
};

api.interceptors.request.use(authInterceptor);
