import { createRouter, createWebHistory } from 'vue-router'
import HomePageVue from '@/components/HomePage.vue'
import LoginPage from '@/components/LoginPage.vue'
import AdminDashboard from '@/components/AdminDashboard.vue'
import UpdateVenue from '@/components/UpdateVenue.vue'
import UserRegistration from '@/components/UserRegistration.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePageVue,
      // meta: { requiresAuth: true, requiredrole: 'user' },
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage,
    },
    {
      path: '/signup',
      name: 'Register',
      component: UserRegistration,
    },
    {
      path: '/admindashboard',
      name: 'admindashboard',
      component: AdminDashboard,
      meta: { requiresAuth: true, requiredrole: 'admin' },
    },
    { path: '/updatevenue/:id', 
      name: 'updatevenue', 
      component: UpdateVenue
     },
  ],
})

export default router
