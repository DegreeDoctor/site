<script>
import { useQuasar } from "quasar";
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            q: useQuasar(),
            darkMode: false,
            store: useStore(),
        };
    },
    created() {
        this.darkMode = this.store.getDarkMode;
        this.q.dark.set(this.darkMode);
    },
    methods: {
        darkToggle() {
            this.q.dark.toggle();
            this.store.toggleDarkMode();
        },
    },
};
</script>

<template>
    <q-toggle
        v-model="darkMode"
        unchecked-icon="clear"
        checked-icon="check"
        color="red"
        label="Dark"
        @update:model-value="darkToggle"
    />
</template>
