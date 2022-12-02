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
        darkMode: useStorage("darkMode", false),
        // Current degree to view in degree view
        selectedDegree: useStorage("selectedDegree", ""),
    }),
    //Act like computed in Vue
    getters: {
        getCurrentDegree: (state) => {
            return state.degrees[state.selectedDegree];
        },
        getCredits: (state) => {
            return state.credits;
        },
        getDarkMode: (state) => {
            return state.darkMode;
        },
    },
    //Act like methods in Vue
    actions: {
        addDegree(degree) {
            //this.degrees[degree.name] = degree;
            this.degrees["Test Ryan Fun God Turbo"] = {
                name: "Test Ryan Fun God Turbo",
                majors: ["Computer Science"],
                minors: ["Mathematics"],
                pathway: "Artificial Intelligence",
                concentration: "Artificial Intelligence",
                template: {
                    "1-Fall": [
                        "Minds and Machines",
                        "Computer Science I",
                        "Calculus I",
                        "Physics I",
                    ],
                    "1-Spring": [
                        "Introduction to Cognitive Science",
                        "Introduction to Biology",
                        "Introduction to Biology Laboratory",
                        "Data Structures",
                        "Calculus II",
                    ],
                    "2-Fall": [
                        "Multivariable Calculus and Matrix Algebra",
                        "Writing in Context",
                        "Foundations of Computer Science",
                        "Computer Organization",
                    ],
                    "2-Spring": [
                        "Linear Algebra",
                        "Strategic Writing",
                        "Introduction to Algorithms",
                        "Principles of Software",
                    ],
                    "3-Summer": [
                        "Introduction to Artificial Intelligence",
                        "Programming for Cognitive Science and Artificial Intelligence",
                        "Critical Thinking",
                        "Operating Systems",
                    ],
                    "3-Fall or Spring": [
                        "Earth and Sky",
                        "Intelligent Virtual Agents",
                        "Introduction to Differential Equations",
                        "Programming Languages",
                    ],
                    "4-Fall": [
                        "Software Design and Documentation",
                        "Distributed Computing Over The Internet",
                        "Design and Analysis of Algorithms",
                        "Open Source Software",
                    ],
                    "4-Spring": [
                        "Randomized Algorithms",
                        "Machine Learning from Data",
                        "Computational Finance",
                        "Natural Language Processing",
                    ],
                },
            };
            this.selectedDegree = "Test Ryan Fun God Turbo";
        },
        updateDegree(name, degree) {
            this.degrees[name] = degree;
        },
        removeDegree(name) {
            delete this.degrees[name];
        },
        addCredits(name, amount) {
            if (!this.credits[name]) {
                this.credits[name] = amount;
            }
        },
        removeCredits(name) {
            if (this.credits[name]) {
                delete this.credits[name];
            }
        },
        changeCredits(name, amount) {
            if (this.credits[name]) {
                this.credits[name] = amount;
            }
        },
        fetchCredits(name) {
            return this.credits[name];
        },
        toggleDarkMode() {
            this.darkMode = !this.darkMode;
        },
    },
});
