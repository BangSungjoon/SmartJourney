<template>
  <div id="app">
    <Header />
    <router-view /> <!-- HomePage가 여기에 렌더링 -->
    <Footer />
  </div>
</template>

<script>
import Header from "@/components/layout/Header.vue";
import Footer from "@/components/layout/Footer.vue";

export default {
  components: {
    Header,
    Footer,
  },
};
</script>

<style>
/* 전역 스타일 */
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
  color: #333;
}

a {
  text-decoration: none;
  color: inherit;
}
</style>
