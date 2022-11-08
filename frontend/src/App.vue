<script>
import { RouterView } from "vue-router";
import AFooter from "./components/AFooter.vue";
import ProgressBar from "./components/ProgressBar.vue";

export default {
    components: {
        RouterView,
        AFooter,
        ProgressBar,
    },
};
</script>

<template>
    <q-layout view="hHh LpR fFf">
        <ProgressBar :circle="true" />
        <q-page-container>
            <RouterView />
        </q-page-container>
        <AFooter />
    </q-layout>
</template>

<style scoped></style>
