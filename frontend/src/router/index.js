import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/pages/HomePage/index.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
