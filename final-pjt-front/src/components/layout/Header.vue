<template>
    <header class="site-header">
      <!-- 로고 -->
      <!-- <a href="/"> -->
      <RouterLink :to="{ name: 'home' }" class="no-underline">
        <div class="logo">
          <img src="@/assets/images/home/logo.png" alt="사이트 로고" />
          <span>SJ</span>
        </div>
      </RouterLink>
      <!-- </a> -->
  
      <!-- 네비게이션 메뉴 -->
      <nav class="nav-menu">
        <ul>
          <!-- <li><RouterLink :to="{ name: 'home' }">메인</RouterLink></li> -->
          <!-- <li><a href="/portfolio_main">포트폴리오</a></li> -->
          <li><RouterLink :to="{ name:'portfolio_main' }">포트폴리오</RouterLink></li>
          <li><RouterLink :to="{ name:'map' }">내 주변 은행 찾기</RouterLink></li>
          <li><RouterLink :to="{ name:'Recommend' }">예금 적금 추천</RouterLink></li>
          <li><RouterLink :to="{ name:'subsidyMain' }">보조금 찾기</RouterLink></li>

        </ul>
      </nav>
  
      <!-- 사용자 메뉴 (로그인 및 기타 옵션) -->
      <div class="user-menu">
        <template v-if="userId !== null">
          <!-- <a href="/mypage/:id">마이페이지</a> -->
          <RouterLink :to="{ name: 'mypage-cart', params: { id: userId } }">마이페이지</RouterLink>
          <a href="#" @click="logOut">로그아웃</a>
        </template>
        <template v-else>
          <RouterLink :to="{ name: 'login' }">로그인</RouterLink>
          <RouterLink :to="{ name:'SignUpView' }">회원가입</RouterLink>
        </template>
      </div>
    </header>
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
/* 헤더 전체 스타일 */
.site-header {
  display: flex; /* 가로 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  justify-content: space-between; /* 양쪽 끝 정렬 */
  padding: 10px 20px; /* 내부 여백 */
  background-color: #fff; /* 흰색 배경 */
  border-bottom: 1px solid #ddd; /* 하단 구분선 */
  font-family: 'Noto Sans KR', sans-serif;
}

/* 로고 스타일 */
.logo {
  display: flex; /* 로고와 텍스트 가로 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  gap: 10px; /* 로고와 텍스트 간 간격 */
}

.logo img {
  height: 60px; /* 로고 이미지 크기 */
}

.logo span {
  font-size: 1.2rem;
  font-weight: bold; /* 텍스트 굵게 */
  color: #333; /* 텍스트 색상 */
}

/* 네비게이션 메뉴 스타일 */
.nav-menu ul {
  display: flex; /* 가로 정렬 */
  list-style: none; /* 기본 리스트 스타일 제거 */
  gap: 30px; /* 메뉴 간 간격 */
  margin: 0;
  padding: 0;
}

.nav-menu a {
  text-decoration: none; /* 밑줄 제거 */
  color: #333; /* 텍스트 색상 */
  font-size: 1rem; /* 텍스트 크기 */
  font-weight: 500; /* 중간 굵기 */
  transition: color 0.3s ease; /* 호버 시 색상 전환 효과 */
}

.nav-menu a:hover {
  color: #007bff; /* 호버 시 파란색으로 변경 */
}

/* 사용자 메뉴 스타일 */
.user-menu {
  display: flex; /* 가로 정렬 */
  gap: 15px; /* 버튼 간 간격 */
}

.user-menu a {
  text-decoration: none; /* 밑줄 제거 */
  color: #333; /* 텍스트 색상 */
  font-size: 1rem; /* 텍스트 크기 */
  font-weight: 500; /* 텍스트 굵기 */
  transition: color 0.3s ease; /* 호버 시 색상 전환 효과 */
}

.user-menu a:hover {
  color: #007bff; /* 호버 시 파란색으로 변경 */
}

.no-underline {
  text-decoration: none;
}
</style>
