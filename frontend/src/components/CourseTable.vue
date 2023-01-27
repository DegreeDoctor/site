<template>
    <div id="table">
        <div class="flex-row" v-for="semester in parsedSemesters">
            <h3 class="semesterPre">
                {{ semester[0] }}
            </h3>
            <div class="courseCard" v-for="course in semester[1]">
                <CourseHolder v-if="course.name != 'empty'"   :course="course"  />
                <CourseHolder v-else/>
            </div>
        </div>
    </div>


</template>
<script>
import CourseHolder from './CourseHolder.vue';
export default {
    components: {
        CourseHolder
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
                for ( let i = 0; i < 4; i++) {
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
    display: flex;
    flex-flow: column wrap;
    gap: 10px;
    width: fit-content;
    margin: 0 auto;
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