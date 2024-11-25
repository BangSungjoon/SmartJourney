<template>
    <section class="hero-section">
      <div class="hero-content slide-top">
        <p class="hero-subtitle">간단한 질문으로 나에게 최적화된 금융 플랜을 설계하세요.</p>
        <h1 class="hero-title">
          고객님의 <span class="highlight">투자목표</span>를 설정하여 주세요.
        </h1>
        <p class="hero-description">
          고객님의 투자성향 분석을 통해<br />
          고객님을 위한 맞춤형 글로벌 자산배분 포트폴리오를 제안해 드립니다.
        </p>
        <RouterLink to="/question/1">
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
    background-image: url('@/assets/images/portfolio/port1.jpg'); /* 배경 이미지 경로 */
    background-size: cover; /* 배경 크기 */
    background-position: center; /* 배경 위치 */
    background-repeat: no-repeat; /* 배경 반복 금지 */
    color: white; /* 기본 글자 색상 */
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  /* 콘텐츠 스타일 */
  .hero-content {
    max-width: 600px; /* 컨텐츠 최대 너비 */
    padding: 20px; /* 모바일 뷰에서도 여백 확보 */
  }
  
  /* 텍스트 스타일 */
  .hero-subtitle {
    font-size: 2rem;
    margin-bottom: 10px;
    color: #f1f1f1;
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
  