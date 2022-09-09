import { defineStore } from "pinia";

export const useStore = defineStore("main", {
    state: () => ({
        temp: "test",
    }),
    //Act like computed in Vue
    getters: {
        getTemp: (state) => {
            return state.temp + "\n";
        },
    },
    //Act like methods in Vue
    actions: {
        addToTemp(param) {
            this.temp += param;
        },
    },
});
