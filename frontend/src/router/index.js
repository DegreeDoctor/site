import { createRouter, createWebHistory } from "vue-router";
import { useStore } from "../stores/store";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "redirect",
            beforeEnter: () => {
                const store = useStore();
                if(store.hasDegrees) {
                    return {name: "degree"}
                }
                else {
                    return {name: "quiz"};
                }
            }
        },
        {
            path: "/degree",
            name: "degree",
            component: () => import("../views/DegreeView.vue"),
        },
        {
            path: "/quiz",
            name: "quiz",
            component: () => import("../views/QuizView.vue"),
        }
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
