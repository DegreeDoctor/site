import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useStore = defineStore("main", {
    state: () => ({
        degrees: useStorage("degrees", []),
        credits: useStorage("credits", 0),
    }),
    //Act like computed in Vue
    getters: {
        hasDegrees: (state) => {
            return state.degrees.length > 0;
        },
        getCredits: (state) => {
            return state.credits;
        },
    },
    //Act like methods in Vue
    actions: {
        addDegree() {
            this.degrees.push("Degree");
        },
        changeCredits(amount) {
            this.credits += amount;
        },
    },
});
