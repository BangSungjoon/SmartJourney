<template>
    <div>
      <HomeBanner />
      <HomeFeatures />
      <HomeServices />
      <HomeExchange/>
    </div>
  </template>
  
  <script>
  import HomeBanner from '@/components/pages/home/HomeBanner.vue';
  import HomeFeatures from '@/components/pages/home/HomeFeatures.vue';
  import HomeServices from '@/components/pages/home/HomeServices.vue';
import HomeExchange from '@/components/pages/home/HomeExchange.vue';
  export default {
    components: {
      HomeBanner,
      HomeFeatures,
      HomeServices,
      HomeExchange
    },
  };
  </script>
  
  <style scoped>
  /* 홈 페이지 전용 스타일 */
  </style>
  