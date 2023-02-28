<template>
    <q-btn @click="debug()">
        debug
    </q-btn>
    <CourseSearch :coursesData="coursesData" :prompt="showSearch" @close="debugTest()"/>
    <div id="table">
        <Semester v-for="semester in semesters" :ref=semester[0] :semester="semester" @addCourse="showAddCourseModal"/>
    </div>
</template>
<script>
import CourseHolder from './CourseHolder.vue';
import Semester from './Semester.vue';
import coursesJson from '../data/courses.json';
import CourseSearch from './CourseSearch.vue';

export default {
    components: {
    CourseHolder,
    Semester,
    CourseSearch
},  
    data() {
        return {
            parsedSemesters: [],
            coursesData: coursesJson,
            showSearch: false,
        }
    },  
    props: {
        semesters: {
            type: Object,
            
        }
    },
    methods: {
        showAddCourseModal(semesterName) {
            this.showSearch = true;
            // this.$refs[course.se]
            console.log(this.$refs[semesterName])
            // this.$emit('addCourse', course);
        },
        debug() {
            console.log(this.showSearch)
        },
        debugTest() {
            this.showSearch = false;
        }
    },
    mounted() {
        console.log(this.$refs)
    }
    
}
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