<script>
import { RouterView } from "vue-router";
import AHeader from "./components/AHeader.vue";

export default {
    components: {
        RouterView,
        AHeader,
    },
};
</script>

<template>
    <q-layout view="hHh LpR fFf">
        <AHeader />
        <q-page-container>
            <RouterView />
        </q-page-container>
    </q-layout>
</template>

<style scoped></style>
