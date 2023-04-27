import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import 'vuetify/dist/vuetify.css'
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@mdi/font/css/materialdesignicons.css' 
import router from './router/router.js'

//setting vutify 3
const vuetify = createVuetify({
    components,
    directives,
    icons : {
        iconfont: 'fa' || 'md' || 'mdiSvg',
    }
  })
const app = createApp(App)
app.use(createPinia());
app.use(router)
app.use(vuetify);
app.mount('#app');
