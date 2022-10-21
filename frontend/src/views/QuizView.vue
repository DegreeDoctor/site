<script>
import { useStore } from "../stores/store";
import { ref } from 'vue';



const stringOptions = [
    'Computer Science', 'Information Technology Web Science', 'Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'Economics', 'Psychology', 'Sociology', 'Philosophy', 'English', 'French', 'German', 'Spanish', 'Italian', 'Russian', 'Chinese', 'Japanese', 'Arabic', 'Other'
]

export default {
    data() {
        return {
            store: useStore(),
        };
    },
    setup() {
        const filterOptions = ref(stringOptions)

        return {
            model: ref(null),
            filterOptions,

            createValue(val, done) {

                if (val.length > 0) {
                    if (!stringOptions.includes(val)) {
                        stringOptions.push(val)
                    }
                    done(val, 'toggle')
                }
            },

            filterFn(val, update) {
                update(() => {
                    if (val === '') {
                        filterOptions.value = stringOptions
                    }
                    else {
                        const needle = val.toLowerCase()
                        filterOptions.value = stringOptions.filter(
                            v => v.toLowerCase().indexOf(needle) > -1
                        )
                    }
                })
            }
        }
    }
}
</script>



<template>
    <q-form action="https://some-url.com" method="post">
        <q-select filled v-model="model" use-input use-chips multiple input-debounce="0" @new-value="createValue"
            :options="filterOptions" @filter="filterFn" style="width: 250px" />
    </q-form>
</template>
