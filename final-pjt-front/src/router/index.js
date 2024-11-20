import { createRouter, createWebHistory } from 'vue-router'
import MapView from '@/views/MapView.vue'
import HomeView from '@/views/HomeView.vue'
import PortfolioView from '@/views/PortfolioView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import SaveRecommendView from '@/views/SaveRecommendView.vue'
import PortfolioListView from '@/views/PortfolioListView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue'),
    // },
    {
      path:'/map',
      name:'map',
      component: MapView,
    },
    {
      path:'/portfolio',
      name:'portfolio',
      component: PortfolioView,
    },
    {
      path: '/portfolio/:id',
      name: 'portlist',
      component: PortfolioListView
    },
    {
			path: '/signup',
			name: 'SignUpView',
			component: SignUpView
		},
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/saveRecommend',
      name: 'saveRecommend',
      component: SaveRecommendView
    },
  ],
})

export default router
