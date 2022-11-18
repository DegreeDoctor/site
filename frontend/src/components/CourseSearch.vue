<script>
import coursesJson from "../data/courses.json";
import ACourse from "../components/ACourse.vue";

export default {
    components: {
        ACourse,
    },
    props: {
        coursesData: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            course: null,
        };
    },
};
</script>

<template>
    <div>test!</div>
</template>
