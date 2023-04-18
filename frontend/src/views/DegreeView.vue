<template>
    <!-- the semesters prop is all of the degree data - what courses at which semesters -->
    <!-- the credits prop keeps track of which course has been selected which in turn lets the progress bar work -->
    <!-- the add-course event is when a course had been added through the add course dialog -->
    <CourseTable 
        :semesters="templateToArray" 
        :credits="credits" 
        @add-course="addCourse" 
    />
</template>

<script>
import { useStore } from "../stores/store";
import CourseTable from "../components/CourseTable.vue";

export default {
    components: {
        CourseTable,
    },
    data() {
        return {
            store: useStore(),
        };
    },
    computed: {
        templateToArray() {
            return this.store.templateToArray;
        },
        credits() {
            return this.store.getCredits;
        }
    },
    methods: {
        // this is the function that handles when a course is added through the dialog in CourseTable.vue
        // it updates the degree in local storage, adding the course name to the selected semester
        // both the semester and course name are passed through the event through the data variable
        //  e.g. [ {...name="Computer Science 1"}, "1-Fall"]
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
