import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useStore = defineStore("main", {
    state: () => ({
        /* Degree is formatted as follows
            "name" {   
                //Name of degree user defined
                name: "",
                //List of major names
                majors: [],
                //List of minor names
                minors: [],
                //Name of pathway
                pathway: "",
                //Name of concentration
                concentration: "",
                // Template see program_template_specs.json in backend for it
                template: {
                    // Each Semester labeled by number for year and name of semester
                    // Contains a list of courses
                    1-Fall: [
                    ],
                }
            }
        */
        degrees: useStorage("degrees", {}),
        // Object of lists formatted as: {"course1": 4, "Course2", 3}
        credits: useStorage("credits", {}),
        // Current degree to view in degree view
        selectedDegree: useStorage("selectedDegree", "")
    }),
    //Act like computed in Vue
    getters: {
        getCurrentDegree: (state) => {
            return state.degrees[state.selectedDegree];
        },
        getCredits: (state) => {
            return state.credits;
        },
    },
    //Act like methods in Vue
    actions: {
        addDegree(degree) {
            //this.degrees[degree.name] = degree;
            this.degrees["Test Ryan Fun God Turbo"] = {
                "name": "Test Ryan Fun God Turbo",
                "majors": ["Computer Science"],
                "minors": ["Mathematics"],
                "pathway": "Artificial Intelligence",
                "concentration": "Artificial Intelligence",
            };
        },
        removeDegree(name) {
            delete this.degrees[name];
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
