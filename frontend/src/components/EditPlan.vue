<script>
import { useStore } from "../stores/store";
import programsJSON from "../data/programs.json";
import coursesJSON from "../data/courses.json";

export default {
    data() {
        const pathways = [
            "None",
            "Art History, Theory, and Criticism",
            "Artificial Intelligence",
            "Behavioral and Cognitive Neuroscience",
            "Chinese Language",
            "Creative Design and Innovation",
            "Design, Innovation, and Society Pathway",
            "Economics",
            "Economics of Banking and Finance",
            "Economics of Decision-Making",
            "Economics of Healthcare Markets",
            "Economics of Policy and Regulations",
            "Economics of Quantitative Modeling",
            "Economics of Technology and Innovation",
            "Electronic Arts",
            "Environmental Futures",
            "Ethics, Integrity, and Social Responsibility",
            "Extent and Limits of Rationality",
            "Fact and Fiction",
            "Game Studies",
            "Gender, Race, Sexuality, Ethnicity, and Social Change",
            "Graphic Design",
            "History",
            "Information Technology and Web Sciences",
            "Interactive Media/Data Design",
            "Language",
            "Linguistics",
            "Literature and Creative Writing",
            "Living in a World of Data",
            "Logical Thinking",
            "Media and Culture",
            "Mind, Brain, and Intelligence",
            "Music and Culture",
            "Music Composition and Production",
            "Music Performance",
            "Philosophy",
            "Pre-Health Pathway",
            "Public Health",
            "Science, Technology, and Society",
            "Strategic Communication",
            "Studio Arts",
            "Sustainability",
            "Thinking with Science",
            "Transfer Student Arts and Humanities",
            "Transfer Student Social Science",
            "Understanding Human Behavior",
            "Video, Performance, and Social Practice",
            "Well-being: Body and Mind",
        ];
        const concentrations = [
            "None",
            "Crizbae is a Monkey1",
            "Crizbae is a Monkey2",
            "Crizbae is a Monkey3",
            "Crizbae is a Monkey4",
            "Crizbae is a Monkey5",
        ];
        return {
            store: useStore(),
            selectedMajors: [],
            degreeName: "",
            majorOptions: Object.keys(programsJSON["2022-2023"]),
            filteredMajors: Object.keys(programsJSON["2022-2023"]),
            selectedMinors: [],
            minorOptions: Object.keys(programsJSON["2022-2023"]),
            filteredMinors: Object.keys(programsJSON["2022-2023"]),
            selectedPathways: "None",
            pathwayOptions: pathways,
            filteredPathways: pathways,
            selectedConcentrations: "None",
            concentrationOptions: concentrations,
            filteredConcentrations: concentrations,
            programsData: programsJSON,
            coursesData: coursesJSON,
        };
    },
}
</script>


<template>
    <q-form class="full-width column wrap justify-center items-center content-center">
        <q-input
            v-model="degreeName"
            label="Plan Name *"
            hint="Rename Your Plan"
            :dense="true"
            clearable
            style="
                width: 300px;
                margin-bottom: 20px;
                font-family: 'Rubik', sans-serif;
            "
            lazy-rules
            :rules="[(val) => (val && val.length > 0) || 'Please enter a name']"
        />
        <q-select
            v-model="selectedMajors"
            use-input
            multiple
            input-debounce="0"
            max-values="2"
            :options="filteredMajors"
            options-dense
            clearable
            :dense="true"
            :input-style="{ FontFace: 'Rubik', fontSize: '15px' }"
            :popup-content-style="{ fontSize: '15px', width: '250px' }"
            label="Major(s) *"
            hint="Change Your Major(s)"
            style="
                width: 300px;
                margin-bottom: 20px;
                font-family: 'Rubik', sans-serif;
            "
            lazy-rules
            :rules="[
                (val) =>
                    (val && val.length > 0) || 'Please pick at least one major',
            ]"
            @input-value="filteredMajors"
        />
        <q-select
            v-model="selectedMinors"
            use-input
            multiple
            max-input="2"
            :input-style="{ FontFace: 'Rubik', fontSize: '15px' }"
            input-debounce="0"
            :options="filteredMinors"
            options-dense
            clearable
            :dense="true"
            :popup-content-style="{ fontSize: '15px', width: '250px' }"
            label="Minor(s)"
            hint="Edit Your Minor(s)"
            style="
                width: 300px;
                margin-bottom: 20px;
                font-family: 'Rubik', sans-serif;
            "
            @input-value="filterMinor"
        />
        <q-select
            v-model="selectedPathways"
            use-input
            input-debounce="0"
            :options="filteredPathways"
            options-dense
            clearable
            :dense="true"
            :popup-content-style="{ fontSize: '15px', width: '250px' }"
            label="Pathway"
            hint="Edit Your Pathway"
            style="
                width: 300px;
                margin-bottom: 20px;
                font-family: 'Rubik', sans-serif;
            "
            @input-value="filterPathway"
        />
        <q-select
            v-model="selectedConcentrations"
            use-input
            input-debounce="0"
            :options="filteredConcentrations"
            :dense="true"
            options-dense
            clearable
            :popup-content-style="{ fontSize: '15px', width: '250px' }"
            label="Concentration"
            hint="Edit Your Concentration"
            style="
                width: 300px;
                margin-bottom: 20px;
                font-family: 'Rubik', sans-serif;
            "
            @input-value="filteredConcentrations"
        />
  </q-form>
</template>


<style>

</style>