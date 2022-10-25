<script>
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            store: useStore(),
            selectedMajors: [],
            majorSearch: "",
            minorSearch: "",
            selectedMinors: [],
            majorOptions: [
                "Computer Science",
                "Information Technology Web Science",
                "Math",
                "Physics",
                "Chemistry",
                "Biology",
                "History",
                "Geography",
                "Economics",
                "Psychology",
                "Sociology",
                "Philosophy",
                "English",
                "French",
                "German",
                "Spanish",
                "Italian",
                "Russian",
                "Chinese",
                "Japanese",
                "Arabic",
                "Other",
            ],
            minorOptions: [
                "Monkey Science",
                "Information Technology Web Science",
                "Math",
                "Physics",
                "Chemistry",
                "Biology",
                "History",
                "Geography",
                "Economics",
                "Psychology",
                "Sociology",
                "Philosophy",
                "English",
                "French",
                "German",
                "Spanish",
                "Italian",
                "Russian",
                "Chinese",
                "Japanese",
                "Arabic",
                "Other",
            ],
        };
    },
    computed: {
        filterMajor() {
            if (this.majorSearch === "") {
                return this.majorOptions;
            } else {
                const needle = this.majorSearch.toLowerCase();
                return this.majorOptions.filter(
                    (v) => v.toLowerCase().indexOf(needle) > -1
                );
            }
        },

        filterMinor() {
            if (this.minorSearch === "") {
                return this.minorOptions;
            } else {
                const needle = this.minorSearch.toLowerCase();
                return this.minorOptions.filter(
                    (v) => v.toLowerCase().indexOf(needle) > -1
                );
            }
        },
    },
    methods: {
        addMajor(val, done) {
            if (val.length > 0) {
                if (!this.selectedMajors.includes(val)) {
                    this.selectedMajors.push(val);
                }
                done(val, "toggle");
            }
        },

        addMinor(val, done) {
            if (val.length > 0) {
                if (!this.selectedMinors.includes(val)) {
                    this.selectedMinors.push(val);
                }
                done(val, "toggle");
            }
        },
    },
};
</script>

<template>
    <q-form action="https://some-url.com" method="post" class="fixed-center">
        <p>Select Your Major(s):</p>
        <q-select
            v-model="model"
            filled
            use-input
            use-chips
            multiple
            input-debounce="0"
            :options="filterMajor"
            style="width: 250px"
            @new-value="addMajor"
        />
        <p>Select Your Minor(s):</p>

        <q-select
            v-model="model"
            filled
            use-input
            use-chips
            multiple
            input-debounce="0"
            :options="filterMinor"
            style="width: 250px"
            @new-value="addMinor"
        />
    </q-form>
</template>
