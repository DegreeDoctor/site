<script>
import { useStore } from "../stores/store";
import programsJSON from "../data/programs.json";
import { ref } from 'vue'

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


export default {
  setup() {
    const degreeName = "";
    const majorOptions = Object.keys(programsJSON["2022-2023"]);
    const filteredMajors = Object.keys(programsJSON["2022-2023"]);
    const selectedMajors = [];
    const minorOptions = Object.keys(programsJSON["2022-2023"]);
    const filteredMinors = Object.keys(programsJSON["2022-2023"]);
    const selectedMinors = [];
    const pathwayOptions = pathways;
    const filteredPathways = pathways;
    const selectedPathways = "None";
    const concentrationOptions = pathways;
    const filteredConcentrations = concentrations;
    const selectedConcentrations = "None";
    const programsData = programsJSON;
    const store = useStore();

    const optionsMajors = ref(filteredMajors)
    const optionsMinors = ref(filteredMinors)
    const optionsPathways = ref(filteredPathways)
    const optionsConcentrations = ref(filteredConcentrations)

    return {
      degreeName, selectedMajors, selectedMinors, selectedPathways, selectedConcentrations, majorOptions, minorOptions, pathwayOptions, concentrationOptions, programsData, store, 
      optionsMajors, optionsMinors, optionsPathways, optionsConcentrations,
      filteredMajorsModel: ref(null),
      filteredMinorsModel: ref(null),
      filteredPathwaysModel: ref(null),
      filteredConcentrationsModel: ref(null),
 

      filterMajorsFn(val, update, abort) {
        setTimeout(() => {
          update(() => {
            if (val === '') { 
              optionsMajors.value = filteredMajors 
            }
            else { 
              const needle = val.toLowerCase() 
              optionsMajors.value = filteredMajors.filter(v => v.toLowerCase().indexOf(needle) > -1) 
            }
          },
            ref => { // "ref" is the Vue reference to the QSelect
            if (val !== '' && ref.options.length > 0) {
                ref.setOptionIndex(-1) // reset optionIndex in case there is something selected
                ref.moveOptionSelection(1, true) // focus the first selectable option and do not update the input-value
              }
            }
          )
        }, 300)
      },

      filterMinorsFn(val, update, abort) {
        setTimeout(() => {
          update(() => {
            if (val === '') { optionsMinors.value = filteredMinors }
            else { const needle = val.toLowerCase(); optionsMinors.value = filteredMinors.filter(v => v.toLowerCase().indexOf(needle) > -1) }
          },
            ref => { // "ref" is the Vue reference to the QSelect
              if (val !== '' && ref.optionsMinors.length > 0 && ref.getOptionIndex() === -1) {
                ref.moveOptionSelection(1, true) // focus the first selectable option and do not update the input-value
                ref.toggleOption(ref.optionsMinors[ref.optionIndex], true) // toggle the focused option
              }
            }
          )
        }, 300)
      },

      filterPathwayFn(val, update, abort) {
        setTimeout(() => {
          update(() => {
            if (val === '') { optionsPathways.value = filteredPathways }
            else { const needle = val.toLowerCase(); optionsPathways.value = filteredPathways.filter(v => v.toLowerCase().indexOf(needle) > -1) }
          },
            ref => { // "ref" is the Vue reference to the QSelect
              if (val !== '' && ref.optionsPathways.length > 0 && ref.getOptionIndex() === -1) {
                ref.moveOptionSelection(1, true) // focus the first selectable option and do not update the input-value
                ref.toggleOption(ref.optionsPathways[ref.optionIndex], true) // toggle the focused option
              }
            }
          )
        }, 300)
      },

      filterConcentrationFn(val, update, abort) {
        setTimeout(() => {
          update(() => {
            if (val === '') { optionsConcentrations.value = filteredConcentrations }
            else { const needle = val.toLowerCase(); optionsConcentrations.value = filteredConcentrations.filter(v => v.toLowerCase().indexOf(needle) > -1) }
          },
            ref => { // "ref" is the Vue reference to the QSelect
              if (val !== '' && ref.optionsConcentrations.length > 0 && ref.getOptionIndex() === -1) {
                ref.moveOptionSelection(1, true) // focus the first selectable option and do not update the input-value
                ref.toggleOption(ref.optionsConcentrations[ref.optionIndex], true) // toggle the focused option
              }
            }
          )
        }, 300)
      },

      abortFilterFn() {
        // console.log('delayed filter aborted')
      }, 

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
      filterPathway(val) {
        this.filteredPathways = this.pathwayOptions.filter((x) =>
          x.toLowerCase().includes(val.toLowerCase())
        );
      },
      addPathway(val) {
        if (val.length > 0) {
          if (!this.selectedPathways.includes(val)) {
            this.selectedPathways.push(val);
          }
        }
      },
      filterConcentration(val) {
        this.filteredConcentrations = this.concentrationOptions.filter(
          (x) => x.toLowerCase().includes(val.toLowerCase())
        );
      },
      addConcentration(val) {
        if (val.length > 0) {
          if (!this.selectedConcentrations.includes(val)) {
            this.selectedConcentrations.push(val);
          }
        }
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
        degree["template"] =
          this.programsData["2022-2023"][this.selectedMajors[0]][
          "template"
          ];
        this.store.addDegree(degree);
        this.$router.push("/degree");
      },

    }
  }
}
</script>


