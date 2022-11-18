<script>
export default {
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
            if (e.target.draggable === true || e.target.children.length != 0) {
              e.target.classList.remove('drag-enter');
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
            e.target.classList.remove('drag-enter');
        }
    }
}
</script>

<template>
    <q-avatar 
        rounded 
        size="100px" 
        font-size="82px" 
        color="primary" 
        text-color="red" 
        icon="fa-solid fa-trash"
        @dragenter="courseIn"
        @dragleave="courseOut"
        @dragover="courseDrag"
        @drop="courseDrop"
    />
</template>