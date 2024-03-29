<script>
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            current: useStore().getCurrentDegreeName,
            // allDegrees: useStore().getDegreeUUID,
            store: useStore(),
            plan: false,
            filter: "",
            deleteIconsVisible: false,
            deleteIconsVisibleArray: [false],
            htmlList: [],
        };
    },
    computed: {
        selectedPlan() {
            // if there are no degrees return an empty string
            if (this.store.getDegreeUUID.length === 0) {
                return "";
            }
            return this.store.getCurrentDegreeName;
        },
        filteredPlans() {
            return this.store.getDegreeUUID.filter((x) =>
                x.toLowerCase().includes(this.filter.toLowerCase())
            );
        },
        allDegrees() {
            return this.store.getDegreeUUID;
        },
        allDegreesSubNames() {
            return this.store.getDegreeSubNames;
        },
    },
    methods: {
        darkMode() {
            return this.store.getDarkMode;
        },
        selectPlan(val) {
            this.store.swapDegree(this.store.findDegree(val));
            this.current = this.store.findDegree(val);
            this.$router.push("/degree");
        },
        selectPlanByUUID(val) {
            this.store.swapDegree(val);
            this.current = this.store.findDegree(val);
        },
        filterPlan(val) {
            this.filter = val;
        },
        deletePlan(val) {
            // find the index of the next available plan
            let index =
                this.store.getDegreeUUID.indexOf(this.store.findDegree(val)) -
                1;
            if (index < 0) {
                index = 0;
            }
            this.store.removeDegree(this.store.findDegree(val));
            // if there are no plans left, create a new one send the user to the quiz page
            if (this.store.getDegreeUUID.length === 0) {
                this.$router.push("/quiz");
            }
            // show a notification to the user that the plan was deleted
            let msg = "Plan " + '"' + val + '"' + " deleted";
            this.showNotif("top", msg, "negative", 1250);
            // select the next available plan
            this.selectPlanByUUID(this.store.getDegreeUUID[index]);
            this.toggleTrashIcons();
        },
        deleteAllPlans() {
            this.$q
                .dialog({
                    title: "Delete All Plans",
                    message: "This action cannot be undone",
                    cancel: true,
                    persistent: false,
                })
                .onOk(() => {
                    // go through each plan and delete it
                    this.store.getDegreeUUID.forEach((plan) => {
                        this.store.removeDegree(plan);
                    });
                    this.showNotif(
                        "top",
                        "All plans deleted",
                        "negative",
                        1250
                    );
                    this.$router.push("/quiz");
                })
                .onCancel(() => {
                    return;
                })
                .onDismiss(() => {
                    return;
                });
        },
        toggleTrashIcons() {
            //this.deleteIconsVisibleArray[val]=!this.deleteIconsVisibleArray[val];
            this.deleteIconsVisible = !this.deleteIconsVisible;
        },
        showNotif(position, message, type, timeout = 1250) {
            // Useful reference https://quasar.dev/quasar-plugins/notify#positioning
            this.$q.notify({
                badgeClass: "hide-badge",
                type,
                textColor: "white",
                message,
                position,
                timeout,
            });
        },
        // allows to change name of plan
        renamePlanDialog(item) {
            this.$q
                .dialog({
                    title: "Rename Plan",
                    cancel: true,
                    persistent: false,
                    prompt: {
                        model: item,
                        type: "text",
                        label: "New Name",
                        hint: "Enter a new name for the plan",
                        isValid: (v) =>
                            !!v &&
                            v.length <= 25 &&
                            !this.store.findDegree(v) &&
                            v !== null,
                        lazyRules: true,
                        rules: [
                            (v) => !!v || "Name is required",
                            (v) =>
                                (v && v.length <= 25) ||
                                "Name must be less than 25 characters",
                            // check if the name is already taken
                            (v) =>
                                !this.store.findDegree(v) ||
                                "Name already taken",
                        ],
                    },
                })
                .onOk((data) => {
                    // check if name is already taken
                    if (!this.store.findDegree(data)) {
                        this.store.renameDegree(
                            this.store.findDegree(item),
                            data
                        );
                        this.showNotif(
                            "top",
                            "Plan renamed to " + '"' + data + '"',
                            "positive",
                            1250
                        );
                    } else {
                        this.showNotif(
                            "top",
                            "Name already taken",
                            "negative",
                            1250
                        );
                    }
                })
                .onCancel(() => {
                    return;
                })
                .onDismiss(() => {
                    return;
                });
        },
    },
};
</script>