<template>
  <div class="q-pa-md full-width column wrap justify-center items-center content-center">
    <div class="q-gutter-md">
      <p>Create Your Plan!</p>
      <q-input 
        v-model="degreeName" 
        label="Plan Name"
        style="width: 300px; margin-bottom: 20px" 
      />

      <!-- MAJORS -->
      <q-select
        v-model="filteredMajorsModel"
        use-chips
        use-input
        hide-dropdown-icon
        clearable
        options-dense
        multiple
        max-values="2"
        hint="Select up to 2 majors"
        input-debounce="0"
        label="Major(s)"
        :options="optionsMajors"
        @filter="filterMajorsFn"
        @filter-abort="abortFilterFn"
        @keyup.delete="model = null"
        style="width: 300px"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>

      <!-- MINORS -->
      <q-select
        v-model="filteredMinorsModel"
        use-input
        use-chips
        multiple
        hide-dropdown-icon
        clearable
        options-dense
        max-values="2"
        hint="Select up to 2 minors"
        input-debounce="0"
        label="Minor(s)"
        :options="optionsMinors"
        @filter="filterMinorsFn"
        @filter-abort="abortFilterFn"
        style="width: 300px"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>
      
      
      <!-- PATHWAY -->
      <q-select
        v-model="filteredPathwaysModel"
        use-input
        use-chips
        hide-dropdown-icon
        clearable
        options-dense
        input-debounce="0"
        label="Pathway"
        :options="optionsPathways"
        @filter="filterPathwayFn"
        @filter-abort="abortFilterFn"
        style="width: 300px"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>
      
      
      <!-- CONCENTRATION --> 
      <q-select
        v-model="filteredConcentrationsModel" 
        use-input
        use-chips
        hide-dropdown-icon
        clearable
        options-dense
        input-debounce="0"
        label="Concentration"
        :options="optionsConcentrations"
        @filter="filterConcentrationFn"
        @filter-abort="abortFilterFn"
        style="width: 300px"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>
    </div>

    <q-btn 
      label="Submit" 
      color="accent" 
      @click="submit"
      style="padding-top: 0px; padding-bottom: 0px; padding-left: 15px; padding-right: 15px; margin-top: 20px;" 
    />

  </div>
</template>

<style>
p {
    margin-top: 15px;
    margin-bottom: 15px;
    font-size: 30px;
    display: grid;
    justify-content: center;
}
</style>
