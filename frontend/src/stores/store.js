import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

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
                console.log(`adding to ${semester}`)
                this.degrees[this.selectedDegree].template[semester].push(course);
                console.log(this.degrees[this.selectedDegree].template[semester])
            } else if (action == "remove") {
                console.log(`removing ${course}`)
                console.log(this.degrees[this.selectedDegree].template[semester])
                this.degrees[this.selectedDegree].template[semester] = 
                    this.degrees[this.selectedDegree].template[semester].filter(
                        (item) => item != course
                    );
                console.log(this.degrees[this.selectedDegree].template[semester].filter(
                    (item) => item != course
                ))
                console.log(this.degrees[this.selectedDegree].template[semester])
            }

        },
        deleteEverything() {
            Object.keys(this.degrees).forEach( degreeName => {
                delete this.degrees[degreeName]
            })
        }
    },
});
