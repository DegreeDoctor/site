<script>
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            store: useStore(),
        };
    }
};
</script>

<template>
    <router-link to="quiz">test</router-link>
</template>
