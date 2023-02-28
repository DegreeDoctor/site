<template>
    <div class="card">
        <q-checkbox v-model="val" />
        <span class="name">{{ course.name }}</span>
        <span class="bar"></span>
        <span class="courseCode">{{ course.subject }} - {{ course.ID }}</span>
        <span class="credits">({{ course.credits[0] }})</span>
        <!--why is course.credits an array -->
    </div>
</template>

<script>
export default {
    props: {
        course: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            val: false, // turn this into a prop later
        };
    },
};
</script>
<style>
.card {
    display: flex;
    width: 100%;
    gap: 2px;
}
.card span {
    align-self: center;
}
.name {
    font-weight: 600;
    width: 55%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.bar {
    align-self: auto !important;
    background-color: white;
    width: 1px;
    flex-basis: 2px;
    border-radius: 1px;
}

.credits {
    flex-grow: 1;
    text-align: end;
}
</style>
