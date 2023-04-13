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
 <div class="navbar">
    <div class="left">
        <div class="image-container">
            <router-link to="/quiz" id="logo"><img src="../assets/Degree_Doctor_logo.png"/></router-link>
        </div>
    </div>
 </div>
</template>

<style scoped>
.image-container {
  position: absolute;
  top: 3.5%;
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
</style>
