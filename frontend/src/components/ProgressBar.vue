<script>
import { useStore } from "../stores/store";

export default {
    name: 'ProgressBar',
    data() {
        return {
            store: useStore(),
        }
    },
    computed: {
        percent() {
            let p = this.store.getCredits;
            return p / 128;
        }
    }
}
</script>

<template>
    <q-circular-progress
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