<template>
  <header>
    <div>
      <h1>메인 화면입니다.</h1>

      <nav>
        <RouterLink :to="{ name:'home'}">메인</RouterLink> |
        <RouterLink :to="{ name:'map' }">내 주변 은행 찾기</RouterLink> |
      </nav>

    </div>
  </header>

  <RouterView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>


<style scoped>

</style>
