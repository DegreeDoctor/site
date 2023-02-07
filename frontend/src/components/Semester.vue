<template>
    <div class="semesterContainer">
        <h3 class="semesterName">{{ semester[0] }}</h3>
        <div class="courseContainer">
            <CourseCard class="course" v-for="course in semester[1]" :course="course" />
        </div>
    </div>
</template>
<script>
import CourseCard from './CourseCard.vue';

export default {
    props: {
        semester: {
            type: Object,
            required: true,
        },
    },
    components: { CourseCard }
}
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