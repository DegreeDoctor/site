<script>
import { useImage } from "@vueuse/core";
import { useStore } from "../stores/store";
import DarkModeToggle from "./DarkModeToggle.vue";
import PlansList from "./PlansList.vue";

export default {
    components: {
        DarkModeToggle,
        PlansList,
    },
    methods: {
        sendQuiz() {
            this.$router.push("/quiz");
        },
    },
};
</script>

<template>
    <q-header elevated class="bg-secondary text-white header" height-hint="98">
        <q-toolbar>
            <q-toolbar-title>
                <q-avatar @click="sendQuiz()">
                    <img src="../assets/Degree_Doctor_logo.png" />
                </q-avatar>
                <a @click="sendQuiz()"> Degree Doctor</a>
            </q-toolbar-title>

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
        </div>
    </nav>  
</template>

<style scoped>
.navbar{
    display: flex;
    background:turquoise;
    justify-content:flex-end;
    align-items: center;
    height: 5rem;
}
.image-container {
  position: absolute;
  top: 4.8%;
  right: 20%;
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
display: flex;
align-items:center;
justify-content: space-between;
  position: absolute;
  top: 2.88em;
  right:75%;
  transform: translate(-50%,-50%);
  z-index: 1; /* Places this below the image container */
  margin-left: -1000px;
}
.DD .fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: turquoise;
  -webkit-animation: text-slide 4s cubic-bezier(.1, 0, 0.5, 0.5);
  animation: text-slide s cubic-bezier(.1, 0, 0.5, 0.5);
  animation-fill-mode: forwards;
  -webkit-animation-fill-mode: forwards;
}
.fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: white;
}   
@media screen and (min-width: 1440px){
    @keyframes image-slide {
        0% { transform: translateX(-390px) scale(0); }
        60% { transform: translateX(-390px) scale(1); }
        90% { transform: translateX(-1000px) scale(1); }
        100% { transform: translateX(-1000px) scale(1); }  
    }
    @keyframes text-slide {
        100% { width: 100%; }
        75%{ width: 100%; }
        60% { width: 0; }
        0% { width: 0; }
        75%{ width: 100%; }
        100% { width: 0%; }

    }
}
/* Slides the image from right (150px) to left (-250px) */
@media screen and (max-width: 1440px){
    @keyframes image-slide {
        0% { transform: translateX(-390px) scale(0); }
        60% { transform: translateX(-390px) scale(1); }
        90% { transform: translateX(-1000px) scale(1); }
        100% { transform: translateX(-1000px) scale(1); }  
    }
    @keyframes text-slide {
        100% { width: 100%; }
        75%{ width: 100%; }
        60% { width: 0; }
        0% { width: 0; }
        75%{ width: 100%; }
        100% { width: 0%; }

    }
}
@media screen and (max-width: 1024px){
.image-container {
    position: absolute;
    top: 6%;
    right: 10%;
    transform: translate(-50%,-50%);
    z-index: 2; /* Makes sure this is on top */
}
.DD {
display: flex;
align-items:center;
justify-content: space-between;
position: absolute;
top: 2.88em;
right:70%;
transform: translate(-50%,-50%);
z-index: 1; /* Places this below the image container */
margin-left: -1000px;
}
.DD .fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: turquoise;
  -webkit-animation: text-slide 4s cubic-bezier(.1, 0, 0.5, 0.5);
  animation: text-slide s cubic-bezier(.1, 0, 0.5, 0.5);
  animation-fill-mode: forwards;
  -webkit-animation-fill-mode: forwards;
}
.fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: white;
}  

    @keyframes image-slide {
        0% { transform: translateX(-350px) scale(0); }
        60% { transform: translateX(-350px) scale(1); }
        90% { transform: translateX(-800px) scale(1); }
        100% { transform: translateX(-800px) scale(1); }  
    }
    @keyframes text-slide {
        100% { width: 100%; }
        75%{ width: 100%; }
        60% { width: 0; }
        0% { width: 0; }
        75%{ width: 100%; }
        100% { width: 0%; }

    }
}
@media screen and (max-width: 768px){
.image-container {
position: absolute;
top: 6%;
right: 85%;
transform: translate(-50%,-50%);
z-index: 2; /* Makes sure this is on top */
}
.DD {
display: flex;
align-items:center;
justify-content: space-between;
position: absolute;
top: 2.88em;
right: 70%;
transform: translate(-50%,-50%);
z-index: 1; /* Places this below the image container */
margin-left: -1000px;
}
.DD .fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: turquoise;
  -webkit-animation: text-slide 4s cubic-bezier(.1, 0, 0.5, 0.5);
  animation: text-slide s cubic-bezier(.1, 0, 0.5, 0.5);
  animation-fill-mode: forwards;
  -webkit-animation-fill-mode: forwards;
}
.fading-effect {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  width: 100%;
  background: white;
}  
    @keyframes image-slide {
        0% { transform: translateX(235px) scale(0); }
        60% { transform: translateX(235px) scale(1); }
        90% { transform: translateX(-80px) scale(1); }
        100% { transform: translateX(-80px) scale(1); }  
    }
    @keyframes text-slide {
        100% { width: 100%; }
        75%{ width: 100%; }
        60% { width: 0; }
        0% { width: 0; }
        75%{ width: 100%; }
        100% { width: 0%; }
    }
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
.header {
    display: flex;
    justify-content: center;
    align-items: center;
    max-height: 54px;
    height: 100%;
}
</style>
