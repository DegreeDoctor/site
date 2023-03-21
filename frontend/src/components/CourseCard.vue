<template>
    <div class="card" @click="toggleCheck">
        <q-checkbox v-model="val" />
        <span class="name">{{ course.name }}</span>
        <span class="bar"></span>
        <span class="courseCode">{{ course.subject }} - {{ course.ID }}</span>
        <span class="credits">({{ course.credits[0] }})</span>
        <!--why is course.credits an array -->
        <q-btn
            push
            color="primary"
            class="info"
            padding="none"
            icon="help_outline"
            @click.stop="moreInfo"
        />
        <q-dialog v-model="showInfo" seamless class="moreInfo">
            <q-card style="width: 75vw">
                <q-card-section class="column no-wrap">
                    <div>
                        <div class="row no-wrap">
                            <h4 class="text-weight-bold" style="margin: 0">
                                {{ course.name }}
                            </h4>
                            <q-space />
                            <q-btn v-close-popup flat round icon="close" />
                        </div>

                        <div class="text-grey">
                            {{ course.subject }}-{{ course.ID }}
                        </div>
                    </div>
                    <q-separator />
                    <div>
                        <div class="text-grey">
                            {{ course.description }}
                        </div>
                        <div class="text-grey">
                            {{ offered }}
                        </div>
                    </div>
                </q-card-section>
            </q-card>
        </q-dialog>
    </div>
</template>

<script>
export default {
    props: {
        course: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            val: false, // turn this into a prop later
            showInfo: false,
        };
    },
    computed: {
        offered() {
            /*
semesters has 3 different cases to test:
    offered in all semesters       | (works)
    offered in 1-2 semesters       | (works)
    offered by profs availability  | (needs testing) COMM-4590 is a test case, not available to add though
years has 2-3(?) different cases to test:
    offered every year             | (works)
    offered every other year       | (needs testing) COMM-4590 is a test case, not available to add though
    offered by profs availability  | (needs testing) COMM-6790 - alternate years
    */
            const offered = this.course.offered;
            let out = "Offered";
            if (offered.semesters.length == 3) {
                // if its offered in all semesters just say "all semesters"
                //  instead of listing everything individually
                out += " all semesters";
            } else {
                out += " in the ";
                // concatenates all of the semesters offered
                //  adds an "and" between the last 2 semesters
                //   still needs more testing
                offered.semesters.forEach((semester, index) => {
                    out += `${semester}${
                        index != offered.semesters.length - 1 ? " and " : " "
                    }`;
                });
            }
            if (offered.year == "all") {
                // nothing, default is all years
            } else {
                out += ` in ${offered.year} years`;
            }
            return out;
        },
    },
    methods: {
        toggleCheck() {
            // emit update to parent
            this.val = !this.val;
        },
        toggleDesc() {
            this.showInfo = !this.showInfo;
        },
        moreInfo() {
            this.toggleDesc();
        },
    },
};
</script>
<style>
.card {
    display: flex;
    width: 100%;
    gap: 2px;
    cursor: move;
}
.card span {
    align-self: center;
}
.name {
    font-weight: 600;
    width: 30ch;
    /* width: 55%; */
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.bar {
    align-self: auto !important;
    background-color: white;
    width: 1px;
    flex-basis: 2px;
    border-radius: 1px;
}

.courseCode {
    width: 12ch;
}

.credits {
    /* flex-grow: 1; */
    text-align: end;
}

.info {
    padding: 0;
    aspect-ratio: 1/1;
    margin-left: auto;
}

.moreInfo {
    position: relative;
}
</style>
