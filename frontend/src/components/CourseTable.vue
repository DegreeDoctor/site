<template>
    <div id="table">
        <Semester
            v-for="semester in semesters"
            :key="semester"
            :semester="semester"
        />
    </div>
</template>
<script>
// import CourseHolder from './CourseHolder.vue';
import Semester from "./Semester.vue";
export default {
    components: {
        // CourseHolder,
        Semester,
    },
    props: {
        semesters: {
            type: Object,
            default: () => {},
        },
    },
    data() {
        return {
            parsedSemesters: [],
        };
    },
};
</script>
<style>
#table {
    display: grid;
    gap: 5%;
    width: 70%;
    margin: 0 auto;
    grid-template-columns: 1fr 1fr;
}

.semesterPre {
    margin: auto auto auto 0;
}

.flex-row {
    display: flex;
    flex-flow: row wrap;
    gap: 10px;
}

.courseCard {
    width: fit-content;
}
</style>
