<script>
import { useStore } from "../stores/store";

export default {
    data() {
        const majors = [
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
        ];
        const minors = [
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
        ];
        return {
            store: useStore(),
            selectedMajors: [],
            majorSearch: "",
            majorOptions: majors,
            filteredMajors: majors,
            selectedMinors: [],
            minorSearch: "",
            minorOptions: minors,
            filteredMinors: minors,
        };
    },
    methods: {
        addMajor(val) {
            if (val.length > 0) {
                if (!this.selectedMajors.includes(val)) {
                    this.selectedMajors.push(val);
                }
            }
        },
        addMinor(val) {
            if (val.length > 0) {
                if (!this.selectedMinors.includes(val)) {
                    this.selectedMinors.push(val);
                }
            }
        },
        filterMajor(val) {
            this.filteredMajors = this.majorOptions.filter((x) =>
                x.toLowerCase().includes(val.toLowerCase())
            );
        },
        filterMinor(val) {
            this.filteredMinors = this.minorOptions.filter((x) =>
                x.toLowerCase().includes(val.toLowerCase())
            );
        },
    },
};
</script>

<template>
    <q-form action="https://some-url.com" method="post" class="fixed-center">
        <p>Select Your Major(s):</p>
        <q-select
            v-model="selectedMajors"
            filled
            use-input
            use-chips
            multiple
            input-debounce="0"
            :options="filteredMajors"
            style="width: 250px"
            @new-value="addMajor"
            @input-value="filterMajor"
        />
        <p>Select Your Minor(s):</p>
        <q-select
            v-model="selectedMinors"
            filled
            use-input
            use-chips
            multiple
            input-debounce="0"
            :options="filteredMinors"
            style="width: 250px"
            @new-value="addMinor"
            @input-value="filterMinor"
        />
    </q-form>
</template>
