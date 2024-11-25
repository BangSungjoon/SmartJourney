<template>
    <div>
      <HomeBanner />
      <HomeFeatures />
      <HomeServices />
    </div>
  </template>
  
  <script>
  import HomeBanner from '@/components/pages/home/HomeBanner.vue';
  import HomeFeatures from '@/components/pages/home/HomeFeatures.vue';
  import HomeServices from '@/components/pages/home/HomeServices.vue';
  
  export default {
    components: {
      HomeBanner,
      HomeFeatures,
      HomeServices,
    },
  };
  </script>
  
  <style scoped>
  /* 홈 페이지 전용 스타일 */
  </style>
  