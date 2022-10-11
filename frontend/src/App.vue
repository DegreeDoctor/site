<script>
import { RouterView } from "vue-router";

export default {
    components: {
        RouterView,
    }
}
</script>

<template>
    <q-layout view="hHh LpR fFf">
        <q-page-container>
            <RouterView />
        </q-page-container>


    </q-layout>
</template>

<style scoped></style>
