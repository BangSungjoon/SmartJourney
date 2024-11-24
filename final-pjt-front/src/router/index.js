import { createRouter, createWebHistory } from 'vue-router'
import MapView from '@/views/MapView.vue'
import HomeView from '@/views/HomeView.vue'
import PortfolioView from '@/views/PortfolioView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import SaveRecommendView from '@/views/SaveRecommendView.vue'
import PortfolioListView from '@/views/PortfolioListView.vue'
import CurrencyExchangeView from '@/views/CurrencyExchangeView.vue'
import MyPageView from '@/views/MyPageView.vue'
import MyPageCartView from '@/views/MyPageCartView.vue'
import ProductDetailView from '@/views/ProductDetailView.vue'
import SubsidyView from '@/views/SubsidyView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/map',
      name: 'map',
      component: MapView,
    },
    {
      path: '/portfolio',
      name: 'portfolio',
      component: PortfolioView,
    },
    {
      path: '/portfolio/:id',
      name: 'portlist',
      component: PortfolioListView
    },
    {
      path: '/currency_exchange',
      name: 'currencyExchange',
      component: CurrencyExchangeView
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
    // 마이페이지
    // {
    //   path: '/mypage/:id',
    //   name: 'mypage',
    //   component: MyPageView
    // },
    // {
    //   path: '/mypage/:id/cart',
    //   name: 'mypage-cart',
    //   component: MyPageCartView
    // },
    {
      path: '/mypage/:id',
      // name: 'mypage',
      component: MyPageView,
      props: true, // props로 id 값을 전달
      children: [
        // {
        //   path: '', // 기본 경로를 빈 문자열로 설정
        //   redirect: 'cart', // 기본적으로 cart로 리다이렉트
        // },
        {
          path: 'cart',
          name: 'mypage-cart',
          component: MyPageCartView,
          props: true, // id 값을 전달
        },
        {
          path: 'portfolio',
          name: 'mypage-portlist',
          component: PortfolioListView,
          props: true, // id 값을 전달
        },
        {
          path: 'subsidy',
          name: 'mypage-subsidy',
          component: () => import('@/components/MySubsidy.vue')
        }
      ],
    },
    {
      path: '/productDetail/:id',
      name: 'productDetail',
      component: ProductDetailView,
      props: true, // params를 props로 전달
    },
    {
      path: '/subsidy',
      name: 'subsidy',
      component: SubsidyView,
    },
  ],
})

export default router
