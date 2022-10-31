<script>
import { useStore } from "../stores/store";
import ACourse from "../components/ACourse.vue";
import CourseHolder from "../components/CourseHolder.vue";

export default {
    components: {
        ACourse,
        CourseHolder
    },
    data() {
        return {
            store: useStore(),
            coursesData: null
        };
    },
    created() {
        import('../data/courses.json').then((val) => this.coursesData = Object.freeze(val));
    },
    computed: {
        templateToArray() {
            const template = this.store.getCurrentDegree;
            const array = [];
            const subArray = [];
            let year = "1";
            for(const name in template) {
                if(name[0] == year) {
                    subArray.push(template[name]);
                }
                else {
                    array.push(subArray);
                    year = name[0];
                    subArray = [];
                }
            }
            
            return array;
        }
    }
};
</script>

<template>
    <!-- <ACourse :course="crs" />
    <CourseHolder />
    <CourseHolder /> -->
</template>
