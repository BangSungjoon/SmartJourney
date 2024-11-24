<template>
  <header>
    <div class="container">
      <h1>방싕주</h1>

      <nav>
        <RouterLink :to="{ name:'home'}">메인</RouterLink> |
        <RouterLink :to="{ name:'map' }">내 주변 은행 찾기</RouterLink> | 
        <RouterLink :to="{ name: 'currencyExchange' }">환율 계산기</RouterLink> |
        <RouterLink :to="{ name:'portfolio' }">나만의 금융 포트폴리오</RouterLink> |
        <RouterLink :to="{ name: 'saveRecommend' }">예적금 추천 받기</RouterLink> |
        <RouterLink :to="{ name: 'subsidy' }">보조금 찾기</RouterLink> |
        <template v-if="isLoggedIn">
          <template v-if="userId !== null">
            <RouterLink :to="{ name: 'mypage-cart', params: { id: userId } }">마이페이지</RouterLink> |
          </template>
          <a href="#" @click="logOut">로그아웃</a>
        </template>
        <template v-else>
          <RouterLink :to="{ name:'SignUpView' }">회원 가입</RouterLink> | 
          <RouterLink :to="{ name: 'login' }">로그인</RouterLink> |
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
import { useRouter } from 'vue-router'

const store = useFinStore()
const router = useRouter()

// 로그인 상태 및 userId 접근
const isLoggedIn = computed(() => store.isLoggedIn)  // 로그인 상태
const userId = computed(() => store.currentUserId)  // 로그인한 사용자의 id

// 로그아웃 함수
const logOut = () => {
  store.logOut()  // store에서 제공하는 logOut 함수 호출
  router.push({ name: 'home' })  // 로그아웃 후 홈으로 이동
}

</script>

<style scoped>

</style>
