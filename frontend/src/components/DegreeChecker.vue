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
    computed: {
        checker(){
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
            let unfulfilled = []
            for(const major in majors){
                for(const req in majors[major]["requirements"]){
                    if(!course.includes(req)){
                        unfulfilled.push(req);
                    }
                }
            }
            return unfulfilled;
        }
    },
};
</script>

<template>
<q-card >
    <q-list dense>
        <q-item v-for = "item in checker" :key = "item">
            {{ item }}
        </q-item>
    </q-list>
</q-card>
</template>
