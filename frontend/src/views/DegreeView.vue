<script>
import { useStore } from "../stores/store";
import ACourse from "../components/ACourse.vue";
import CourseHolder from "../components/CourseHolder.vue";
import CourseTrash from "../components/CourseTrash.vue";
import coursesJson from "../data/courses.json";

export default {
    components: {
        ACourse,
        CourseHolder,
        CourseTrash
    },
    data() {
        return {
            store: useStore(),
            coursesData: coursesJson,
            tst: false
        };
    },
    computed: {
        templateToArray() {
            const template = this.store.getCurrentDegree["template"];
            let array = [];
            let subArray = [];
            let year = template[0];
            for(const name in template) {
                if(name != year) {
                    array.push([year, subArray]);
                    year = name;
                    subArray = [];
                }
                for(const i in template[name]) {
                    if(this.coursesData) {
                        if(this.coursesData[template[name][i]]) {
                            subArray.push(this.coursesData[template[name][i]]);
                        }
                    }
                    subArray.push();
                }
            }
            return array;
        }
    }
};
</script>

<template>
    <CourseTrash />
    <q-markup-table separator="cell" flat bordered>
        <tbody>
            <tr v-for="year in templateToArray">
                <h4 class="q-ma-none"> {{ year[0] }} </h4>
                <!-- Label row -->
                <tr>
                    <td v-for="course in year[1]" class="col">
                        Recommended: {{ course.name }}
                    </td>
                </tr>
                <!-- Course Row -->
                <tr>
                    <td v-for="course in year[1]" class="col">
                        <CourseHolder :course="course" />
                    </td>
                </tr>
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