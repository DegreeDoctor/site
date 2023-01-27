<script>
import { useStore } from "../stores/store";
import CourseHolder from "../components/CourseHolder.vue";
import CourseTrash from "../components/CourseTrash.vue";
import CourseSearch from "../components/CourseSearch.vue";
import coursesJson from "../data/courses.json";
import CourseTable from "../components/CourseTable.vue"

export default {
    components: {
        CourseHolder,
        CourseTrash,
        CourseSearch,
        CourseTable
    },
    data() {
        return {
            store: useStore(),
            coursesData: coursesJson,
            tst: false,
        };
    },
    computed: {
        templateToArray() {
            const template = this.store.getCurrentDegree["template"];
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
                    if (this.coursesData) {
                        if (this.coursesData[template[name][i]]) {
                            subArray.push(this.coursesData[template[name][i]]);
                        }
                    }
                    subArray.push();
                }
            }
            return array;
        },
    },
    methods: {
        debug() {
            // this.store.deleteEverything();       // this deleted everything in local store
            console.log(this.templateToArray)
        }
    }
};
</script>

<template>
    <q-btn @click="debug()">
        debug
    </q-btn>
    <br/>
    <CourseTrash />
    <CourseTable :semesters="templateToArray"/>
</template>

<style scoped lang="scss">


CourseTable {
    margin: 0 auto;
}
</style>
