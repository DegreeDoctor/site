import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: HomeView,
        },
        {
            path: "/home",
            redirect: "/",
        },
        /*
            On non default pages you can Lazy load like below to have
            faster times to navigate pages.
        {
            path: "/about",
            name: "about",
            component: () => import("../views/AboutView.vue"),
        },
        */
    ],
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition;
        } else {
            return { top: 0 };
        }
    },
});

export default router;
