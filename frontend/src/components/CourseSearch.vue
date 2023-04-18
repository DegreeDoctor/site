<script>
import CourseCard from "./CourseCard.vue";

export default {
    components: {
        CourseCard,
    },
    props: {
        coursesData: {
            type: Object,
            required: true,
        },
        prompt: {
            type: Boolean,
            default: false,
        },
    },
    emits: ["close", "addCourse"],
    data() {
        return {
            course: null,
            search: "",
            subject: "",
            code: "",
            chosen: [],
            options: [
                {
                    label: "Fall",
                    value: "fall",
                },
                {
                    label: "Spring",
                    value: "spring",
                },
                {
                    label: "Summer",
                    value: "summer",
                },
                {
                    label: "Communication Intensive",
                    value: "CI",
                },
                {
                    label: "4000 Level",
                    value: "4 LVL",
                },
            ],
            advancedSearch: false,
        };
    },
    computed: {
        filterIcon() {
            return this.advancedSearch ? "expand_less" : "expand_more";
        },
        showPrompt() {
            return this.prompt;
        },
        filteredCourses() {
            const courses = Object.values(this.coursesData);
            let output = [];
            for (const i in courses) {
                const course = courses[i];
                if (
                    !course.name
                        .toLowerCase()
                        .includes(this.search.toLowerCase())
                ) {
                    continue;
                }
                if (
                    !course.subject
                        .toLowerCase()
                        .includes(this.subject.toLowerCase())
                ) {
                    continue;
                }
                if (
                    !course.ID.toLowerCase().includes(this.code.toLowerCase())
                ) {
                    continue;
                }
                const fall = this.chosen.includes("fall");
                if (fall) {
                    if (!course.offered.semesters.includes("fall")) {
                        continue;
                    }
                }
                const spring = this.chosen.includes("spring");
                if (spring) {
                    if (!course.offered.semesters.includes("spring")) {
                        continue;
                    }
                }
                const summer = this.chosen.includes("summer");
                if (summer) {
                    if (!course.offered.semesters.includes("summer")) {
                        continue;
                    }
                }
                const CI = this.chosen.includes("CI");
                if (CI) {
                    if (!course.properties.CI) {
                        continue;
                    }
                }
                const LVL4 = this.chosen.includes("4 LVL");
                if (LVL4) {
                    if (!(course.ID[0] == "4")) {
                        continue;
                    }
                }
                output.push(course);
            }
            return output;
        },
    },
    methods: {
        addCourse(course) {
            this.$emit("addCourse", course);
        },
        close() {
            this.$emit("close");
        },
        debug() {
            console.log(this.prompt);
        },
        toggleAdvancedSearch() {
            this.advancedSearch = !this.advancedSearch;
        },
    },
};
</script>

<template>
    <q-dialog v-model="showPrompt" persistent>
        <q-card style="min-width: 50vw">
            <q-card-section>
                <div class="text-h3">Search for a course!</div>
            </q-card-section>

            <q-card-section>
                <q-input
                    v-model="search"
                    style="width: 100%"
                    label="Course Name"
                    autofocus
                />
            </q-card-section>
            <q-card-section vertical>
                <q-expansion-item label="Advanced Search Options">
                    <q-separator />
                    <q-card-section
                        class="flex row advancedFilter"
                        style="padding-bottom: 0"
                    >
                        <q-card-section style="padding-top: 0">
                            <q-input
                                v-model="subject"
                                label="Subject (ex: CSCI)"
                            />
                            <q-input
                                v-model="code"
                                label="Course Code (ex: 2300)"
                            />
                        </q-card-section>
                        <q-option-group
                            v-model="chosen"
                            :options="options"
                            type="checkbox"
                            label="Select semesters to include"
                            class="q-pr-md col-grow options"
                        />
                    </q-card-section>
                </q-expansion-item>
            </q-card-section>
            <q-card-section style="padding-top: 0">
                <q-virtual-scroll
                    v-slot="{ item }"
                    style="max-height: 300px"
                    :items="filteredCourses"
                >
                    <q-card-section class="q-pt-md courseGroup" horizontal>
                        <CourseCard
                            :course="item"
                            :check="false"
                            :show-bar="false"
                            class="course"
                        />
                        <q-btn
                            v-close-popup
                            class="q-ma-none col-grow"
                            label="Add Course"
                            @click="addCourse(item)"
                        />
                    </q-card-section>
                </q-virtual-scroll>
            </q-card-section>

            <q-card-actions class="text-primary">
                <q-btn v-close-popup flat label="Cancel" @click="close()" />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>

<style lang="scss">
.card {
    max-width: 70% !important;
    background-color: darken($secondary, 15%) !important;
    box-sizing: border-box !important;
    padding: 5px !important;
    border-radius: 10px !important;
    height: 5vh !important;
    color: white !important;
}

.courseGroup {
    display: flex;
    margin: 0 auto;
    padding-top: 2px;
    width: 90%;
}

.advancedFilter {
    box-sizing: border-box;
    padding: 15px;
    gap: 5%;
}

.options {
    display: grid;
    grid-auto-flow: column;
    grid-template-rows: 1fr 1fr 1fr;
}

.dropdown-toggle {
    border-radius: 5px;
    box-sizing: border-box;
    padding: 3px;
    cursor: pointer;
}

.dropdown-toggle:hover {
    background-color: lightgray;
}

.addButton {
    margin: auto;
}
</style>
