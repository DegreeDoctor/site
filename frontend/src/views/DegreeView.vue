<script>
import { useStore } from "../stores/store";
import ACourse from "../components/ACourse.vue";

export default {
    components: {
        ACourse
    },
    data() {
        return {
            store: useStore(),
            crs: {
                name: "Introduction to ALgogsd",
                subject: "TEST",
                ID: "1234",
                description:
                    "I am describing a course. blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah",
                credits: [1, 2, 3, 4],
                concentration: ["conc1.name"],
                prerequisites: ["course1.name"],
                crosslisted: {
                    CROSS: "1324",
                },
                properties: {
                    CI: true,
                    MR: false,
                },
                professors: ["The Profsessor"],
                offered: {
                    year: "uia",
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
