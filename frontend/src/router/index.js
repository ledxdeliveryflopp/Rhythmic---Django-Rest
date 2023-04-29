import { createRouter, createWebHistory } from "vue-router";
import LoginPage from "../pages/LoginPage";
import HomePage from "../pages/HomePage";
import { useCookies } from "vue3-cookies";

const cookies = useCookies().cookies;

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  {
    path: "/login",
    name: "login",
    component: LoginPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to) => {
  let isAuthenticated = cookies.isKey("token");
  if (!isAuthenticated && to.path !== "/login") {
    return { name: "login" };
  }
  if (isAuthenticated && to.name === "login") {
    return { name: "home" };
  }
});

export default router;
