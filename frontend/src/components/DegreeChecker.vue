<script>
import programsJson from "../data/programs.json"

export default {
    name: "DegreeChecker",
    data() {
        return {
            programsData: programsJson,

        };
    },
    methods: {
        clicked(){
            console.log(this.programsData)
        }
    },
};
</script>

<template>
<q-btn @click = "clicked">
test
</q-btn>
</template>
