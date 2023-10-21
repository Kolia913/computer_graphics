import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import FractalView from '../views/FractalView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: {
        layout: 'empty',
      },
    },
    {
      path: '/fractals',
      name: 'fractals',
      component: FractalView,
      meta: {
        layout: 'empty',
      },
    },
  ],
});

export default router;
