import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useStore = defineStore("main", {
    state: () => ({
        degrees: useStorage("degrees", []),
        // Object of lists formatted as: {"course1": 4, "Course2", 3}
        credits: useStorage("credits", {}),
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
        addCredits(name, amount) {
            if(!this.credits[name]) {
                this.credits[name] = amount;
            }
        },
        removeCredits(name) {
            if(this.credits[name]) {
                delete this.credits[name];
            }
        },
        changeCredits(name, amount) {
            if(this.credits[name]) {
                this.credits[name] = amount;
            }
        },
        fetchCredits(name) {
            return this.credits[name];
        }
    },
});
