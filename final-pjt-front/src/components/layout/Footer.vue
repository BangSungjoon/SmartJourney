<template>
    <footer class="footer">
      <div class="footer-content">
        <p>© 2024 방싕주 팀 - 모든 권리 보유</p>
        <nav>
          <ul class="footer-links">
            <li><a href="/about">회사소개</a></li>
            <li><a href="/policy">이용약관</a></li>
            <li><a href="/privacy">개인정보처리방침</a></li>
            <li><a href="/contact">문의하기</a></li>
          </ul>
        </nav>
      </div>
    </footer>
  </template>
  
  <script>
  export default {
    name: "Footer",
  };
  </script>
  
  <style scoped>
  /* Footer 전체 영역 */
  .footer {
    position: relative; /* 페이지의 흐름에 맞추어 배치 */
    width: 100%; /* 전체 화면 너비 */
    height: 70px; /* 고정 높이 */
    background-color: #333; /* 배경색 */
    color: white; /* 텍스트 색상 */
    display: flex; /* Flexbox 사용 */
    justify-content: center; /* 가로 중앙 정렬 */
    align-items: center; /* 세로 중앙 정렬 */
    padding: 0 20px; /* 좌우 여백 */
    box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1); /* 상단 그림자 */
    z-index: 1000; /* 다른 요소 위에 표시 */
  }
  
  /* Footer 콘텐츠 */
  .footer-content {
    text-align: center;
  }
  
  /* Footer 링크 목록 */
  .footer-links {
    display: flex; /* 가로 나열 */
    gap: 20px; /* 항목 간 간격 */
    list-style: none; /* 기본 목록 스타일 제거 */
    margin: 10px 0 0;
    padding: 0;
  }
  
  /* Footer 링크 스타일 */
  .footer-links li a {
    color: white;
    text-decoration: none; /* 밑줄 제거 */
    font-size: 0.9rem;
  }
  
  .footer-links li a:hover {
    text-decoration: underline; /* 마우스 오버 시 밑줄 표시 */
    color: #ffd700; /* 강조 색상 */
  }


  </style>