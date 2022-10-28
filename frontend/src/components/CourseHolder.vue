<script>
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            store: useStore(),
            course: null
        }
    },
    methods: {
        courseIn(e) {
            if (e.target.draggable !== true) {
              e.target.classList.add('drag-enter');
            }
        },
        courseOut(e) {
            e.target.classList.remove('drag-enter');
        },
        courseDrag(e) {
            e.preventDefault();
        },
        courseDrop(e) {
            e.preventDefault();

            // don't drop on other draggables
            if (e.target.draggable === true) {
              return;
            }

            const draggedId = e.dataTransfer.getData('text');
            const draggedEl = document.getElementById(draggedId);

            // check if original parent node
            if (draggedEl.parentNode === e.target) {
              e.target.classList.remove('drag-enter');
              return;
            }

            // make the exchange
            draggedEl.parentNode.removeChild(draggedEl);
            e.target.appendChild(draggedEl);
            e.target.classList.remove('drag-enter');
        }
    }
}
</script>

<template>
    <div
        class="holder"
        @dragenter="courseIn"
        @dragleave="courseOut"
        @dragover="courseDrag"
        @drop="courseDrop"
    />
</template>

<style scoped lang="scss">
    .holder {
        height: 100px;
        width:  310px;
        background-color: darken($secondary, 15%)
    }

    .drag-enter{
        outline-style: dashed
    }
</style>