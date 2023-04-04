<script>
import { useStore } from "../stores/store";
import programsJson from "../data/programs.json";

export default {
    name: "DegreeChecker",
    data() {
        return {
            programsData: programsJson,
            store: useStore(),

        };
    },
    methods: {
        clicked(){
            let majors = []//this.programsData["2022-2023"]["Computer Science"]
            let currentDegree = this.store.getCurrentDegree;
            for(const major in currentDegree["majors"]){
                let currentMajor = currentDegree["majors"][major];
                majors.push(this.programsData["2022-2023"][currentMajor]);
            }
            let course = []
            for(const semester in currentDegree["template"]){
                course = [...course, ...currentDegree["template"][semester]];
            }
            for(const major in majors){
                for(const req in majors[major]["requirements"]){
                    if(!course.includes(req)){
                        console.log(req);
                    }
                }
            }
            console.log(majors)
            console.log(course)
        }
    },
};
</script>

<template>
<q-btn @click = "clicked">
test
</q-btn>
</template>
