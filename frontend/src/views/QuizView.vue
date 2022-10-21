<script>
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            store: useStore(),
        };
    },
};
</script>

<template>
    <q-form action="https://some-url.com" method="post">
    <q-select filled v-model="model" use-input use-chips multiple input-debounce="0" @new-value="createValue"
            :options="filterOptions" @filter="filterFn" style="width: 250px" />
    </q-form>
</template>
