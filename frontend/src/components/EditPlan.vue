<script>
export default {

}
</script>


<template>
    <q-form
        class="full-width column wrap justify-center items-center content-center"
        @submit.prevent.stop="submit"
    >
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
            @input-value="filterMajor"
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
            @input-value="filterConcentration"
        />
        <div>
            <q-btn label="Submit" color="primary" type="submit" />
            <q-btn
                label="Reset"
                color="primary"
                flat
                style="margin-left: 10px"
                @click="reset"
            />
        </div>
  </q-form>
</template>


<style>

</style>