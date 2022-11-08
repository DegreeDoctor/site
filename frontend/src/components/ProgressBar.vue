<script>
export default {
    name: 'ProgressBar',
    props: {
        circle: {
            type: Boolean,
            required: true,
        },
    },
    data () {
        return {
            percent: 50,
        }
    }
}
</script>

<template>
    <q-circular-progress
        v-if = "circle"
        show-value
        font-size="12px"
        :value="percent"
        size="50px"
        :thickness="0.22"
        color="teal"
        track-color="grey-3"
        class="q-ma-md"
    >
    {{ percent }}%
    </q-circular-progress>

</template>