<script>
import { RouterView } from "vue-router";
import AHeader from "./components/AHeader.vue";
import AFooter from "./components/AFooter.vue";

export default {
    components: {
        RouterView,
        AHeader,
        AFooter,
    },
};
</script>

<template>
    <q-layout view="hHh LpR fFf">
        <AHeader />
        <q-page-container>
            <RouterView />
        </q-page-container>
        <AFooter />
    </q-layout>
</template>


<style scoped></style>
