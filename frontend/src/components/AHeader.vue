<script>
import { useStore } from "../stores/store";

export default {

}
</script>

<template>
    <q-header elevated class="bg-secondary text-white" height-hint="98">
        <q-toolbar>
        <q-toolbar-title>
            <q-avatar>
                <img src="../assets/Degree_Doctor_logo.png">
            </q-avatar>
            Degree Doctor
        </q-toolbar-title>

    <div class="q-pa-md q-gutter-sm">
        <q-btn label="Prompt" color="primary" @click="prompt = true"></q-btn>
        <q-dialog v-model="prompt" persistent>
            <q-card style="min-width: 350px">
            <q-card-section>
                <div class="text-h6">Your address</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
                <q-input dense v-model="address" autofocus @keyup.enter="prompt = false"></q-input>
            </q-card-section>

            <q-card-actions class="text-primary">
                <q-btn flat label="Cancel" v-close-popup></q-btn>
                <q-btn flat label="Add address" v-close-popup></q-btn>
            </q-card-actions>
            </q-card>
        </q-dialog>
    </div>
        </q-toolbar>
    </q-header>
</template>
<!-- 
Icon, left most
light mode switch, right
popup button, right of switch
-->