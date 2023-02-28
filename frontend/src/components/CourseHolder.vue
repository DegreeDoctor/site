<script>
import { useStore } from "../stores/store";
import ACourse from "./ACourse.vue";
import coursesJson from "../data/courses.json";
import CourseSearch from "./CourseSearch.vue";

export default {
    components: {
        ACourse,
        CourseSearch,
    },
    props: {
        course: {
            type: Object,
            required: false,
            default: null,
        },
    },
    data() {
        return {
            store: useStore(),
            coursesData: coursesJson,
        };
    },
    methods: {
        courseIn(e) {
            if (e.target.draggable !== true) {
                e.target.classList.add("drag-enter");
            }
        },
        courseOut(e) {
            e.target.classList.remove("drag-enter");
        },
        courseDrag(e) {
            e.preventDefault();
        },
        courseDrop(e) {
            e.preventDefault();

            // don't drop on other draggables
            if (e.target.draggable === true || e.target.children.length != 0) {
                e.target.classList.remove("drag-enter");
                return;
            }

            const draggedId = e.dataTransfer.getData("text");
            const draggedEl = document.getElementById(draggedId);

            // check if original parent node
            if (draggedEl.parentNode === e.target) {
                e.target.classList.remove("drag-enter");
                return;
            }

            // make the exchange
            //draggedEl.parentNode <-- curr
            //e.target <-- moving to
            draggedEl.parentNode.removeChild(draggedEl);
            e.target.appendChild(draggedEl);
            e.target.classList.remove("drag-enter");
        },
    },
};
</script>

<template>
    <div
        class="holder"
        @dragenter="courseIn"
        @dragleave="courseOut"
        @dragover="courseDrag"
        @drop="courseDrop"
    >
        <ACourse v-if="course" :course="course" :check="true" />
        <CourseSearch v-else :courses-data="coursesData" />
    </div>
</template>

<style scoped lang="scss">
.holder {
    height: 100px;
    width: 310px;
    background-color: darken($secondary, 15%);
}

.drag-enter {
    outline-style: dashed;
}
</style>
