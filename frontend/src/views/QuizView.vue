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
const filteredConcentrations = pathways;
const selectedConcentrations = "None";
const programsData = programsJSON;
const store = useStore();

export default {
  setup() {
    const options = ref(filteredMajors)

    return {
      model: ref(null),
      options,

      filterFn(val, update, abort) {
        // call abort() at any time if you can't retrieve data somehow

        setTimeout(() => {
          update(
            () => {
              if (val === '') {
                options.value = filteredMajors
              }
              else {
                const needle = val.toLowerCase()
                options.value = filteredMajors.filter(v => v.toLowerCase().indexOf(needle) > -1)
              }
            },

            // "ref" is the Vue reference to the QSelect
            ref => {
              if (val !== '' && ref.options.length > 0) {
                ref.setOptionIndex(-1) // reset optionIndex in case there is something selected
                ref.moveOptionSelection(1, true) // focus the first selectable option and do not update the input-value
              }
            }
          )
        }, 300)
      },

      filterFnAutoselect(val, update, abort) {
        // call abort() at any time if you can't retrieve data somehow

        setTimeout(() => {
          update(
            () => {
              if (val === '') {
                options.value = "filteredMajors"
              }
              else {
                const needle = val.toLowerCase()
                options.value = filteredMajors.filter(v => v.toLowerCase().indexOf(needle) > -1)
              }
            },

            // "ref" is the Vue reference to the QSelect
            ref => {
              if (val !== '' && ref.options.length > 0 && ref.getOptionIndex() === -1) {
                ref.moveOptionSelection(1, true) // focus the first selectable option and do not update the input-value
                ref.toggleOption(ref.options[ref.optionIndex], true) // toggle the focused option
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
      }

    }
  }
}
</script>


<template>
  <div class="q-pa-md">
    <div class="q-gutter-md">
      <!-- MAJORS -->
      <q-select
        filled
        v-model="model"
        clearable
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        label="Major(s)"
        :options="options"
        @filter="filterFnAutoselect"
        @filter-abort="abortFilterFn"
        style="width: 250px"
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
        filled
        v-model="model"
        clearable
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        label="Minor(s)"
        :options="options"
        @filter="filterFnAutoselect"
        @filter-abort="abortFilterFn"
        style="width: 250px"
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
        filled
        v-model="model"
        clearable
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        label="Pathway"
        :options="options"
        @filter="filterFnAutoselect"
        @filter-abort="abortFilterFn"
        style="width: 250px"
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
        filled
        v-model="model"
        clearable
        use-input
        hide-selected
        fill-input
        input-debounce="0"
        label="Concentration"
        :options="options"
        @filter="filterFnAutoselect"
        @filter-abort="abortFilterFn"
        style="width: 250px"
      >
        <template v-slot:no-option>
          <q-item>
            <q-item-section class="text-grey">
              No results
            </q-item-section>
          </q-item>
        </template>
      </q-select>


      <div>
      <q-btn 
        label="Submit" 
        color="accent" 
        @click="submit"
        style="padding-top: 0px; padding-bottom: 0px; padding-left: 15px; padding-right: 15px; margin-top: 20px;" 
      />
    </div>
    </div>
  </div>
</template>

<style>
p {
    margin-top: 15px;
    margin-bottom: 15px;
    font-size: 30px;
}
</style>
