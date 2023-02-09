<script>
import { useStore } from "../stores/store";
import programsJSON from "../data/programs.json";
import { useQuasar } from 'quasar'

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
    };
  },
  methods: {
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
    filterPathway(val) {
      this.filteredPathways = this.pathwayOptions.filter((x) =>
        x.toLowerCase().includes(val.toLowerCase())
      );
    },
    filterConcentration(val) {
      this.filteredConcentrations = this.concentrationOptions.filter(
        (x) => x.toLowerCase().includes(val.toLowerCase())
      );
    },
    submit() {
      let degree = {
        name: this.degreeName,
        majors: this.selectedMajors,
        minors: this.selectedMinors,
        pathway: this.selectedPathways,
        credits: {},
        concentration: this.selectedConcentrations,
      };
      // checks if any of the majors are also minors
      for (let i = 0; i < degree.majors.length; i++) {
        for (let j = 0; j < degree.minors.length; j++) {
          if (degree.majors[i] == degree.minors[j]) {
            this.showNotif("top", "One of your majors is also a minor", "negative");
            return;
          }
        }
      }
      degree["template"] =
        this.programsData["2022-2023"][this.selectedMajors[0]][
        "template"
        ];
      this.store.addDegree(degree);
      this.$router.push("/degree");
      let message = "You have created plan " + "\"" + this.degreeName + "\"";
      this.showNotif("top", message, "positive");
    },
    reset() {
      this.degreeName = "";
      this.selectedMajors = [];
      this.selectedMinors = [];
      this.selectedPathways = "None";
      this.selectedConcentrations = "None";
      this.showNotif("top", "Form has been reset", "info", 300)
    },
  },
  setup() {
    const $q = useQuasar(); 
    return {
      // Useful reference https://quasar.dev/quasar-plugins/notify#positioning
      showNotif (position, message, type, timeout = 1250) {
        $q.notify({
          badgeClass: "hide-badge",
          type,
          textColor: "white",
          message,
          position,
          timeout
        })
      },
    }
  }
};

</script>

<template>
  <q-form
  class="full-width column wrap justify-center items-center content-center" 
  @submit.prevent.stop="submit">
    <p>Create Your Degree!</p>
    <q-input
      v-model="degreeName"
      label="Plan Name *"
      hint="Name Your Plan"
      :dense="true"
      clearable
      style="width: 300px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;"
      lazy-rules
      :rules="[ val => val && val.length > 0 || 'Please enter a name']"
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
      hint="Select Your Major(s)"
      @input-value="filterMajor"
      style="width: 300px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;"
      lazy-rules
      :rules="[ val => val && val.length > 0 || 'Please pick at least one major']"
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
      hint="Select Your Minor(s)"
      @input-value="filterMinor"
      style="width: 300px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;"
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
      hint="Select Your Pathway"
      @input-value="filterPathway"
      style="width: 300px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;"
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
      hint="Select Your Concentration"
      @input-value="filterConcentration"
      style="width: 300px; margin-bottom: 20px; font-family: 'Rubik', sans-serif;"
    />
    <div>
        <q-btn label="Submit" color="primary" type="submit" />
        <q-btn label="Reset" color="primary" flat @click="reset" style="margin-left: 10px;"/>
    </div>
  </q-form>
</template>

<style>

@import url('https://fonts.googleapis.com/css2?family=Rubik&display=swap');

p {
  margin-top: 15px;
  margin-bottom: 10px;
  font-family: 'Rubik', sans-serif;
  font-size: 30px;
}

.hide-badge {
  background-color: transparent;
  box-shadow: 0 0 0 0 transparent;
  color: transparent;
}

</style>
