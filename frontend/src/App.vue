<script>
import { RouterView } from "vue-router";
import AFooter from "./components/AFooter.vue";

export default {
    components: {
        RouterView,
        AFooter,
    },
};
</script>

<template>
    <q-layout view="hHh LpR fFf">
        <q-page-container>
            <RouterView />
        </q-page-container>

        <AFooter />

    </q-layout>
</template>

<style scoped></style>
