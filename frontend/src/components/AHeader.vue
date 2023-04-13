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
    margin-left: -4em;

}
#title{
    display:flex;
    color:WHITE;
    font-weight: 500;
    text-decoration: none;
    font-size: 1.2rem;
    padding-bottom: 3px;
    justify-content: space-around;
    margin-left: 3em;
    opacity: 0;
}
.other{
    padding-right: 17em;
}
.image-container {
  position: absolute;
  top: 3.5%;
  right: 20%;
  transform: translate(-50%,-50%);
}
.image-container img {
  -webkit-filter: drop-shadow(-4px 5px 5px rgba(0,0,0,0.6));
  filter: drop-shadow(-4px 5px 5px rgba(0,0,0,0.6));
  animation: image-slide 4s cubic-bezier(.5,.5,0,1);
  animation-fill-mode: forwards;
}

@media screen and (max-width: 2560px){
    @keyframes image-slide {
        0% { transform: translateX(-730px) scale(0); }
        60% { transform: translateX(-730px) scale(1); }
        90% { transform: translateX(-1550px) scale(1); }
        100% { transform: translateX(-1550px) scale(1); }  
    }
    @keyframes fade-in{
        from {
            opacity: 0; /* Start with the text fully transparent */
        }
        to {
            opacity: 1; /* End with the text fully opaque */
        }
    }
    .navbar{
        height: 8em;
    }
    img{
        width:5em;
        margin-top: -3em;
    }
    #title{
        font-size:2em;
        margin-left: 10em;
        animation-name: fade-in;
        animation-duration: 1s;
        animation-fill-mode: forwards;
        animation-delay: 3000ms;
    }
    .other{
        padding-right: 29em;

    }
    DarkModeToggle{
        width: 2em;
    }


}













@media screen and (max-width: 1440px){
    @keyframes image-slide {
        0% { transform: translateX(-400px) scale(0); }
        60% { transform: translateX(-400px) scale(1); }
        90% { transform: translateX(-875px) scale(1); }
        100% { transform: translateX(-875px) scale(1); }  
    }
    @keyframes fade-in{
        from {
            opacity: 0; /* Start with the text fully transparent */
        }
        to {
            opacity: 1; /* End with the text fully opaque */
        }
    }
    #title{
        animation-name: fade-in;
        animation-duration: 1s;
        animation-fill-mode: forwards;
        animation-delay: 2750ms;
    }


}
@media screen and (max-width: 1024px){
    @keyframes image-slide {
        0% { transform: translateX(-275px) scale(0); }
        60% { transform: translateX(-275px) scale(1); }
        90% { transform: translateX(-600px) scale(1); }
        100% { transform: translateX(-600px) scale(1); }  
    }
    @keyframes fade-in{
        from {
            opacity: 0; /* Start with the text fully transparent */
        }
        to {
            opacity: 1; /* End with the text fully opaque */
        }
    }
    #title{
        margin-left: 0em;
        animation-name: fade-in;
        animation-duration: 1s;
        animation-fill-mode: forwards;
        animation-delay: 3000ms;
    }
    .other{
        padding-right: 11em;
    }


}
@media screen and (max-width: 768px){
    @keyframes image-slide {
        0% { transform: translateX(-200px) scale(0); }
        60% { transform: translateX(-200px) scale(1); }
        90% { transform: translateX(-425px) scale(1); }
        100% { transform: translateX(-425px) scale(1); }  
    }
    @keyframes fade-in{
        from {
            opacity: 0; /* Start with the text fully transparent */
        }
        to {
            opacity: 1; /* End with the text fully opaque */
        }
    }
    #title{
        margin-left: -2em;
        animation-name: fade-in;
        animation-duration: 1s;
        animation-fill-mode: forwards;
        animation-delay: 3000ms;
    }
    .other{
        padding-right: 9em;
    }
    img{
        margin-top: 1em;
        width:3.5em;
    }
}
@media screen and (max-width: 768px){
    @keyframes image-slide {
        0% { transform: translateX(-200px) scale(0); }
        60% { transform: translateX(-200px) scale(1); }
        90% { transform: translateX(-425px) scale(1); }
        100% { transform: translateX(-425px) scale(1); }  
    }
    @keyframes fade-in{
        from {
            opacity: 0; /* Start with the text fully transparent */
        }
        to {
            opacity: 1; /* End with the text fully opaque */
        }
    }
    #title{
        margin-left: -2em;
        animation-name: fade-in;
        animation-duration: 1s;
        animation-fill-mode: forwards;
        animation-delay: 3000ms;
    }
    .other{
        padding-right: 9em;
    }
    img{
        margin-top: 1em;
        width:3.5em;
    }
}



</style>