import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import coursesJson from "../data/courses.json";

export const useStore = defineStore("main", {
    state: () => ({
        /* Degree is formatted as follows
            "name" {
                //Credits
                // Object of lists formatted as: {"course1": 4, "Course2", 3}
                credits   {},
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
        darkMode: useStorage("darkMode", false),
        // Current degree to view in degree view
        selectedDegree: useStorage("selectedDegree", ""),
    }),
    //Act like computed in Vue
    getters: {
        getCurrentDegree: (state) => {
            if (state.selectedDegree != "") {
                return state.degrees[state.selectedDegree];
            }
        },
        getCurrentDegreeName: (state) => {
            return state.selectedDegree;
        },
        getCredits: (state) => {
            if (state.selectedDegree != "") {
                return state.degrees[state.selectedDegree].credits;
            }
        },
        getDarkMode: (state) => {
            return state.darkMode;
        },
        getDegreeNames: (state) => {
            return Object.keys(state.degrees);
        },
        templateToArray: (state) => {
            if(!state.degrees[state.selectedDegree]) return [];
            const template = state.degrees[state.selectedDegree]["template"];
            let array = [];
            let subArray = [];
            let sem = Object.keys(template)[0];
            for (const name in template) {
                if (name != sem) {
                    array.push([sem, subArray]);
                    sem = name;
                    subArray = [];
                }
                for (const i in template[name]) {
                    if (coursesJson) {
                        if (coursesJson[template[name][i]]) {
                            subArray.push(coursesJson[template[name][i]]);
                        }
                    }
                    subArray.push();
                }
            }
            return array;
        },
    },
    //Act like methods in Vue
    actions: {
        swapDegree(name) {
            this.selectedDegree = name;
        },
        addDegree(degree) {
            this.degrees[degree.name] = degree;
            this.selectedDegree = degree.name;
        },
        updateDegree(name, degree) {
            this.degrees[name] = degree;
        },
        removeDegree(name) {
            delete this.degrees[name];
        },
        addCredits(name, amount) {
            if (!this.degrees[this.selectedDegree].credits[name]) {
                this.degrees[this.selectedDegree].credits[name] = amount;
            }
        },
        removeCredits(name) {
            if (this.degrees[this.selectedDegree].credits[name]) {
                delete this.degrees[this.selectedDegree].credits[name];
            }
        },
        changeCredits(name, amount) {
            if (this.degrees[this.selectedDegree].credits[name]) {
                this.degrees[this.selectedDegree].credits[name] = amount;
            }
        },
        fetchCredits(name) {
            return this.degrees[this.selectedDegree].credits[name];
        },
        toggleDarkMode() {
            this.darkMode = !this.darkMode;
        },
        updateDegreeSemester(semester, course, action) {
            if (action == "add") {
                this.degrees[this.selectedDegree].template[semester].push(
                    course
                );
            } else if (action == "remove") {
                this.degrees[this.selectedDegree].template[semester] =
                    this.degrees[this.selectedDegree].template[semester].filter(
                        (item) => item != course
                    );
            }
        },
        deleteEverything() {
            Object.keys(this.degrees).forEach((degreeName) => {
                delete this.degrees[degreeName];
            });
        },
    },
});
