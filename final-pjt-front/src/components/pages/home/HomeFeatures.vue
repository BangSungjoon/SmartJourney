<template>
    <section class="home-features">
      <!-- 첫 번째 섹션 -->
      <div class="feature-row">
        <div class="feature-text">
          <h3>1. 금융 포폴 만들기</h3>
          <p>돈 관리와 카드 관리를 한눈에 보고, 일정까지 스마트하게 관리해 보세요.</p>
          <a href="#">이동 링크</a>
        </div>
        <div class="image-grid">
          <img src="@/assets/images/home/feature1.jpg" alt="Feature 1" />
        </div>
      </div>
  
      <!-- 두 번째 섹션 -->
      <div class="feature-row reverse">
        <div class="feature-text">
          <h3>2. 환율 계산</h3>
          <p>송금 전 사기 방지 알림과 은행 점검 시간을 걱정하지 않아도 되는 간편함을 경험하세요.</p>
          <a href="#">이동 링크</a>
        </div>
        <div class="image-grid">
          <img src="@/assets/images/home/feature2.jpg" alt="Feature 2" />
        </div>
      </div>


      <!-- 세 번째 섹션 -->
      <div class="feature-row">
        <div class="feature-text">
          <h3>3. 예적금 상품 추천</h3>
          <p>돈 관리와 카드 관리를 한눈에 보고, 일정까지 스마트하게 관리해 보세요.</p>
          <a href="#">이동 링크</a>
        </div>
        <div class="image-grid">
          <img src="@/assets/images/home/feature1.jpg" alt="Feature 1" />
        </div>
      </div>
    </section>
  </template>
  
  <style scoped>
  .home-features {
    padding: 50px 20px;
    background-color: #f9f9f9;
    display: flex;
    flex-direction: column;
    gap: 50px; /* 섹션 간 간격 */
    font-family: 'Noto Sans KR', sans-serif;
  }
  
  .feature-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 7px; /* 텍스트와 이미지 간 간격 */
    padding: 0 4rem; /* 섹션 좌우 여백 추가 */
  }
  
  .feature-row.reverse {
    flex-direction: row-reverse; /* 텍스트와 이미지를 반대로 배치 */
  }
  
  .feature-text {
    flex: 1;
    max-width: 50%; /* 텍스트 너비 제한 */
  }
  
  .feature-text h3 {
    font-size: 2rem;
    color: #333;
    margin-bottom: 20px;
  }
  
  .feature-text p {
    font-size: 1.5rem;
    color: #666;
    line-height: 1.6;
  }
  
  .image-grid {
    flex: 1;
    display: flex;
    justify-content: center;
  }
  
  .image-grid img {
  width: 40rem; /* 부모 컨테이너에 맞춤 */
  height: auto; /* 원본 비율 유지 */
  object-fit: cover; /* 필요 시 이미지 잘림 방지 */
  border-radius: 0.625rem; /* 모서리를 둥글게 (10px = 0.625rem) */
  box-shadow: 0 0.25rem 0.625rem rgba(0, 0, 0, 0.1); /* 그림자 추가 */
}
  </style>
  