import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/TestView.vue'),
    },
    {
      path: '/users/:user',
      name: 'users',
      component: () => import('../views/UsersView.vue'),
    }
  ],
})

export default router
