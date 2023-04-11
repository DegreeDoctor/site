import { createRouter, createWebHashHistory } from "vue-router";
import { useStore } from "../stores/store";

const router = createRouter({
    mode: "hash",
    history: createWebHashHistory(),
    routes: [
        {
            path: "/",
            name: "redirect",
            beforeEnter: () => {
                const store = useStore();
                if (store.getCurrentDegree) {
                    return { name: "degree" };
                } else {
                    return { name: "quiz" };
                }
            },
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
        },
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
