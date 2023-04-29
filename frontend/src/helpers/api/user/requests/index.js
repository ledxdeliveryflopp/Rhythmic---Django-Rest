import { api } from "@/helpers/api/axios";

export const login = (userData) => {
  return new Promise((resolve, reject) => {
    api
      .post(`login/`, userData)
      .then((profileData) => {
        resolve(profileData);
      })
      .catch((error) => reject(error));
  });
};
