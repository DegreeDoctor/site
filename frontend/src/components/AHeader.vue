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
    <nav> 
        <div class="navbar">
            <div class="left">
                <div class="image-container">
                    <router-link to="/quiz" id="logo"><img src="../assets/Degree_Doctor_logo.png"/></router-link>
                </div>
                <div class="DD">
                    <RouterLink to="/" id="title">Degree Doctor</RouterLink>
                    <div class="fading-effect"></div>
                </div>
            </div>
            <div class="other">
                <DarkModeToggle/>
            </div>
        </div>
    </nav>  
</template>



<!-- <style scoped>
.navbar{
    display: flex;
    background:#835eba;
    justify-content:flex-end;
    align-items: center;
    height: 5rem;
}
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
  background: #835eba;
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
    top: 4%;
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
  background: #835eba;
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
  background: #835eba;
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
top: 5.3%;
right: 75%;
transform: translate(-50%,-50%);
z-index: 2; /* Makes sure this is on top */
}
.DD {
display: flex;
align-items:center;
justify-content: space-between;
position: absolute;
top: 2.88em;
right: 63%;
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
  background: #835eba;
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
  background: #835eba;
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
    color:WHITE;
    text-decoration: none;
    font-size: 1.2rem;
    padding-bottom: 3px;
    justify-content: space-around;

}
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
    background:white;
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
</style> -->


<style scoped>
.navbar{
    display: flex;
    background:#835eba;
    justify-content:space-between;
    align-items: center;
    height: 5rem;
}
.left{
    display: flex;
    flex-direction: row;
    align-items: center;
   padding-left: 17em;
}
img{
    width: 4em;
    margin-right: 2em;

}
#title{
    display:flex;
    color:WHITE;
    text-decoration: none;
    font-size: 1.2rem;
    padding-bottom: 3px;
    justify-content: space-around;
}
.other{
    padding-right: 17em;
}



</style>