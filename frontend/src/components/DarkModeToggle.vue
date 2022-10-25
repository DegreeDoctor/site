<template>
    <q-toggle
        v-model="darkMode"
        checked-icon="check"
        color="red"
        label="Light Switch"
        unchecked-icon="clear"
    />
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    setup() {
        const darkMode = ref(false)
        return {
            darkMode
        }
    }
})
</script>