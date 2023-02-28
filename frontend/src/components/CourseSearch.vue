<script>
import ACourse from "../components/ACourse.vue";

export default {
    components: {
        ACourse,
    },
    props: {
        coursesData: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            course: null,
            prompt: false,
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
        };
    },
    computed: {
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
            this.course = course;
        },
    },
};
</script>

<template>
    <q-avatar
        square
        size="75px"
        font-size="50px"
        color="primary"
        icon="add"
        class="addButton"
        :style="{ cursor: 'pointer' }"
        @click="prompt = true"
    />
    <q-dialog v-model="prompt" persistent>
        <q-card style="min-width: 350px">
            <q-card-section>
                <div class="text-h6">Search for a course!</div>
            </q-card-section>

            <q-card-section class="q-pt-none" horizontal>
                <q-card-section class="q-pt-none" vertical>
                    <q-input v-model="search" label="Course Name" autofocus />
                    <q-input v-model="subject" label="Subject (ex: CSCI)" />
                    <q-input v-model="code" label="Course Code (ex: 2300)" />
                </q-card-section>
                <q-option-group
                    v-model="chosen"
                    :options="options"
                    type="checkbox"
                    label="Select semesters to include"
                    class="q-pr-md"
                />
            </q-card-section>
            <q-card-section>
                <q-virtual-scroll
                    v-slot="{ item }"
                    style="max-height: 300px"
                    :items="filteredCourses"
                >
                    <q-card-section class="q-pt-md" horizontal>
                        <ACourse :course="item" :check="false" />
                        <q-btn
                            v-close-popup
                            class="q-ma-none"
                            label="Add Course"
                            @click="addCourse(item)"
                        />
                    </q-card-section>
                </q-virtual-scroll>
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
                <q-btn v-close-popup flat label="Cancel" />
            </q-card-actions>
        </q-card>
    </q-dialog>
</template>

<style>
.addButton {
    margin: auto;
}
</style>
