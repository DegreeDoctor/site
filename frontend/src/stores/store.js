import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core"

export const useStore = defineStore("main", {
    state: () => ({
        degrees: useStorage('degrees', []),
    }),
    //Act like computed in Vue
    getters: {
        hasDegrees: (state) => {
            return state.degrees.length > 0;
        },
    },
    //Act like methods in Vue
    actions: {
        addDegree() {
            this.degrees.push("Degree");
        },
    },
});
