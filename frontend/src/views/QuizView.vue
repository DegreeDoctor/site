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
    <button @click="store.addDegree()">test button</button>
    <router-link to="degree">test</router-link>
    <Footer />
</template>
