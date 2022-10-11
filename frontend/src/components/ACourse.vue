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
            currCredit: this.course.credits[0]
        };
    },
    mounted() {
        const creds = this.store.fetchCredits(this.course.name);
        this.checked = !!creds;
        if(this.checked) {
            this.currCredit = creds;
        }
    },
    computed: {
        offeredParse() {
            let text = "Offered ";
            if(this.course.offered.year == "uia") {
                text += "on availability of instructor."
            }
            else {
                if(this.course.offered.year != "all") {
                    text += " during " + this.course.offered.year + " years";
                }
                text += " in the ";
                if(this.course.offered.semesters.length == 1) {
                    text += this.course.offered.semesters[0] + ".";
                }
                else if(this.course.offered.semesters.length == 2) {
                    text += this.course.offered.semesters[0] + " and " + this.course.offered.semesters[1] + ".";
                }
                else {
                    text += this.course.offered.semesters[0] + ", " + this.course.offered.semesters[1] + ", and " + this.course.offered.semesters[2] + ".";
                }
            }
            return text;
        },
        propertiesParse() {
            let text = "";
            if(this.course.properties.CI) {
                text += "Communication Intensive";
            }
            if(this.course.properties.MR) {
                if(text.length > 0) text += " and ";
                text += "Major Restricted";
            }
            if(text.length > 0) text += ".";
            return text;
        },
        crosslistedParse() {
            let text = this.course.subject + "-" + this.course.ID;
            for(const subj in this.course.crosslisted) {
                text += "/" + subj + "-" + this.course.crosslisted[subj];
            }
            return text;
        },
        fixName() {
            let name = this.course.name;
            if(name.length > 16) {
                name = name.substring(0, 14).trimEnd() + "...";
            }
            return name;
        }
    },
    methods: {
        checkClicked(value) {
            if (value) {
                this.store.addCredits(this.course.name, this.currCredit);
            } else {
                this.store.removeCredits(this.course.name);
            }
        },
        updateCredits(c) {
            if(this.checked) {
                this.store.changeCredits(this.course.name, c);
            }
            this.currCredit = c;
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
    >   
        <q-card-section horizontal @click.self="popup = true">
            <q-card-section class="text-subtitle1" @click.self="popup = true">
                {{ fixName }}
                <q-separator />
                {{ course.subject + "-" + course.ID }}
            </q-card-section>
            <q-card-section vertical class="q-py-sm" @click.self="popup = true">
                <q-btn color="secondary" dense :label="currCredit" class="q-px-md">
                    <q-menu>
                        <q-list auto-close dense>
                            <q-item
                                v-for="c in course.credits"
                                v-close-popup
                                clickable
                                @click="updateCredits(c)"
                            >
                                <q-item-label>{{ c }}</q-item-label>
                            </q-item>
                        </q-list>
                    </q-menu>
                </q-btn>
                <q-separator />
                <q-checkbox
                    v-model="checked"
                    color="secondary"
                    @update:model-value="(value) => checkClicked(value)"
                />
            </q-card-section>
        </q-card-section>
    </q-card>
    <q-dialog v-model="popup">
        <q-card>
            <q-card-section class="row items-center q-pb-none">
                <div class="text-h5"> {{ course.name }} </div>
                <q-space />
                <q-btn 
                    v-close-popup 
                    icon="close" 
                    flat
                    round 
                    dense 
                />
            </q-card-section>
            <q-card-section class="q-pt-none">
                <div class="text-body1">
                    {{ crosslistedParse }}
                    <q-separator />     
                    {{ course.description }}
                    <q-separator /> 
                    <q-space />
                    {{ propertiesParse }}
                    <q-space />
                    {{ offeredParse }}
                    <q-separator />
                </div>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<style scoped lang="scss">
.course-card {
    max-width: 300px;
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
