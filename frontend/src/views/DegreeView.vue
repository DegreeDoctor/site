<script>
import { useStore } from "../stores/store";
import CourseHolder from "../components/CourseHolder.vue";
import CourseTrash from "../components/CourseTrash.vue";
import CourseSearch from "../components/CourseSearch.vue";
import coursesJson from "../data/courses.json";

export default {
    components: {
        CourseHolder,
        CourseTrash,
        CourseSearch,
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
};
</script>

<template>
    <CourseSearch :courses-data="coursesData" />
    <CourseTrash />
    <q-markup-table separator="cell" flat bordered>
        <tbody>
            <tr v-for="sem in templateToArray" :key="sem">
                <td>
                    <h4 class="q-ma-none">{{ sem[0] }}</h4>
                </td>
                <td>
                    <tr>
                        <td v-for="course in sem[1]" :key="course" class="col">
                            Recommended: {{ course.name }}
                        </td>
                    </tr>
                    <!-- Course Row -->
                    <tr>
                        <td v-for="course in sem[1]" :key="course" class="col">
                            <CourseHolder :course="course" />
                        </td>
                    </tr>
                </td>
            </tr>
        </tbody>
    </q-markup-table>
</template>

<style scoped lang="scss">
.col {
    max-width: 320px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
