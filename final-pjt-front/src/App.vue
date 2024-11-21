<template>
  <header>
    <div class="container">
      <h1>방싕주</h1>

      <nav>
        <RouterLink :to="{ name:'home'}">메인</RouterLink> |
        <RouterLink :to="{ name:'map' }">내 주변 은행 찾기</RouterLink> | 
        <RouterLink :to="{ name: 'currencyExchange' }">환율 계산기</RouterLink> |
        <RouterLink :to="{ name:'portfolio' }">나만의 금융 포트폴리오</RouterLink> |
        <template v-if="isLoggedIn">
          <a href="#" @click.prevent="">마이페이지</a> | 
          <a href="#" @click.prevent="logOut">로그아웃</a>
        </template>
        <template v-else>
          <RouterLink :to="{ name:'SignUpView' }">회원 가입</RouterLink> | 
          <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
        </template>
      </nav>

    </div>
  </header>
  <main class="container">
    <RouterView />
  </main>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useFinStore } from '@/stores/counter';
import { computed } from 'vue';

const store = useFinStore()

// 로그인 상태를 computed 속성으로 처리
const isLoggedIn = computed(() => !!store.token) // !!는 상태를 true/false로 쉽게 바꿔준다.


// 로그아웃 함수
const logOut = () => {
  store.token = null
  localStorage.removeItem('token')
}
</script>


<style scoped>

</style>
