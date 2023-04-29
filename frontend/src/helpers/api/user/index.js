import { login } from "@/helpers/api/user/requests";

export const loginService = (userData) => {
  return new Promise((resolve, reject) => {
    login(userData)
      .then((response) => {
        return response.response.data;
      })
      .catch((error) => {
        return reject(error.response.data);
      });
  });
};
