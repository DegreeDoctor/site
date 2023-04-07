<template>
    <!-- <q-btn @click="debug()">
        debug
    </q-btn> -->
    <br />
    <CourseTable :semesters="templateToArray" @add-course="addCourse" />
    <br />
    <DegreeChecker/>
</template>

<script>
import { useStore } from "../stores/store";
import coursesJson from "../data/courses.json";
import CourseTable from "../components/CourseTable.vue";
import DegreeChecker from "../components/DegreeChecker.vue";

export default {
    components: {
        CourseTable,
        DegreeChecker,
    },
    data() {
        return {
            store: useStore(),
            coursesData: coursesJson,
            tst: false,
            test: null,
        };
    },
    computed: {
        templateToArray() {
            return this.store.templateToArray;
        },
    },
    mounted() {},
    methods: {
        // debug() {
        //     // this.store.deleteEverything();       // this deleted everything in local store
        //     console.log(this.templateToArray)
        // },
        addCourse(data) {
            const courseObj = data[0];
            const semesterName = data[1];
            this.store.updateDegreeSemester(
                semesterName,
                courseObj.name,
                "add"
            );
        },
    },
};
</script>

<style scoped lang="scss">
CourseTable {
    margin: 0 auto;
}
</style>
