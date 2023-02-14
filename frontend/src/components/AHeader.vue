<script>
import { useStore } from "../stores/store";
import DarkModeToggle from "./DarkModeToggle.vue";
import ProgressBar from "./ProgressBar.vue";
import PlansList from "./PlansList.vue";

export default {
    components: {
        DarkModeToggle,
        ProgressBar,
        PlansList,
    },
};
</script>

<template>
    <q-header elevated class="bg-secondary text-white" height-hint="98">
        <q-toolbar>
            <q-toolbar-title>
                <q-avatar>
                    <img src="../assets/Degree_Doctor_logo.png" />
                </q-avatar>
                Degree Doctor
            </q-toolbar-title>

            <DarkModeToggle />
            <PlansList />
        </q-toolbar>
    </q-header>
</template>

<style scoped>
.card-contain {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding-right: 1em;
}
</style>
