<template>
    <div>
        <CourseSearch
            :courses-data="coursesData"
            :prompt="showSearch"
            @close="showSearch = false"
            @add-course="addCourse"
        />
        <div id="table" :key="semesters">
            <Semester
                v-for="semester in semesters"
                :ref="semester[0]"
                :key="semester[0]"
                :semester="semester"
                @add-course="showAddCourseModal"
            />
        </div>
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
    },
    emits: ["addCourse"],
    data() {
        return {
            parsedSemesters: [],
            coursesData: coursesJson,
            showSearch: false,
            opened: null,
        };
    },
    mounted() {},
    methods: {
        showAddCourseModal(semesterName) {
            this.showSearch = true;
            this.opened = semesterName;
        },
        addCourse(course) {
            this.$emit("addCourse", [course, this.opened]);
            this.showSearch = false;
        },
    },
};
</script>
<style>
#table {
    display: grid;
    gap: 5%;
    width: 70%;
    margin: 16px auto;
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

@media (max-width: 768px) {
    #table {
        grid-template-columns: 1fr;
        width: 90%;
        gap: 2%;
    }
}
</style>
