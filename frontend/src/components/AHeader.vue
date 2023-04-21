<script>
import DarkModeToggle from "./DarkModeToggle.vue";
import PlansList from "./PlansList.vue";

export default {
    components: {
        DarkModeToggle,
        PlansList,
    },
    methods: {
        sendQuiz() {
            this.$router.push("/quiz");
        },
    },
};
</script>

<template>
    <q-header elevated class="bg-secondary text-white header" height-hint="98">
        <q-toolbar>
            <q-toolbar-title>
                <q-avatar @click="sendQuiz()">
                    <img src="../assets/Degree_Doctor_logo.png" />
                </q-avatar>
                <a @click="sendQuiz()" class="name"> Degree Doctor</a>
            </q-toolbar-title>

            <PlansList />
            <DarkModeToggle />
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
.header {
    display: flex;
    justify-content: center;
    align-items: center;
    max-height: 54px;
    height: 100%;
}

@media (max-width: 600px) {
    .name { 
        display: none;
    }
}

</style>
