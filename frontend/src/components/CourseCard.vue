<template>
    <div class="card">
        <q-checkbox v-model="val" />
        <span class="name">{{ course.name }}</span>
        <span class="bar"></span>
        <span class="courseCode">{{ course.subject }} - {{ course.ID }}</span>
        <span class="credits">({{ course.credits[0] }})</span>  <!--why is course.credits an array -->
        <q-btn push color="primary" class="info" padding="none" icon="help_outline" />
        <!-- <q-icon icon="help_outline"/> -->
        <!-- <i>help</i> -->
        <!-- <span icon="help"></span> -->
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
    cursor: move;
}
.card span {
    align-self: center;
}
.name {
    font-weight: 600;
    width: 30ch;
    /* width: 55%; */
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

.courseCode {
    width: 11ch;
}

.credits {
    /* flex-grow: 1; */
    text-align: end;
}

.info {
    padding: 0;
    aspect-ratio: 1/1;
    margin-left: auto;
}
</style>