<template>
    <div>
        <div class="q-pa-md btn">
            {{ selectedPlan }}
            <q-menu anchor="bottom left">
                <q-item
                    v-for="item in allDegreesSubNames"
                    :key="item"
                    class="planList"
                    :class="[
                        'planList',
                        { 'active-item': selectedPlan === item },
                        darkMode() ? 'dark-mode-active-item' : '',
                    ]"
                >
                    <a
                        class="item truncate"
                        :class="{ active: selectedPlan === item }"
                        @click="selectPlan(item)"
                    >
                        {{ item }}
                    </a>
                    <a
                        class="edit"
                        :class="{ 'hide-icon': deleteIconsVisible }"
                        @click="renamePlanDialog(item)"
                    >
                        <q-icon
                            name="fa-solid fa-pen-to-square"
                            size="1.25em"
                        />
                    </a>
                    <a
                        class="trash"
                        :class="{ 'hide-icon': deleteIconsVisible }"
                        @click="toggleTrashIcons"
                    >
                        <q-icon name="fa-solid fa-trash" size="1.25em" />
                    </a>
                    <a
                        class="check"
                        :class="{ 'hide-icon': !deleteIconsVisible }"
                        @click="deletePlan(item)"
                    >
                        <q-icon name="fa-solid fa-check" size="1.25em" />
                    </a>
                    <a
                        class="cross"
                        :class="{ 'hide-icon': !deleteIconsVisible }"
                        @click="toggleTrashIcons"
                    >
                        <q-icon name="fa-solid fa-times" size="1.25em" />
                    </a>
                </q-item>
                <q-separator />
                <q-item clickable to="/quiz">
                    <a class="new-plan">Create new plan</a>
                </q-item>
                <q-separator />
                <q-item clickable @click="deleteAllPlans">
                    <a class="delete-all">Delete all plans</a>
                </q-item>
            </q-menu>
            <q-icon name="fa-solid fa-caret-down" />
        </div>
    </div>
</template>

<style>
.btn {
    border-radius: 5px;
    padding: 0.5em 1em;
    font-size: 1.1em;
    font-weight: 500;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    gap: 0.5em;
}
.btn .q-icon {
    font-size: 1em;
}
.btn:hover {
    background-color: transparent !important;
    cursor: pointer;
    color: #bdbdbd;
}
.btn q-item:hover {
    cursor: pointer;
}
.q-item {
    align-items: center;
    justify-content: center;
}
.hide-icon {
    display: none;
}
.active-item {
    background-color: #eee;
}
.dark-mode-active-item.active-item {
    background-color: #424242;
    color: #fff;
}
.planList {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 1em;
}
.item {
    display: flex;
    flex-direction: row;
    flex: 1;
    text-align: left;
}
.item:hover {
    color: #bdbdbd;
    cursor: pointer;
}
.edit {
    color: #2196f3;
}
.edit:hover {
    color: #2196f3bd;
    cursor: pointer;
}
.trash {
    color: #f44336;
}
.trash:hover {
    color: #f44336bd;
    cursor: pointer;
}
.cross {
    color: #f44336;
}
.cross:hover {
    color: #f44336bd;
    cursor: pointer;
}
.check {
    color: #4caf50;
}
.check:hover {
    color: #4caf50bd;
    cursor: pointer;
}
.truncate {
    max-width: 200px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.new-plan {
    font-weight: 500;
    text-decoration: none;
}
.hide-badge {
    background-color: transparent !important;
    box-shadow: none !important;
    color: transparent !important;
}
</style>
