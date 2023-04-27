import { createRouter, createWebHistory } from "vue-router";

import Login from '../views/Login.vue'
import Additionalinfo from '../views/Additionalinfo.vue'
import Help from '../views/Help.vue'
import Home from '../views/Home.vue'

const routes = [
    {
        name: 'Login',
        path: '/login',
        component: Login,
    },

    {
        name: 'Additionalinfo',
        path: '/additionalinfo/:email',
        component: Additionalinfo,
    },
    {
        name: 'Help',
        path: '/help',
        component: Help,
    },
    {
        name: 'Home',
        path: '/',
        component: Home,
    }

];
const router = Router();
export default router;
function Router() {
    const router = new createRouter({
        history: createWebHistory(),
        routes,
    });
    return router;
}
