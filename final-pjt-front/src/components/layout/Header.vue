<template>
    <header class="site-header">
      <!-- 로고 -->
      <div class="logo">
        <img src="@/assets/images/home/logo.png" alt="사이트 로고" />
        <span>이름 들어갈 곳</span>
      </div>
  
      <!-- 네비게이션 메뉴 -->
      <nav class="nav-menu">
        <ul>
          <li><a href="/">메인</a></li>
          <li><a href="/portfolio_main">포트폴리오</a></li>
          <li><a href="/map">내 주변 은행 찾기</a></li>
          <li><a href="/recommend">예금 적금 추천</a></li>
        </ul>
      </nav>
  
      <!-- 사용자 메뉴 (로그인 및 기타 옵션) -->
      <div class="user-menu">
        <a href="/login">로그인</a>
        <a href="/signup">회원가입</a>
        <a href="#">마이페이지</a>

      </div>
    </header>
  </template>
  

<script setup>

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
</style>
