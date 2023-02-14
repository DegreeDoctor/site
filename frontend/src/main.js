import { createApp } from "vue";
import { createPinia } from "pinia";
import { Quasar, Notify, Dialog } from "quasar";

import App from "./App.vue";
import router from "./router";

// Import icon libraries
import "@quasar/extras/material-icons/material-icons.css";
import "@quasar/extras/fontawesome-v6/fontawesome-v6.css";

// Import Quasar css
import "quasar/src/css/index.sass";

import "./assets/main.css";

const app = createApp(App);
const pinia = createPinia();
app.use(Quasar, {
    plugins: {
        Notify,
        Dialog,
    }, // import Quasar plugins and add here
    config: {
        notify: {
            /* look at QuasarConfOptions from the API card */
        },
    },
});
app.use(pinia);
app.use(router);

app.mount("#app");
