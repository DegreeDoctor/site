<script>
import { useQuasar } from "quasar";
import { useStore } from "../stores/store";

export default {
  data() {
    return {
      current: useStore().getCurrentDegreeName,
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
    },
    filterPlan(val) {
      this.filter = val;
    },
    positioned() {
      this.$q.dialog({
        title: 'Positioned',
        message: 'This dialog appears from bottom.',
        position: 'bottom'
      })
    },
  },
}
</script>

<template> 
<div class="q-pa-md">
  <q-btn
      no-caps
      label="My Plans"
      color="primary"
      @click="positioned"
  ></q-btn>
  <q-dialog v-model="plan">
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
  </q-dialog> 
</div>
</template>