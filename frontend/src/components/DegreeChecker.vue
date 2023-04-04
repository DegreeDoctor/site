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
            let computerScience = this.programsData["2022-2023"]["Computer Science"]
            let currentDegree = this.store.getCurrentDegree;
            console.log(computerScience)
            console.log(currentDegree)
        }
    },
};
</script>

<template>
<q-btn @click = "clicked">
test
</q-btn>
</template>
