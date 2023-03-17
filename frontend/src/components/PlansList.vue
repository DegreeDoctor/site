<script>
import { useStore } from "../stores/store";

export default {
    data() {
        return {
            current: useStore().getCurrentDegreeName,
            // allDegrees: useStore().getDegreeNames,
            store: useStore(),
            plan: false,
            filter: "",
            deleteIconsVisible: false,            
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
        allDegrees() {
            return this.store.getDegreeNames;
        },
        allDegreesSubNames() {
            return this.store.getDegreeSubNames;
        }
    },
    methods: {
        selectPlan(val) {
            this.store.swapDegree(val);
            this.current = val;
        },
        filterPlan(val) {
            this.filter = val;
        },
        deletePlan(val, all = false) {
            // if the degree is undefined, do nothing
            this.store.removeDegree(val);
            // find the index of the next available plan
            let index = this.store.getDegreeNames.indexOf(val) - 1;
            if (index < 0) {
                index = 0;
            }
            // if there are no plans left, create a new one send the user to the quiz page
            if (this.store.getDegreeNames.length === 0) {
                this.$router.push("/quiz");
            }
            // show a notification to the user that the plan was deleted
            if (all === true) {
                this.toggleTrashIcons();
                return;
            } else {
                let msg = "Plan " + '"' + val + '"' + " deleted";
                this.showNotif("top", msg, "negative", 1250);
                // select the next available plan
                this.selectPlan(this.store.getDegreeNames[index]);
                this.toggleTrashIcons();
            }
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
                    this.store.getDegreeNames.forEach((plan) => {
                        this.deletePlan(plan, true);
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
        renamePlanNotification() {
            this.$q.notify({
                badgeClass: "hide-badge",
                type: "warning",
                textColor: "white",
                message: "This feature is not yet implemented",
                position: "top",
                timeout: 1250,
            });
        },
        renamePlanDialog() {
            this.$q
                .dialog({
                    title: "Change Plan Name",
                    message: "Rename your plan",
                    prompt: {
                        model: "",
                        type: "text",
                    },
                    cancel: true,
                    persistent: false,
                })
                .onOk((data) => {
                    this.store.updateDegree(this.current, data);
                    this.selectPlan(data);
                    this.current = data;
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
    <div class="q-pa-md btn">
        {{ selectedPlan }}
        <q-menu anchor="bottom left">
            <q-item
                v-for="item in allDegreesSubNames"
                :key="item"
                class="planList"
                :class="{ 'active-item': selectedPlan === item }"
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
                    @click="renamePlanNotification"
                >
                    <q-icon name="fa-solid fa-pen-to-square" size="1.25em" />
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
    background-color: #fff !important;
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
    color: black;
}
</style>
