<script>
import { useStore } from "../stores/store";

export default {
    props: {
        course: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            store: useStore(),
            checked: false,
            popup: false,
        };
    },
    methods: {
        checkClicked(value) {
            if (value) {
                this.store.changeCredits(this.course.credits);
            } else {
                this.store.changeCredits(-this.course.credits);
            }
        },
    },
};
</script>

<template>
    <q-card
        flat
        bordered
        class="course-card"
        color="primary"
        @click="popup = true"
    >   
        <q-card-section horizontal>
            <q-card-section class="text-subtitle1">
                {{ course.name }}
                <q-separator />
                {{ course.subject + "-" + course.ID }}
            </q-card-section>
            <q-checkbox
                v-model="checked"
                color="secondary"
                @update:model-value="(value) => checkClicked(value)"
            />
            <q-card-section>
                <q-badge color="secondary" class="credits" rounded floating>
                    {{ course.credits }}
                </q-badge>
            </q-card-section>
        </q-card-section>
    </q-card>
    <q-dialog v-model="popup">
        <q-card>
            <q-card-section class="row items-center q-pb-none">
                {{ course.name }}
                <q-space />
                <q-btn 
                    v-close-popup 
                    icon="close" 
                    flat
                    round 
                    dense 
                />
            </q-card-section>
            <q-card-section>
                test
                <q-separator />
                {{ course.description }}
                <q-separator />
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<style scoped lang="scss">
.course-card {
    width: fit-content;
    background-color: $primary
}

.course-card:hover {
    background-color: lighten($primary, 2%);
}

.credits {
    color: #000;
}
</style>
