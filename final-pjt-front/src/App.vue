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
        <template v-if="isLoggedIn">
          <!-- userId가 있을 때만 렌더링 -->
          <template v-if="userId !== null">
            <RouterLink :to="{ name: 'mypage', params: { id: userId } }">마이페이지</RouterLink> |
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
import { computed, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useFinStore()
const router = useRouter()
const userId = ref(null) // 현재 사용자의 id를 저장할 변수

// 로그인 상태를 computed 속성으로 처리
const isLoggedIn = computed(() => !!store.token) // !!는 상태를 true/false로 쉽게 바꿔준다.


// 로그아웃 함수
const logOut = () => {
  store.token = null
  localStorage.removeItem('token')
  router.push({ name: 'home' })
}

// 현재 사용자의 Id를 받아오기
onMounted(() => {
  const token = localStorage.getItem('token');
  if (token) {
    axios.get('http://127.0.0.1:8000/accounts/user/', {
      headers: {
        'Authorization': `Token ${token}`,
      }
    })
      .then(response => {
        console.log(response.data.pk)
        userId.value = response.data.pk;
      })
      .catch(error => {
        console.error('Failed to fetch user information:', error);
      });
  }
  console.log(userId.value)
});
</script>


<style scoped>

</style>
