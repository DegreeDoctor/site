<template>
    <div id="table">
        <Semester v-for="semester in semesters" :semester="semester" />
    </div>


</template>
<script>
import CourseHolder from './CourseHolder.vue';
import Semester from './Semester.vue';
export default {
    components: {
    CourseHolder,
    Semester
},  
    data() {
        return {
            parsedSemesters: []
        }
    },  
    props: {
        semesters: {
            type: Object,
            
        }
    },
    mounted() {
        console.log(this.semesters)
        // parse semesters and make them default to length of 4
        this.parseSemesters();
        console.log(this.parsedSemesters)
    },
    methods: {
        parseSemesters() {
            this.parsedSemesters = []
            this.semesters.forEach( sem => {
                let tempSem = [ sem[0], []]
                for ( let i = 0; i < 4 ; i++) {
                    if (i < sem[1].length ) {
                        tempSem[1].push(JSON.parse(JSON.stringify(sem[1][i])))
                    } else {
                        tempSem[1].push({name:"empty"})
                    }
                }
                this.parsedSemesters.push(tempSem)
            })
        }
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