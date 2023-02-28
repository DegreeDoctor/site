<script>
import { useImage } from "@vueuse/core";
import { useStore } from "../stores/store";
import DarkModeToggle from "./DarkModeToggle.vue";
import ProgressBar from "./ProgressBar.vue";

export default {
    components: {
    DarkModeToggle,
    ProgressBar,
    useImage
},
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
        deletePlan() {
            this.store.removeDegree(this.selectedPlan);
        },
    },
};
</script>

<!-- <template>
    <q-header elevated class="bg-secondary text-white" height-hint="98">
        <q-toolbar>
            <q-toolbar-title to="/">
                <q-avatar>
                    <img src="../assets/Degree_Doctor_logo.png" />
                </q-avatar>
                Degree Doctor
            </q-toolbar-title>

            <DarkModeToggle />

            <div class="q-pa-md">
                <q-btn
                    no-caps
                    label="My Plans"
                    color="primary"
                    @click="plan = true"
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
                            <q-btn
                                v-close-popup
                                flat
                                label="Delete Plan"
                                @click="deletePlan();"
                                to="/degree"
                            ></q-btn>
                        </q-card-actions>
                    </q-card>
                </q-dialog>
            </div>
        </q-toolbar>
    </q-header>
</template> -->
<template>
    <nav> 
        <div class="navbar">
            <div class="image-container">
                <router-link to="/quiz" id="logo"><img src="../assets/Degree_Doctor_logo.png"/></router-link>
            </div>
            <div class="DD">
                <RouterLink to="/" id="title">Degree Doctor</RouterLink>
                <div class="fading-effect"></div>
            </div>
            <div class="other">
                <DarkModeToggle/>
                <RouterLink to="/quiz" id="plans">My Plans</RouterLink>
            </div>
        </div>
    </nav>  
</template>

<style scoped>
.navbar{
    display: flex;
    background:turquoise;
    justify-content: space-around;
    align-items: center;
    height: 5rem;
}
.image-container {
  position: absolute;
  top: 5%;
  left: 25%;
  transform: translate(-50%,-50%);
  z-index: 2; /* Makes sure this is on top */
}
.image-container img {
  -webkit-filter: drop-shadow(-4px 5px 5px rgba(0,0,0,0.6));
  filter: drop-shadow(-4px 5px 5px rgba(0,0,0,0.6));
  height: 200px;
  animation: image-slide 4s cubic-bezier(.5,.5,0,1);
  animation-fill-mode: forwards;
}
.DD {
  position: absolute;
  top: 5%;
  transform: translate(-50%,-50%);
  z-index: 1; /* Places this below the image container */
  margin-left: -700px;
}
.DD .fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: turquoise;
  -webkit-animation: text-slide 4s cubic-bezier(1, 0, 0.5, 0.5);
  animation: text-slide 4s cubic-bezier(1, 0, 0.5, 0.5);
  animation-fill-mode: backwards;
  -webkit-animation-fill-mode: backwards;
}
.fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: white;
}   
/* Slides the image from left (-250px) to right (150px) */
@keyframes image-slide {
  0% { transform: translateX(150px) scale(0); }
  60% { transform: translateX(150px) scale(1); }
  90% { transform: translateX(-250px) scale(1); }
  100% { transform: translateX(-250px) scale(1); }  
}

/* Slides the text by shrinking the width of the object from full (100%) to nada (0%) */
@keyframes text-slide {
    100% { width: 100%; }
    75%{ width: 100%; }
    60% { width: 0; }
    0% { width: 0; }
  /* 0% { width: 100%; }
  60% { width: 100%; }
  75%{ width: 0; }
  100% { width: 0; } */
}













#title{
    display:flex;
    color:black;
    text-decoration: none;
    font-size: 1.2rem;
    padding-bottom: 3px;
    justify-content: space-around;
    /* position: relative; */

}
/* #logo{
    animation: 1s slideright;
} */
/* @keyframes slideleft{
    from {
    margin-left: -10%;
    width: 300%;
  }

  to {
    margin-right: 0%;
    width: 500%;
  }
} */
@keyframes slideright{
    from {
    margin-left: -10%;
    width: 200%;
  }

  to {
    margin-right: 0%;
    width: 300%;
  }
}


#plans{
    /* color:white;  */
    text-decoration:none;
}
.navbar-left{
    display: flex;
    justify-content:space-around;
    align-items: center;
    animation: 1s slideright ;
    animation-fill-mode: forwards;
}

.navbar-right{
    display: flex;
    justify-content: space-evenly;
    align-items: center; 

}

.navbar img{
    width: 3rem;
    height: 3rem;
}
button{
    background-color: blue;
    border-radius: .2rem;
}
.card-contain {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding-right: 1em;
}
.Degree_Doctor{
    font: 2rem;
    text-decoration: none;
}
</style>
