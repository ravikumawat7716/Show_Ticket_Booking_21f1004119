// import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

router.beforeEach((to, from, next) => {
    const requiresAuth = to.meta.requiresAuth;
    const requiredrole = to.meta.requiredrole;

    if (requiresAuth && !localStorage.getItem('token')) {
        localStorage.removeItem('token');
        localStorage.removeItem('role');
        localStorage.removeItem('username');
        next('/login');
    }
    else if (requiredrole && localStorage.getItem('role') != requiredrole) {
        next('/');
    }
    else {
        next();
    }});

const app = createApp(App)

app.use(router)

app.mount('#app')
