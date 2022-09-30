<script>
import { useStore } from "../stores/store";
import ACourse from "../components/ACourse.vue";

export default {
    components: {
        ACourse,
    },
    data() {
        return {
            store: useStore(),
            crs: {
                name: "The Name",
                subject: "TEST",
                ID: "1234",
                description:
                    "I am describing a course. blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah",
                credits: 4,
                concentration: ["conc1.name"],
                prerequisites: ["course1.name"],
                crosslisted: {
                    CROSS: "1324",
                },
                properties: {
                    CI: true,
                    MR: true,
                },
                professors: ["The Profsessor"],
                offered: {
                    year: "all",
                    semesters: ["spring", "summer"],
                },
            },
        };
    },
};
</script>

<template>
    <router-link to="quiz">test</router-link>
    <ACourse :course="crs" />
</template>
