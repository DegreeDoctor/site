<script>
import { useQuasar } from "quasar";
import { useStore } from "../stores/store";

export default {
  data() {
    return {
      current: useStore().getCurrentDegreeName,
      allDegrees: useStore().getDegreeNames,
      store: useStore(),
      plan: false,
      filter: "",
    };
  },
  computed: {
    selectedPlan() {
      return this.store.getCurrentDegreeName;
    },
    filteredPlans() {
      return this.store.getDegreeNames.filter((x) =>
        x.toLowerCase().includes(this.filter.toLowerCase())
      );
    },
  },
  methods: {
    selectPlan(val) {
      this.store.swapDegree(val);
      this.current = val;
    },
    filterPlan(val) {
      this.filter = val;
    },
    positioned() {
      this.$q.dialog({
        title: 'Positioned',
        message: 'This dialog appears from bottom.',
      })
    },
  },
}
</script>

<template> 
<div class="q-pa-md btn">
  <!-- <q-btn :ripple="false" flat no-caps v-bind:label="current" icon-right="fa-solid fa-caret-down" class="btn"> -->
  {{ current }}
    <q-menu>
      <q-item v-for="item in allDegrees" :key="item" clickable v-on:click="selectPlan(item)">
        <q-btn flat >
          <q-icon name="fa-solid fa-trash" size="1.5em"/>
        </q-btn>
        <q-item-section>{{ item }}</q-item-section>
      </q-item>
      <q-separator />
      <q-item>
        <q-btn flat to="/quiz" label="Create new plan"></q-btn>
      </q-item>
    </q-menu>
  <q-icon name="fa-solid fa-caret-down" />
  <!-- <q-dialog v-model="plan">
    <q-card style="min-width: 350px">
        <q-card-section>
            <div class="text-h6">Pick a plan</div>
        </q-card-section>

        <q-card-section class="q-pt-none">
            <h6 class="q-ma-none">
                Current Plan: {{ selectedPlan }}
            </h6>
            <div class="card-contain">
                <q-select
                    v-model="current"
                    filled
                    use-input
                    input-debounce="0"
                    label="Search"
                    :options="filteredPlans"
                    style="width: 200px"
                    behavior="menu"
                    @input-value="filterPlan"
                    @update:model-value="selectPlan"
                >
                    <template #no-option>
                        <q-item>
                            <q-item-section class="text-grey">
                                No results
                            </q-item-section>
                        </q-item>
                    </template>
                </q-select>
                <div>
                    <ProgressBar />
                </div>
            </div>
        </q-card-section>
        <q-card-actions class="text-primary">
            <q-btn v-close-popup flat label="Cancel"></q-btn>
            <q-btn
                v-close-popup
                flat
                label="Add new plan"
                to="/quiz"
            ></q-btn>
        </q-card-actions>
    </q-card>
  </q-dialog>  -->
</div>
</template>

<style>
  .btn {
    color: #fff;
    border-radius: 5px;
    padding: 0.5em 1em;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    padding-right: 1em;
    padding-left: 1em;
  }
  .btn .q-icon {
    font-size: 1em;
  }
  .btn:hover {
    background-color: transparent !important;
    cursor: pointer;
  }
</style>