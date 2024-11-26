<template>
    <section class="hero-section">
      <div class="hero-content slide-top">
        <div class="hero-title-second-line">
          간단한 질문으로<br />
          나를 위한 <span class="highlight">맞춤형</span> <span class="highlight">금융 플랜</span>을 설계하세요.
        </div>
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

.hero-content {
    max-width: 600px; /* 컨텐츠 최대 너비 */
    padding: 20px; /* 모바일 뷰에서도 여백 확보 */
    text-align: center; /* 콘텐츠 내부 텍스트 정렬 */
}

.hero-title-second-line {
    font-size: 3rem; /* 글꼴 크기 */
    font-weight: bold; /* 글꼴 굵기 */
    margin: 0 auto; /* 블록을 가운데로 */
    display: inline-block; /* 블록 요소를 인라인으로 처리 */
    line-height: 1.4; /* 줄 간격 */
    white-space: normal; /* 자동 줄바꿈 허용 */
    text-align: center; /* 텍스트 중앙 정렬 */
}

.hero-title-second-line .highlight {
    color: #ffd700; /* 강조 텍스트 색상 */
}

.hero-description {
    font-size: 1rem; /* 설명 텍스트 크기 */
    line-height: 1.6;
    margin: 30px 0 30px;
    max-width: 100%; /* 너비 제한 해제 */
    white-space: nowrap; /* 줄바꿈 방지 */
}

  
  /* 버튼 스타일 */
  .hero-button {
    font-size: 1.2rem;
    font-weight: bold;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #fad02c;
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
  