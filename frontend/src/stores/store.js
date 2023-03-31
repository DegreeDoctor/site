import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import coursesJson from "../data/courses.json";
import { v4 as uuidv4 } from "uuid";

export const useStore = defineStore("main", {
    state: () => ({
        /* Degree is formatted as follows
            "uuid" {
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
        selectedDegree: useStorage("selectedDegree", ""), // uuid
    }),
    //Act like computed in Vue
    getters: {
        getCurrentDegree: (state) => {
            if (!state.degrees) return undefined;
            if (state.selectedDegree != "") {
                // get index from uuid
                return state.degrees[state.selectedDegree];
            }
        },
        getCurrentDegreeName: (state) => {
            if (state.selectedDegree != "") {
                if (!state.degrees[state.selectedDegree]) return "";
                return state.degrees[state.selectedDegree].name;
            }
        },
        getCurrentDegreeIndex: (state) => {
            if (!state.degrees) return -1;
            if (state.selectedDegree != "") {
                return Object.keys(state.degrees).indexOf(state.selectedDegree);
            }
        },
        getCredits: (state) => {
            if (state.selectedDegree != "") {
                if (!state.degrees[state.selectedDegree]) return [];
                return state.degrees[state.selectedDegree].credits;
            }
        },
        getDarkMode: (state) => {
            return state.darkMode;
        },
        getDegreeUUID: (state) => {
            return Object.keys(state.degrees);
        },
        getDegreeSubNames: (state) => {
            // console.log(state.degrees[Object.keys(state.degrees)[getCurrentDegreeIndex]].name);
            let degreeNames = Object.keys(state.degrees);
            let degreeSubNames = [];
            degreeNames.forEach((degreeName) => {
                degreeSubNames.push(state.degrees[degreeName].name);
            });
            return degreeSubNames;
        },
        templateToArray: (state) => {
            if (!state.degrees[state.selectedDegree]) return [];
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
            // swap degree based uuid
            // console.log(name);
            // console.log(this.selectedDegree);
            this.selectedDegree = name;
        },
        findDegree(name) {
            // find degree's uuid based on name
            let uuid = "";
            Object.keys(this.degrees).forEach((degreeName) => {
                if (this.degrees[degreeName].name == name) {
                    uuid = degreeName;
                }
            });
            return uuid;
        },
        addDegree(degree) {
            let uuid = uuidv4();
            // console.log(degree);
            this.degrees[uuid] = degree; // degree is an object
            // console.log(this.degrees[uuid].name);
            // set the objects name atrribute to the uuid
            this.selectedDegree = uuid;
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
