<script>
import { useStore } from "../stores/store";
import programsJson from "../data/programs.json";

export default {
    name: "DegreeChecker",
    data() {
        return {
            programsData: programsJson,
            store: useStore(),
        };
    },
    computed: {
        majors(){
            let majors = []//this.programsData["2022-2023"]["Computer Science"]
            let currentDegree = this.store.getCurrentDegree;
            for(const major in currentDegree["majors"]){
                let currentMajor = currentDegree["majors"][major];
                majors.push(this.programsData["2022-2023"][currentMajor]);
            }
            console.log("majors");
            console.log(majors);
            return majors;
        },
        course(){
            let course = []
            let currentDegree = this.store.getCurrentDegree;
            for(const semester in currentDegree["template"]){
                course = [...course, ...currentDegree["template"][semester]];
            }
            console.log("course");
            console.log(course);
            return course;
        },
        allrequirements(){
            let majors = this.majors;
            let allrequirements = []
            for(const major in majors){
                for(const req in majors[major]["requirements"]){
                    allrequirements.push(req);
                }
            }
            console.log("all requirements");
            console.log(allrequirements);
            return allrequirements;
        },
        credits(){
            let majors = this.majors;
            let credits = []
            for(const major in majors){
                for(const req in majors[major]["requirements"]){
                    credits.push(majors[major]["requirements"][req]);
                }
            }
            console.log("credits");
            console.log(credits);
            return credits;
        },
        unfulfilled(){
            let majors = this.majors;
            let course = this.course;
            let unfulfilled = []
            for(const major in majors){
                for(const req in majors[major]["requirements"]){
                    if(!course.includes(req)){
                        unfulfilled.push(req);
                    }
                }
            }
            console.log("unfulfilled");
            console.log(unfulfilled);
            return unfulfilled;
        },
        fulfilled(){
            let majors = this.majors;
            let course = this.course;
            console.log(course);
            let fulfilled = []
            for(const major in majors){
                for(const req in majors[major]["requirements"]){
                    if(course.includes(req)){
                        fulfilled.push(req);
                    }
                }
            }
            console.log("fulfilled");
            console.log(fulfilled);
            return fulfilled;
        },
    },
    methods:{
        openNav() {
            document.getElementById("dropdown").style.display = "block";
        },

        closeNav() {
            document.getElementById("dropdown").style.display = "block";
        },
    },

};
</script>

<template>
<q-card class = "required">
    <q-btn class="openbtn" @click="openNav()"> </q-btn>
    <q-btn class="closebtn" @click="closeNav()">x</q-btn>

    <q-list dense id="dropdown">
        
        <h>All Requirements</h>
        <q-item v-for = "item in allrequirements" :key = "item">
            {{ item }}
        </q-item>
        <h>All credits</h>
        <q-item v-for = "item in credits" :key = "item">
            {{ item }}
        </q-item>
        <h>Fulfilled Credits/Requirements</h>
        <q-item v-for = "item in fulfilled" :key = "item">
            {{ item }}
        </q-item>
        <h>Unfulfilled Credits/Requirements</h>
        <q-item v-for = "item in unfulfilled" :key = "item">
            {{ item }}
        </q-item>
    </q-list>
</q-card>
</template>
<style lang="scss">
.required {
    display: grid;
    text-align: left;
    font-size: 1.5rem;
    font-weight: 600;
    margin: 200px;
    top: 150px;
    bottom: 1000px;
    background-color: white;
}
</style>
