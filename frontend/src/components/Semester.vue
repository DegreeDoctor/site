<template>
    <div class="semesterContainer">
        <h3 class="semesterName">{{ semester[0] }}</h3>
        <draggable :list="courseList" group="courses" class="courseContainer" @change="log">
            <CourseCard class="course" v-for="course in courseList" :key=course.name :course="course" />
        </draggable>
        <q-btn push color="secondary" class="addButton" icon="add"  />
    </div>
</template>
<script>
import { useStore } from "../stores/store";
import { defineComponent, toRaw } from 'vue'
import { VueDraggableNext } from 'vue-draggable-next'
import CourseCard from './CourseCard.vue';

export default defineComponent ({
    components: { 
        CourseCard, 
        draggable: VueDraggableNext, 
    },
    data() {
        return {
            store: useStore(),
            semesterName: {
                type: String
            },
            courseList: [
                {
                    "ID": "1100",
                    "credits": [
                        4
                    ],
                    "crosslisted": {},
                    "description": "An introduction to computer programming algorithm design and analysis Additional topics include basic computer organization internal representation of scalar and array data use of topdown design and subprograms to tackle complex problems abstract data types Enrichment material as time allows Interdisciplinary case studies numerical and nonnumerical applications Students who have passed CSCI 1200 cannot register for this course",
                    "name": "Computer Science I",
                    "offered": {
                        "semesters": [
                            "fall",
                            "spring",
                            "summer"
                        ],
                        "year": "all"
                    },
                    "prerequisites": [],
                    "professors": [],
                    "properties": {
                        "CI": false,
                        "MR": false
                    },
                    "subject": "CSCI"
                },
                {
                    "ID": "1010",
                    "credits": [
                        4
                    ],
                    "crosslisted": {},
                    "description": "Functions limits continuity derivatives implicit differentiation related rates maxima and minima elementary transcendental functions introduction to definite integral with applications to area and volumes of revolution Students cannot get credit for both MATH 1010 and MATH 1500",
                    "name": "Calculus I",
                    "offered": {
                        "semesters": [
                            "fall",
                            "spring"
                        ],
                        "year": "all"
                    },
                    "prerequisites": [],
                    "professors": [],
                    "properties": {
                        "CI": false,
                        "MR": false
                    },
                    "subject": "MATH"
                },
                {
                    "ID": "1100",
                    "credits": [
                        4
                    ],
                    "crosslisted": {},
                    "description": "The first semester of a twosemester sequence of interactive courses Topics include linear and angular kinematics and dynamics work and energy momentum and collisions forces and fields gravitation oscillatory motion waves sound and interference",
                    "name": "Physics I",
                    "offered": {
                        "semesters": [
                            "fall",
                            "spring"
                        ],
                        "year": "all"
                    },
                    "prerequisites": {
                        "one_of": [
                            [
                                "MATH-1010",
                                "PHYS-1050"
                            ]
                        ],
                        "required": [
                            "PHYS-1100"
                        ]
                    },
                    "professors": [],
                    "properties": {
                        "CI": false,
                        "MR": false
                    },
                    "subject": "PHYS"
                }
            ]
        }
    },
    props: {
        semester: {
            type: Object,
            required: true,
        },
    },
    mounted() {
        this.semesterName = this.semester[0];
        this.courseList = []
        for (let course of this.semester[1]) {
            this.courseList.push(toRaw(course))
        }
        console.log(this.store.getCurrentDegree)
    },
    methods: {
        debug() {
            console.log(this.semesterName)
            console.log(toRaw(this.courseList))
        },
        log(event) {
            // <!--! this is not reactive right now, still have to change that
                // <!--! it does update the store (i think), but it doesn't update the view
                    // <!--! need to look at the docs for pinia more to fix this
            console.log(event)
            if (event["added"]) {
                this.store.updateDegreeSemester(this.semesterName, event.added.element, "add")
            }
            // this.store.updateDegreeSemester(this.semesterName, toRaw(this.courseList))
            // console.log(this.store.getCurrentDegree)
        },
        addCoursetoStore(event) {
            console.log(event)
            // this.store.updateDegreeSemester(this.semesterName, this.courseList, "add")
        },
        removeCourseFromStore(event) {

        }
    }
})
</script>
<style lang="scss">
    .semesterName {
        text-align: center;
        font-size: 1.5rem;
        font-weight: 600;
        margin: 0;
        width: 100%;
        background-color: white;
    }


    .semesterContainer {
        border: 1px solid black;
        background-color: #D9D9D9;
        min-width: 100%;
        display: flex;
        flex-direction: column;
    }

    .courseContainer {
        margin: 5% 0;
        display: flex;
        flex-flow: column wrap;
        align-content: center;
        gap: 5px;
    }

    .card {
        max-width: 70%;
        background-color: darken($secondary, 15%);
        box-sizing: border-box;
        padding: 5px;
        border-radius: 5px;
        color: white;
    }

    .addButton {
        margin: auto 5px 5px auto;
    }
</style>