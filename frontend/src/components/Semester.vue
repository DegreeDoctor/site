<template>
    <div class="semesterContainer">
        <h3 class="semesterName">{{ semesterName }}</h3>
        <draggable :list="courses" group="courses" class="courseContainer" @change="log">
            <CourseCard class="course" v-for="course in courses" :course="course" />
        </draggable>
    </div>
    <!-- <draggable :list="list" >
      <div
        v-for="element in list"
        :key="element.name"
      >
        {{ element.name }}
      </div>
    </draggable> -->
</template>
<script>
import { defineComponent } from 'vue'
import { VueDraggableNext } from 'vue-draggable-next'
import CourseCard from './CourseCard.vue';

export default defineComponent ({
    components: { 
        CourseCard, 
        draggable: VueDraggableNext, 
    },
    data() {
        return {
            list: [
                { name: 'John', id: 1 },
                { name: 'Joao', id: 2 },
                { name: 'Jean', id: 3 },
                { name: 'Gerard', id: 4 },
            ],
            semesterName: {
                type: String
            },
            courses: {
                type: Array[Object]
            }

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
        this.courses = JSON.parse(JSON.stringify(this.semester[1]))
    },
    methods: {
        log(event) {
            console.log(event)
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
</style>