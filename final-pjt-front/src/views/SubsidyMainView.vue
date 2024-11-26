<template>
    <section class="hero-section">
      <div class="hero-content slide-top">
        <!-- <p class="hero-subtitle">놓치기 쉬운 혜택, 이제 한눈에 찾아보세요</p> -->
        <h1 class="hero-title">
          
          <span class="highlight">놓치기 쉬운 혜택,</span>이제 한눈에 찾아보세요
         
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
/* Hero Section 배경 이미지 스타일 */
.hero-section {
  position: relative; /* 부모 요소 기준으로 자식 요소 배치 */
  height: 100vh; /* 화면 전체 높이 */
  display: flex;
  align-items: center; /* 세로 중앙 정렬 */
  justify-content: flex-start; /* 가로 정렬: 왼쪽으로 */
  overflow: hidden;
  padding-left: 5%; /* 왼쪽에 여백 추가 */
}

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
  z-index: 0; /* 배경 이미지의 레이어 순서를 뒤로 설정 */
  font-family: 'Noto Sans KR', sans-serif;
  }


/* 콘텐츠 스타일 */
.hero-content {
  position: relative; /* 텍스트를 배경 이미지 위로 */
  z-index: 10; /* 텍스트를 배경 이미지 위에 표시 */
  max-width: 40%; /* 콘텐츠 영역을 화면의 40%로 설정 */
  padding: 20px; /* 여백 확보 */
  text-align: left; /* 텍스트를 왼쪽 정렬 */
}

/* 텍스트 스타일 */
.hero-subtitle {
  font-size: 1.3rem;
  margin-bottom: 10px;
  color: #000000;
}

.hero-title {
  font-size: 3.2rem;
  font-weight: bold;
  margin-bottom: 20px;
  white-space: nowrap; /* 줄바꿈 방지 */
}


.hero-title .highlight {
  color: #ffd700; /* 강조 텍스트 색상 */
}

.hero-description {
  font-size: 1.4rem;
  line-height: 1.6;
  margin-bottom: 30px;
  color: #000000; /* 설명 텍스트도 검정색 */
  font-family: 'Noto Sans KR', sans-serif;
  
}

/* 버튼 스타일 */
.hero-button {
  font-size: 1.2rem;
  padding: 10px 20px;
  background-color: #ffd700; /* 버튼 색상 */
  color: #000; /* 버튼 텍스트 색상 */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
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