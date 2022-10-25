<script>
import { useStore } from "../stores/store";
import DarkModeToggle from "./DarkModeToggle.vue";

export default {
    components: {
        DarkModeToggle,
    },
    data() {
        return {
            plan: false,
            current: "CS Plan",
            plans: ["CS Plan", "ITWS Plan", "HASS Plan"],
        };
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

            <div class="q-pa-md">
                <q-btn
                    no-caps
                    label="My Plans"
                    color="primary"
                    @click="plan = true"
                ></q-btn>
                <q-dialog v-model="plan">
                    <q-card style="min-width: 350px">
                        <q-card-section>
                            <div class="text-h6">Pick a plan</div>
                        </q-card-section>

                        <q-card-section class="q-pt-none">
                            <h6 class="q-ma-none">
                                Current Plan: {{ current }}
                            </h6>
                            <q-select
                                filled
                                v-model="current"
                                use-input
                                input-debounce="0"
                                label="Simple filter"
                                :options="plans"
                                style="width: 200px"
                                behavior="menu"
                            >
                                <template v-slot:no-option>
                                    <q-item>
                                        <q-item-section class="text-grey">
                                            No results
                                        </q-item-section>
                                    </q-item>
                                </template>
                            </q-select>
                        </q-card-section>

                        <q-card-actions class="text-primary">
                            <q-btn flat label="Cancel" v-close-popup></q-btn>
                            <q-btn
                                flat
                                label="Add new plan"
                                to="/quiz"
                                v-close-popup
                            ></q-btn>
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
