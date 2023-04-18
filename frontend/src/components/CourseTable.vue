<template>
    <!-- the course search component hsa been moved to the entire course table as to save resources -->
    <!-- and shows itself when any of the add course buttons are clicked                            -->
    <!-- courses-data is just the json file of all of the course information                        -->
    <!-- prompt handles whether or not a the add course dialog is visible or not                    -->
    <CourseSearch
        :courses-data="coursesData"
        :prompt="showSearch"
        @close="showSearch = false"
        @add-course="addCourse"
    />
    <!-- the degree is organized by semesters, and each semester has a number of courses -->
    <div id="table" :key="semesters">
        <!-- semester prop contains course information for the specific semester -->
        <!-- credits prop contains information on what courses have been marked as completed -->
        <!-- the add-course event is when the add course button has been clicked -->
        <Semester
            v-for="semester in semesters"
            :key="semester[0]"
            :semester="semester"
            :credits="credits"
            @add-course="showAddCourseModal"
        />
    </div>
</template>

<script>
import Semester from "./Semester.vue";
import coursesJson from "../data/courses.json";
import CourseSearch from "./CourseSearch.vue";

export default {
    components: {
        Semester,
        CourseSearch,
    },
    props: {
        semesters: {
            type: Object,
            default: null,
        },
        credits: {
            type: Object,
            default: null,
        }
    },
    emits: ["addCourse"],
    data() {
        return {
            // this is the json file that has been imported that contains all course data
            coursesData: coursesJson,
            // this keeps track of if the add course dialog has been opened or not
            showSearch: false,
            // this stores the name of the semester that a course wants to be added to
            opened: "",
        };
    },
    methods: {
        showAddCourseModal(semesterName) {
            this.showSearch = true;
            this.opened = semesterName;
        },
        addCourse(course) {
            this.$emit("addCourse", [course, this.opened]);
            this.showSearch = false;
            this.opened = "";
        },
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
