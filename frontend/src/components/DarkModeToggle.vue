<script>
import { useQuasar } from 'quasar';

export default {
    data() {
        return {
            q: useQuasar(),
            darkMode: useQuasar().dark.isActive
        }
    },
    methods: {
        darkToggle() {
            this.q.dark.toggle()
        }
    }
}
</script>

<template>
    <q-toggle
        v-model="darkMode"
        unchecked-icon="clear"
        checked-icon="check"
        color="red"
        label="Light Switch"
        @update:model-value="darkToggle"
    />
</template>