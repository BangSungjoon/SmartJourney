<template>
    <section class="hero-section">
      <div class="hero-content slide-top">
        <p class="hero-subtitle">놓치기 쉬운 혜택, 이제 한눈에 찾아보세요</p>
        <h1 class="hero-title">
          
          내가 몰랐던 <span class="highlight">숨겨진 혜택</span>도 놓치지 마세요.
         
        </h1>
        <p class="hero-description">
          단계별 설문으로 고객님께 꼭 필요한 <span class="highlight">보조금</span>과 <span class="highlight">지원 정보</span>를 추천합니다. 
        </p>
        <RouterLink to="/subsidy">
          <button class="hero-button">START</button>
        </RouterLink>
      </div>
    </section>
  </template>

<script setup>

</script>

<style scoped>
/* Hero Section 스타일 */
.hero-section {
  display: flex;
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  text-align: center; /* 텍스트 중앙 정렬 */
  height: 100vh; /* 화면 전체 높이 */
  background-color: white; /* 배경 흰색 */
  color: rgb(0, 0, 0); /* 기본 글자 색상 */
  font-family: 'Noto Sans KR', sans-serif;
  position: relative; /* 배경 이미지 조정을 위한 상대 위치 */
}

/* 배경 이미지 스타일 */
.hero-section::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0; /* 배경 이미지를 오른쪽으로 정렬 */
  width: 50%; /* 배경 이미지를 화면의 절반 너비로 설정 */
  height: 100%; /* 높이를 화면 높이에 맞춤 */
  background-image: url('@/assets/images/shared/보조금4.jpg'); /* 배경 이미지 경로 */
  background-size: cover; /* 배경 이미지가 공간을 채우도록 설정 */
  background-repeat: no-repeat; /* 이미지 반복 금지 */
  background-position: center; /* 이미지 중앙 정렬 */
}
/* 콘텐츠 스타일 */
.hero-content {
  position: absolute; /* 위치를 지정하기 위해 absolute 사용 */
  left: 10%; /* 화면 왼쪽에서 10% 떨어진 곳에 배치 */
  top: 30%; /* 화면 세로 중앙 기준으로 배치 */
  transform: translateY(-50%); /* 세로 중앙 정렬 */
  max-width: 33%; /* 콘텐츠 영역을 화면의 1/3 너비로 설정 */
  padding: 20px; /* 모바일 뷰에서도 여백 확보 */
}

/* 텍스트 스타일 */
.hero-subtitle {
  font-size: 2rem;
  margin-bottom: 10px;
  color: #000000;
}

.hero-title {
  font-size: 3rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.hero-title .highlight {
  color: #ffd700; /* 강조 텍스트 색상 */
}

.hero-description {
  font-size: 1.5rem;
  line-height: 1.6;
  margin-bottom: 30px;
}

/* 버튼 스타일 */
.hero-button {
  font-size: 1.2rem;
  font-weight: bold;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #ffd700;
  color: #333;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hero-button:hover {
  background-color: #f7c600;
}

/* 애니메이션 스타일 */
.slide-top {
  animation: slide-top 0.8s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
}

@keyframes slide-top {
  0% {
    transform: translateY(50px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}
</style>