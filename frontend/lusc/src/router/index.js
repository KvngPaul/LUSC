import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView.vue'),
    // children: [
      
    // ]
  },
  {
    path:'/login',
    name: 'Login',
    component: () => import('@/views/LoginView.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('../views/DashboardView.vue'),
    children: [{
      path: '',
      components: {
        userprofile: () => import('../components/dashboard/UserProfile.vue'),
        usertransport: () => import('../components/dashboard/UserTransport.vue'),
        userluggage: () => import('../components/dashboard/UserLuggage.vue'),
        usertradefair: () => import('../components/dashboard/UserTradeFair.vue'),

      }
    }]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
